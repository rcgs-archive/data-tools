---
layout: default
title: メタデータスキーマ
permalink: /schema/
---

# メタデータスキーマ

RCGSアーカイブプロジェクトで使用するメタデータスキーマの仕様とドキュメントです。

## SHACL スキーマ

### [RCGS メタデータスキーマ仕様書](rcgs_schema_specification)
メタデータスキーマの完全な仕様書です。全19クラスのプロパティ定義を含みます。

- **Work**: ゲーム作品の基本情報
- **Variation**: 作品のバリエーション（版や移植版）
- **Package**: 物理的・デジタル的なパッケージ
- **Item**: 個別の資料・コレクション
- **Agent**: 個人・組織情報
- **Platform**: ゲームプラットフォーム
- その他13クラス

### 主要な特徴

1. **階層構造**: Work → Variation → Package → Item の4層構造
2. **SHACL準拠**: W3C標準のSHACL (Shapes Constraint Language) 形式
3. **多言語対応**: 日本語と英語のプロパティ名
4. **RDF互換**: Linked Dataとしての利用が可能

## DSP仕様

Digital Scholarship Platform (DSP) の基本仕様に基づいたメタデータ定義です。

## スキーマファイル

- `rcgs_shacl_schema.ttl`: SHACL形式のスキーマファイル
- `rcgs_metadataschema.xlsx`: Excel形式の元スキーマ定義
- `DSPver139.xlsx`: DSP仕様書

## 更新履歴

- 2024-12: 初期バージョンを公開
- 全19クラス、400+プロパティを定義
