from rdflib import Graph, Namespace, URIRef
from pyshacl import validate
import pandas as pd
import re

def load_property_names(excel_file):
    """DSPver139.xlsxからプロパティ名と日本語名のマッピングを作成"""
    df = pd.read_excel(excel_file, sheet_name='dsp', header=None)
    
    # 13行目以降がプロパティ情報
    property_data = df.iloc[13:].copy()
    property_data.columns = ['項目規則名', 'プロパティ', '最小', '最大', '値タイプ', '値制約', 'コメント']
    
    # 空行や不正な行を除外
    property_data = property_data.dropna(subset=['項目規則名', 'プロパティ'])
    property_data = property_data[~property_data['項目規則名'].str.startswith('[', na=False)]
    
    # プロパティURIと日本語名のマッピングを作成
    property_names = {}
    for _, row in property_data.iterrows():
        japanese_name = row['項目規則名']
        property_uri = row['プロパティ']
        if pd.notna(japanese_name) and pd.notna(property_uri):
            property_names[property_uri] = japanese_name
    
    return property_names

def extract_property_from_shacl(results_text, property_names):
    """SHACLバリデーション結果からプロパティを抽出し、日本語名に変換"""
    lines = results_text.split('\n')
    enhanced_results = []
    
    for line in lines:
        # プロパティパスを含む行を検出
        if 'sh:resultPath' in line or 'Property Shape' in line:
            # URIを抽出
            uri_match = re.search(r'<([^>]+)>', line)
            if uri_match:
                uri = uri_match.group(1)
                # 短縮形のURIを展開
                for prefix, full_uri in [
                    ('rcgs:', 'https://collection.rcgs.jp/terms/'),
                    ('dcterms:', 'http://purl.org/dc/terms/'),
                    ('rdf:', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
                    ('rdfs:', 'http://www.w3.org/2000/01/rdf-schema#'),
                    ('foaf:', 'http://xmlns.com/foaf/0.1/'),
                    ('schema:', 'https://schema.org/'),
                ]:
                    if prefix in line:
                        property_key = line.split(prefix)[1].split()[0].rstrip('>;,')
                        full_property_uri = f"{prefix}{property_key}"
                        if full_property_uri in property_names:
                            japanese_name = property_names[full_property_uri]
                            line += f" → 【{japanese_name}】"
                        break
                
                # 完全URIの場合の処理
                for prop_uri, japanese_name in property_names.items():
                    if ':' in prop_uri and prop_uri.split(':')[1] in uri:
                        line += f" → 【{japanese_name}】"
                        break
        
        enhanced_results.append(line)
    
    return '\n'.join(enhanced_results)

# プロパティ名のマッピングを読み込み
try:
    property_names = load_property_names("DSPver139.xlsx")
    print(f"プロパティ名マッピングを読み込みました: {len(property_names)}件")
    print("サンプルマッピング:")
    for i, (prop, name) in enumerate(list(property_names.items())[:5]):
        print(f"  {prop} → {name}")
    print()
except Exception as e:
    print(f"プロパティ名の読み込みでエラー: {e}")
    property_names = {}

# RDF/XML データセットを読み込む
print("RDFデータを読み込み中...")
data_graph = Graph()
data_graph.parse("all.xml/Package_20230207.xml", format="xml")
print(f"データグラフ: {len(data_graph)} トリプル")

# SHACL スキーマ（Turtle形式）を読み込む
print("SHACLスキーマを読み込み中...")
shacl_graph = Graph()
shacl_graph.parse("rcgs_shacl_schema.ttl", format="turtle")
print(f"SHACLグラフ: {len(shacl_graph)} トリプル")

# SHACL バリデーション実行
print("SHACLバリデーションを実行中...")
conforms, results_graph, results_text = validate(
    data_graph, 
    shacl_graph=shacl_graph, 
    inference="rdfs",  # RDFS 推論を有効化（必要に応じて）
    debug=False
)

# 結果出力
print("=" * 60)
print("バリデーション結果:", "✅ 成功" if conforms else "❌ 失敗")
print("=" * 60)

if not conforms:
    # 日本語名を追加した結果を出力
    enhanced_results = extract_property_from_shacl(results_text, property_names)
    print(enhanced_results)
else:
    print("全てのデータがSHACLスキーマに適合しています。")
