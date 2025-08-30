#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SHACL Schema to Markdown Table Converter

このスクリプトはSHACLスキーマファイル(TTL)を読み込み、
クラスごとのプロパティテーブルをMarkdown形式で出力します。
"""

import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path


def parse_shacl_ttl(file_path: str) -> Dict[str, List[Dict[str, str]]]:
    """
    SHACLスキーマファイルを解析してクラスごとのプロパティ情報を抽出
    
    Returns:
        Dict[class_name, List[property_info]]
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # プレフィックス定義を抽出
    prefixes = {}
    prefix_pattern = r'@prefix\s+([^:]+):\s+<([^>]+)>\s+\.'
    for match in re.finditer(prefix_pattern, content):
        prefixes[match.group(1)] = match.group(2)
    
    # NodeShapeブロックを抽出
    shapes = {}
    
    # ex:ClassNameShape ... . のパターンでNodeShapeを抽出
    shape_pattern = r'(ex:\w+Shape)\s+a\s+sh:NodeShape\s*;(.*?)(?=ex:\w+Shape\s+a\s+sh:NodeShape|$)'
    
    for match in re.finditer(shape_pattern, content, re.DOTALL):
        shape_name = match.group(1)
        shape_content = match.group(2)
        
        # クラス名を抽出 (ex:WorkShape -> Work)
        class_name = shape_name.replace('ex:', '').replace('Shape', '')
        
        # sh:targetClassを抽出
        target_class_match = re.search(r'sh:targetClass\s+([^;]+)\s*;', shape_content)
        target_class = target_class_match.group(1).strip() if target_class_match else class_name
        
        # プロパティを抽出
        properties = parse_properties(shape_content, prefixes)
        
        shapes[class_name] = {
            'target_class': target_class,
            'properties': properties
        }
    
    return shapes


def parse_properties(shape_content: str, prefixes: Dict[str, str]) -> List[Dict[str, str]]:
    """
    NodeShapeのコンテンツからプロパティ情報を抽出
    """
    properties = []
    
    # sh:property [ ... ] ; のパターンでプロパティブロックを抽出
    property_pattern = r'sh:property\s*\[(.*?)\]\s*;'
    
    for match in re.finditer(property_pattern, shape_content, re.DOTALL):
        prop_content = match.group(1)
        prop_info = parse_single_property(prop_content, prefixes)
        if prop_info:
            properties.append(prop_info)
    
    return properties


def parse_single_property(prop_content: str, prefixes: Dict[str, str]) -> Optional[Dict[str, str]]:
    """
    単一のプロパティブロックから情報を抽出
    """
    prop_info = {}
    
    # sh:path を抽出
    path_match = re.search(r'sh:path\s+([^;]+)\s*;', prop_content)
    if path_match:
        prop_info['path'] = path_match.group(1).strip()
    else:
        return None
    
    # sh:name を抽出
    name_match = re.search(r'sh:name\s+"([^"]+)"@ja\s*;', prop_content)
    if name_match:
        prop_info['name'] = name_match.group(1)
    
    # sh:minCount を抽出
    min_count_match = re.search(r'sh:minCount\s+(\d+)\s*;', prop_content)
    if min_count_match:
        prop_info['min_count'] = min_count_match.group(1)
    
    # sh:maxCount を抽出
    max_count_match = re.search(r'sh:maxCount\s+(\d+)\s*;', prop_content)
    if max_count_match:
        prop_info['max_count'] = max_count_match.group(1)
    
    # データタイプ/クラス/値制約を抽出
    datatype_match = re.search(r'sh:datatype\s+([^;]+)\s*;', prop_content)
    class_match = re.search(r'sh:class\s+([^;]+)\s*;', prop_content)
    in_match = re.search(r'sh:in\s+\(([^)]+)\)\s*;', prop_content)
    
    if datatype_match:
        prop_info['value_type'] = datatype_match.group(1).strip()
    elif class_match:
        prop_info['value_type'] = class_match.group(1).strip()
    elif in_match:
        # sh:inの値リストを処理
        values = [v.strip(' "') for v in in_match.group(1).split()]
        prop_info['value_type'] = 'enumeration'
        prop_info['value_constraint'] = ' | '.join(values[:3]) + ('...' if len(values) > 3 else '')
    
    # sh:description を抽出
    desc_match = re.search(r'sh:description\s+"([^"]+)"@ja\s*;', prop_content)
    if desc_match:
        prop_info['description'] = desc_match.group(1)
    
    return prop_info


