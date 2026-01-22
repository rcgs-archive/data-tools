#!/usr/bin/env python3
"""
RDF/XMLファイルのバリデーションスクリプト
RDFLibを使用してRDF/XMLファイルの構文と整合性をチェックします
"""

import sys
from pathlib import Path
from typing import List, Tuple, Optional
import xml.etree.ElementTree as ET

try:
    from rdflib import Graph, URIRef
    from rdflib.exceptions import ParserError
except ImportError:
    print("エラー: RDFLibがインストールされていません")
    print("インストール方法: pip install rdflib")
    sys.exit(1)


def validate_xml_syntax(file_path: Path) -> Tuple[bool, Optional[str]]:
    """
    XMLの基本的な構文チェック
    
    Returns:
        (is_valid, error_message)
    """
    try:
        # XMLの構文チェック（大きなファイルでもメモリ効率的に）
        parser = ET.XMLParser()
        for event, elem in ET.iterparse(file_path, events=('start', 'end'), parser=parser):
            if event == 'end':
                elem.clear()  # メモリを解放
        return True, None
    except ET.ParseError as e:
        return False, f"XML構文エラー: {e}"
    except Exception as e:
        return False, f"XML読み込みエラー: {e}"


def validate_rdf_xml(file_path: Path) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    RDF/XMLファイルのバリデーション
    
    Returns:
        (is_valid, error_message, triple_count)
    """
    try:
        # RDFグラフを作成
        g = Graph()
        
        # RDF/XMLファイルをパース
        g.parse(str(file_path), format='xml')
        
        # トリプル数を取得
        triple_count = len(g)
        
        return True, None, triple_count
        
    except ParserError as e:
        return False, f"RDFパースエラー: {e}", None
    except Exception as e:
        return False, f"RDF読み込みエラー: {e}", None


def validate_rdf_structure(file_path: Path) -> Tuple[bool, List[str]]:
    """
    RDF/XMLの構造的なチェック（名前空間、基本的な要素など）
    
    Returns:
        (is_valid, warnings)
    """
    warnings = []
    
    try:
        # XMLをパース
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # RDF要素の確認
        if root.tag != '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF':
            warnings.append(f"ルート要素がRDFではありません: {root.tag}")
        
        # 名前空間の確認
        namespaces = root.attrib
        if 'xmlns:rdf' not in namespaces:
            warnings.append("rdf名前空間が定義されていません")
        
        # 子要素の確認
        if len(root) == 0:
            warnings.append("RDF要素に子要素がありません")
        
        return len(warnings) == 0, warnings
        
    except Exception as e:
        return False, [f"構造チェックエラー: {e}"]


def format_file_size(size_bytes: int) -> str:
    """ファイルサイズを読みやすい形式に変換"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def main():
    # 入力ディレクトリ
    input_dir = Path(__file__).parent / "converted_rdf"
    
    if not input_dir.exists():
        print(f"エラー: ディレクトリが見つかりません: {input_dir}")
        sys.exit(1)
    
    # XMLファイルを検索
    xml_files = sorted(input_dir.glob("*.xml"))
    
    if not xml_files:
        print(f"警告: {input_dir} にXMLファイルが見つかりませんでした")
        sys.exit(0)
    
    print("=" * 80)
    print("RDF/XML バリデーション")
    print("=" * 80)
    print(f"対象ディレクトリ: {input_dir}")
    print(f"見つかったファイル: {len(xml_files)} 件")
    print("-" * 80)
    
    results = []
    total_files = len(xml_files)
    valid_count = 0
    invalid_count = 0
    
    for i, xml_file in enumerate(xml_files, 1):
        file_size = xml_file.stat().st_size
        print(f"\n[{i}/{total_files}] {xml_file.name} ({format_file_size(file_size)})")
        print("-" * 80)
        
        # 1. XML構文チェック
        xml_valid, xml_error = validate_xml_syntax(xml_file)
        if not xml_valid:
            print(f"❌ XML構文エラー: {xml_error}")
            results.append((xml_file.name, False, xml_error, None))
            invalid_count += 1
            continue
        print("✓ XML構文: OK")
        
        # 2. RDF構造チェック
        structure_valid, structure_warnings = validate_rdf_structure(xml_file)
        if structure_warnings:
            for warning in structure_warnings:
                print(f"⚠ 警告: {warning}")
        if structure_valid:
            print("✓ RDF構造: OK")
        
        # 3. RDF/XMLパースチェック
        rdf_valid, rdf_error, triple_count = validate_rdf_xml(xml_file)
        if not rdf_valid:
            print(f"❌ RDFパースエラー: {rdf_error}")
            results.append((xml_file.name, False, rdf_error, None))
            invalid_count += 1
            continue
        
        print(f"✓ RDFパース: OK (トリプル数: {triple_count:,})")
        results.append((xml_file.name, True, None, triple_count))
        valid_count += 1
    
    # サマリー
    print("\n" + "=" * 80)
    print("バリデーション結果サマリー")
    print("=" * 80)
    print(f"総ファイル数: {total_files}")
    print(f"✓ 有効: {valid_count} 件")
    print(f"❌ 無効: {invalid_count} 件")
    
    if invalid_count > 0:
        print("\nエラーが発生したファイル:")
        for filename, is_valid, error, _ in results:
            if not is_valid:
                print(f"  - {filename}: {error}")
    
    # トリプル数の統計
    valid_results = [r for r in results if r[1] and r[3] is not None]
    if valid_results:
        total_triples = sum(r[3] for r in valid_results)
        print(f"\n総トリプル数: {total_triples:,}")
        print("\nファイル別トリプル数:")
        for filename, _, _, triple_count in sorted(valid_results, key=lambda x: x[3] or 0, reverse=True):
            print(f"  - {filename}: {triple_count:,} トリプル")
    
    # 終了コード
    sys.exit(0 if invalid_count == 0 else 1)


if __name__ == "__main__":
    main()
