---
layout: default
title: ツール・スクリプト
permalink: /tools/
---

# ツール・スクリプト

RCGSアーカイブプロジェクトで開発したデータ変換・処理ツールです。

## SHACL関連ツール

### DSP to SHACL 変換ツール
**ファイル**: `src/shacl_and_validation/dsp_convert_to_shacl.py`

Excel形式のDSP仕様書からSHACLスキーマ（TTL形式）を生成します。

**機能:**
- DSP Excel→SHACL TTL変換
- 日本語プロパティ名の自動付与
- 制約条件の適切な変換
- プレフィックス管理

**使用方法:**
```bash
cd src/shacl_and_validation
python dsp_convert_to_shacl.py
```

### SHACL to Markdown 変換ツール
**ファイル**: `src/shacl_and_validation/shacl_to_markdown.py`

SHACL TTLファイルからMarkdown形式の仕様書を生成します。

**機能:**
- SHACLスキーマの自動解析
- クラスごとのテーブル生成
- 目次付きドキュメント生成
- Jekyll Front Matter対応

**使用方法:**
```bash
cd src/shacl_and_validation
python shacl_to_markdown.py
```

## データ変換ツール

### メタデータ変換
- Excel→RDF変換
- XML→TTL変換
- バリデーション機能

### 画像処理
- サムネイル生成
- メタデータ抽出

## 開発・保守

### 依存関係
- Python 3.8+
- pandas (Excel処理)
- rdflib (RDF処理)
- pyshacl (SHACL検証)

### 環境構築
```bash
pip install pandas rdflib pyshacl openpyxl
```

## ソースコード

すべてのツールは[GitHubリポジトリ](https://github.com/fukudakz/rcgs_archive)で公開されています。
