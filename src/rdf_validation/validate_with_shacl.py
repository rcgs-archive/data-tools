#!/usr/bin/env python3
"""
RDF/XMLファイルをSHACLスキーマでバリデーションするスクリプト
"""

import sys
from pathlib import Path
from typing import List, Tuple, Optional, Dict, Any

try:
    import pyshacl
    from rdflib import Graph
    from rdflib.exceptions import ParserError
except ImportError:
    print("エラー: 必要なライブラリがインストールされていません")
    print("インストール方法: pip install pyshacl rdflib")
    sys.exit(1)


def format_file_size(size_bytes: int) -> str:
    """ファイルサイズを読みやすい形式に変換"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def validate_with_shacl(
    data_file: Path,
    shacl_file: Path,
    data_format: str = 'xml',
    shacl_format: str = 'turtle'
) -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
    """
    SHACLスキーマを使用してRDFデータをバリデーション
    
    Args:
        data_file: バリデーション対象のRDFファイル
        shacl_file: SHACLスキーマファイル
        data_format: データファイルの形式（'xml', 'turtle', 'n3'など）
        shacl_format: SHACLファイルの形式（'turtle', 'xml'など）
    
    Returns:
        (is_valid, error_message, validation_report)
    """
    try:
        # SHACLバリデーションを実行
        conforms, results_graph, results_text = pyshacl.validate(
            str(data_file),
            shacl_graph=str(shacl_file),
            data_graph_format=data_format,
            shacl_graph_format=shacl_format,
            inference='rdfs',  # RDFS推論を有効化
            abort_on_first=False,  # すべてのエラーを収集
            allow_infos=True,  # 情報メッセージも含める
            allow_warnings=True,  # 警告も含める
            meta_shacl=False,  # SHACLのメタバリデーションは無効
            advanced=False,  # 高度な機能は無効
            js=False,  # JavaScriptは無効
            debug=False
        )
        
        # バリデーション結果を解析
        validation_report = {
            'conforms': conforms,
            'results_text': results_text,
            'results_graph': results_graph
        }
        
        return conforms, None, validation_report
        
    except Exception as e:
        return False, f"バリデーションエラー: {e}", None


def parse_validation_results(results_graph: Graph) -> List[Dict[str, Any]]:
    """
    バリデーション結果グラフからエラーと警告を抽出
    
    Returns:
        エラー/警告のリスト
    """
    issues = []
    
    try:
        # SHACL名前空間
        SH = "http://www.w3.org/ns/shacl#"
        
        # バリデーション結果をクエリ
        query = """
        PREFIX sh: <http://www.w3.org/ns/shacl#>
        SELECT ?focusNode ?resultPath ?resultSeverity ?resultMessage ?sourceShape
        WHERE {
            ?report a sh:ValidationReport .
            ?report sh:result ?result .
            ?result sh:focusNode ?focusNode .
            OPTIONAL { ?result sh:resultPath ?resultPath . }
            OPTIONAL { ?result sh:resultSeverity ?resultSeverity . }
            OPTIONAL { ?result sh:resultMessage ?resultMessage . }
            OPTIONAL { ?result sh:sourceShape ?sourceShape . }
        }
        """
        
        for row in results_graph.query(query):
            issue = {
                'focus_node': str(row.focusNode) if row.focusNode else None,
                'path': str(row.resultPath) if row.resultPath else None,
                'severity': str(row.resultSeverity) if row.resultSeverity else None,
                'message': str(row.resultMessage) if row.resultMessage else None,
                'source_shape': str(row.sourceShape) if row.sourceShape else None
            }
            issues.append(issue)
            
    except Exception as e:
        # パースに失敗した場合は、テキスト結果を返す
        pass
    
    return issues


def format_validation_issue(issue: Dict[str, Any]) -> str:
    """バリデーション問題を読みやすい形式にフォーマット"""
    parts = []
    
    if issue.get('severity'):
        severity = issue['severity']
        if 'Violation' in severity:
            parts.append("❌ 違反")
        elif 'Warning' in severity:
            parts.append("⚠ 警告")
        else:
            parts.append("ℹ 情報")
    
    if issue.get('path'):
        parts.append(f"プロパティ: {issue['path']}")
    
    if issue.get('message'):
        parts.append(f"メッセージ: {issue['message']}")
    
    if issue.get('focus_node'):
        parts.append(f"対象ノード: {issue['focus_node']}")
    
    if issue.get('source_shape'):
        parts.append(f"シェイプ: {issue['source_shape']}")
    
    return " | ".join(parts) if parts else "詳細情報なし"


def main():
    # パス設定
    script_dir = Path(__file__).parent
    data_dir = script_dir / "converted_rdf"
    shacl_file = Path(__file__).parent.parent / "data-tools" / "src" / "shacl_and_validation" / "rcgs_shacl_schema.ttl"
    
    # ファイルの存在確認
    if not data_dir.exists():
        print(f"エラー: データディレクトリが見つかりません: {data_dir}")
        sys.exit(1)
    
    if not shacl_file.exists():
        print(f"エラー: SHACLスキーマファイルが見つかりません: {shacl_file}")
        sys.exit(1)
    
    # XMLファイルを検索
    xml_files = sorted(data_dir.glob("*.xml"))
    
    if not xml_files:
        print(f"警告: {data_dir} にXMLファイルが見つかりませんでした")
        sys.exit(0)
    
    print("=" * 80)
    print("SHACL バリデーション")
    print("=" * 80)
    print(f"データディレクトリ: {data_dir}")
    print(f"SHACLスキーマ: {shacl_file}")
    print(f"見つかったファイル: {len(xml_files)} 件")
    print("-" * 80)
    
    results = []
    total_files = len(xml_files)
    valid_count = 0
    invalid_count = 0
    total_violations = 0
    total_warnings = 0
    
    for i, xml_file in enumerate(xml_files, 1):
        file_size = xml_file.stat().st_size
        print(f"\n[{i}/{total_files}] {xml_file.name} ({format_file_size(file_size)})")
        print("-" * 80)
        
        # SHACLバリデーション実行
        is_valid, error, report = validate_with_shacl(
            xml_file,
            shacl_file,
            data_format='xml',
            shacl_format='turtle'
        )
        
        if error:
            print(f"❌ エラー: {error}")
            results.append((xml_file.name, False, error, None, None))
            invalid_count += 1
            continue
        
        if report:
            # バリデーション結果を解析
            issues = parse_validation_results(report['results_graph'])
            
            # 違反と警告を分類
            violations = [i for i in issues if i.get('severity') and 'Violation' in i['severity']]
            warnings = [i for i in issues if i.get('severity') and 'Warning' in i['severity']]
            
            violation_count = len(violations)
            warning_count = len(warnings)
            
            total_violations += violation_count
            total_warnings += warning_count
            
            if is_valid and violation_count == 0:
                print(f"✓ バリデーション成功")
                if warning_count > 0:
                    print(f"  ⚠ 警告: {warning_count} 件")
                valid_count += 1
            else:
                print(f"❌ バリデーション失敗")
                print(f"  違反: {violation_count} 件")
                if warning_count > 0:
                    print(f"  警告: {warning_count} 件")
                invalid_count += 1
                
                # 違反の詳細を表示（最初の10件まで）
                if violations:
                    print("\n  違反の詳細:")
                    for j, violation in enumerate(violations[:10], 1):
                        print(f"    {j}. {format_validation_issue(violation)}")
                    if len(violations) > 10:
                        print(f"    ... 他 {len(violations) - 10} 件の違反")
                
                # 警告の詳細を表示（最初の5件まで）
                if warnings and len(warnings) <= 5:
                    print("\n  警告の詳細:")
                    for j, warning in enumerate(warnings[:5], 1):
                        print(f"    {j}. {format_validation_issue(warning)}")
            
            results.append((xml_file.name, is_valid, None, violation_count, warning_count))
        else:
            print(f"❌ バリデーション結果が取得できませんでした")
            results.append((xml_file.name, False, "結果が取得できませんでした", None, None))
            invalid_count += 1
    
    # サマリー
    print("\n" + "=" * 80)
    print("バリデーション結果サマリー")
    print("=" * 80)
    print(f"総ファイル数: {total_files}")
    print(f"✓ 有効: {valid_count} 件")
    print(f"❌ 無効: {invalid_count} 件")
    print(f"総違反数: {total_violations} 件")
    print(f"総警告数: {total_warnings} 件")
    
    if invalid_count > 0:
        print("\n違反が検出されたファイル:")
        for filename, is_valid, error, violations, warnings in results:
            if not is_valid or (violations and violations > 0):
                status = "❌" if not is_valid or violations > 0 else "⚠"
                violation_str = f"違反: {violations}件" if violations else ""
                warning_str = f"警告: {warnings}件" if warnings else ""
                error_str = f"エラー: {error}" if error else ""
                details = " | ".join(filter(None, [violation_str, warning_str, error_str]))
                print(f"  {status} {filename}: {details}")
    
    # 終了コード
    sys.exit(0 if invalid_count == 0 and total_violations == 0 else 1)


if __name__ == "__main__":
    main()