def format_value_type(value_type: str) -> str:
    """
    値タイプを日本語で表示用にフォーマット
    """
    type_mapping = {
        'xsd:string': '文字列',
        'xsd:integer': '整数',
        'xsd:float': '実数',
        'xsd:boolean': '真偽値',
        'xsd:date': '日付',
        'xsd:dateTime': '日時',
        'enumeration': '選択値'
    }
    
    # プレフィックスを除去
    if ':' in value_type:
        short_type = value_type.split(':')[-1]
        if value_type in type_mapping:
            return type_mapping[value_type]
        elif short_type.startswith('http'):
            return '参照値'
        else:
            return '構造化'
    
    return value_type


def generate_markdown(shapes: Dict[str, Dict]) -> str:
    """
    抽出したスキーマ情報からMarkdownテーブルを生成
    """
    md_content = []
    
    # ヘッダー
    md_content.append("# RCGS メタデータスキーマ仕様書")
    md_content.append("")
    md_content.append("このドキュメントは SHACL スキーマから自動生成されています。")
    md_content.append("")
    
    # 目次
    md_content.append("## 目次")
    md_content.append("")
    for class_name in sorted(shapes.keys()):
        md_content.append(f"- [{class_name}](#{class_name.lower()})")
    md_content.append("")
    
    # 各クラスのテーブル
    for class_name in sorted(shapes.keys()):
        shape_info = shapes[class_name]
        properties = shape_info['properties']
        target_class = shape_info['target_class']
        
        md_content.append(f"## {class_name}")
        md_content.append("")
        md_content.append(f"**対象クラス:** `{target_class}`")
        md_content.append("")
        
        if not properties:
            md_content.append("このクラスには定義されたプロパティがありません。")
            md_content.append("")
            continue
        
        # テーブルヘッダー
        md_content.append("| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |")
        md_content.append("|--------|------------|------|------|----------|--------|----------|")
        
        # プロパティ行
        for prop in properties:
            name = prop.get('name', '')
            path = prop.get('path', '')
            min_count = prop.get('min_count', '0')
            max_count = prop.get('max_count', '-')
            value_type = format_value_type(prop.get('value_type', ''))
            value_constraint = prop.get('value_constraint', '')
            description = prop.get('description', '')
            
            # セル内容をエスケープ
            def escape_cell(text):
                return text.replace('|', '\\|').replace('\n', ' ')
            
            md_content.append(f"| {escape_cell(name)} | {escape_cell(path)} | {min_count} | {max_count} | {escape_cell(value_type)} | {escape_cell(value_constraint)} | {escape_cell(description)} |")
        
        md_content.append("")
    
    return '\n'.join(md_content)


def main():
    """
    メイン処理
    """
    # 入力ファイルと出力ファイルのパス
    input_file = "/Users/fukudakazufumi/Library/CloudStorage/OneDrive-学校法人立命館/Codes/rcgs_archive/src/shacl_and_validation/rcgs_shacl_schema.ttl"
    output_file = "/Users/fukudakazufumi/Library/CloudStorage/OneDrive-学校法人立命館/Codes/rcgs_archive/src/shacl_and_validation/rcgs_schema_specification.md"
    
    try:
        print("SHACLスキーマファイルを解析中...")
        shapes = parse_shacl_ttl(input_file)
        
        print(f"解析完了: {len(shapes)}個のクラスが見つかりました")
        for class_name, info in shapes.items():
            print(f"  - {class_name}: {len(info['properties'])}個のプロパティ")
        
        print("Markdownファイルを生成中...")
        markdown_content = generate_markdown(shapes)
        
        # ファイルに出力
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"完了: {output_file} に出力しました")
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        raise


if __name__ == "__main__":
    main()
