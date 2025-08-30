import pandas as pd
import numpy as np
import re

def shorten_uri(uri: str, prefixes: dict) -> str:
    """URIを短縮形に変換する関数
    Args:
        uri: 完全なURI文字列
        prefixes: プレフィックスの辞書 {プレフィックス: 名前空間}
    Returns:
        str: 短縮形のURI（適切なプレフィックスが見つからない場合は完全なURI）
    """
    # すでに短縮形の場合はそのまま返す
    if ':' in uri and not uri.startswith('http'):
        return uri
        
    # 最長マッチのプレフィックスを探す
    longest_match = ''
    prefix_to_use = None
    
    for prefix, namespace in prefixes.items():
        if uri.startswith(namespace) and len(namespace) > len(longest_match):
            longest_match = namespace
            prefix_to_use = prefix
    
    if prefix_to_use:
        return f"{prefix_to_use}:{uri[len(longest_match):]}"
    
    return f"<{uri}>"  # 短縮できない場合は完全なURIを<>で囲む

def process_max_count(value):
    """最大出現回数を適切に処理する関数"""
    if pd.isna(value) or str(value).upper() == 'N':
        return None
    try:
        float_val = float(value)
        if np.isnan(float_val):
            return None
        return int(float_val)
    except (ValueError, TypeError):
        return None

def is_valid_property(row):
    """プロパティが有効かどうかをチェックする関数"""
    if pd.isna(row["URI"]) or pd.isna(row["クラス"]) or pd.isna(row["値域"]):
        return False
    max_count = process_max_count(row["最大出現回数"])
    if max_count is None and str(row["最大出現回数"]).upper() != 'N':
        return False
    return True



# プレフィックス定義
prefixes = {
    'sh': 'http://www.w3.org/ns/shacl#',
    'dcat': 'http://www.w3.org/ns/dcat#',
    'dcterms': 'http://purl.org/dc/terms/',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'foaf': 'http://xmlns.com/foaf/0.1/',
    'ex': 'http://example.org/shapes/',
    'ma': 'https://mediaarts-db.artmuseums.go.jp/data/property/',
    'class': 'https://mediaarts-db.artmuseums.go.jp/data/class/',
    'schema': 'https://schema.org/',
    'skos': 'http://schema.org/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'rcgs': 'https://collection.rcgs.jp/terms/',
    'dcndl': 'http://ndl.go.jp/dcndl/terms/',
    'owl': 'http://www.w3.org/2002/07/owl#',
}

# 入力・出力ファイルのパス
excel_file = "rcgs_metadataschema.xlsx"
output_ttl = "rcgs_shacl_schema.ttl"

# エクセルデータを読み込む
df = pd.read_excel(excel_file, dtype=str, header=0)

# カラム名の整形
df.columns = df.columns.str.strip().str.replace("\ufeff", "")

# 最小出現回数の処理
df["最小出現回数"] = pd.to_numeric(df["最小出現回数"], errors="coerce").fillna(0).astype(int)

# SHACL の Turtle ヘッダー
ttl_template = "\n".join([f"@prefix {prefix}: <{uri}> ." for prefix, uri in prefixes.items()]) + "\n"

# クラスごとの SHACL Shape を格納する辞書
shapes = {}

# 各行を SHACL 形式に変換
for _, row in df.iterrows():
    if not is_valid_property(row):
        continue
    
    label = row["ラベル"]
    uri = row["URI"]
    min_count = row["最小出現回数"]
    max_count = process_max_count(row["最大出現回数"])
    target_class = row["クラス"]
    value_range = row["値域"]
    comment = row["コメント"]

    # URIを短縮形に変換
    shortened_uri = shorten_uri(uri, prefixes)

    # SHACL Shape の識別子
    shape_name = target_class.split(":")[-1] + "Shape"
    shape_uri = f"ex:{shape_name}"

    # クラスごとの SHACL ノードを作成
    if shape_uri not in shapes:
        shapes[shape_uri] = f"{shape_uri}\n    a sh:NodeShape ;\n    sh:targetClass {target_class} ;\n"

    # sh:datatype または sh:class の決定
    if value_range.startswith("xsd:"):
        range_statement = f"        sh:datatype {value_range} ;"
    elif value_range.startswith("\""):
        range_statement = f"        sh:in ({value_range}) ;"
    else:
        range_statement = f"        sh:class {value_range} ;"

    # コメントの追加
    comment_statement = f'        sh:description "{comment}"@ja ;' if comment and pd.notna(comment) else ""
    
    # プロパティ名の追加（メタデータスキーマとして）
    name_statement = f'        sh:name "{label}"@ja ;' if label and pd.notna(label) else ""

    # プロパティ制約を追加
    max_count_statement = f"        sh:maxCount {max_count} ;" if max_count is not None else ""
    
    # プロパティシェイプの各行を動的に構築
    property_lines = [
        "    sh:property [",
        f"        sh:path {shortened_uri} ;"
    ]
    
    if name_statement:
        property_lines.append(name_statement)
    
    property_lines.append(f"        sh:minCount {min_count} ;")
    
    if max_count_statement:
        property_lines.append(max_count_statement)
    
    if range_statement:
        property_lines.append(range_statement)
    
    if comment_statement:
        property_lines.append(comment_statement)
    
    property_lines.append("    ] ;")
    
    property_shape = "\n".join(property_lines) + "\n"
    shapes[shape_uri] += property_shape

# 生成した SHACL スキーマを出力
with open(output_ttl, "w", encoding="utf-8") as f:
    f.write(ttl_template)
    for shape in shapes.values():
        f.write(shape.rstrip(";") + ".\n\n")

print(f"✅ SHACL スキーマを {output_ttl} に出力しました。")
print()
print("📋 生成された SHACL スキーマの特徴:")
print("  • sh:name による日本語プロパティ名の追加")
print("  • sh:description によるコメント情報")
print("  • 完全なプレフィックス定義")
print("  • メタデータスキーマとして必要な情報を包含")
print()
print("🔍 バリデーションを実行するには:")
print("  sh_validation_rcgscol.py を使用してください。")