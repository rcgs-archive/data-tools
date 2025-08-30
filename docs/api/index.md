---
layout: default
title: API・データ形式
permalink: /api/
---

# API・データ形式

RCGSアーカイブのデータアクセス方法とデータ形式について説明します。

## データ形式

### RDF/Turtle (TTL)
メタデータの主要な保存・交換形式です。

**特徴:**
- W3C標準のRDF形式
- SHACL準拠の構造化データ
- Linked Dataとして利用可能
- SPARQL クエリ対応

**例:**
```turtle
@prefix rcgs: <https://collection.rcgs.jp/terms/> .
@prefix dcterms: <http://purl.org/dc/terms/> .

rcgs:work001 a rcgs:Work ;
    dcterms:title "ドラゴンクエスト"@ja ;
    rcgs:recordID "W001" ;
    dcterms:creator rcgs:agent001 .
```

### JSON-LD
Web API向けのJSON形式データです。

### Excel
人間が読み書きしやすい表形式データです。

## SPARQL エンドポイント

### クエリ例

**すべての作品を取得:**
```sparql
PREFIX rcgs: <https://collection.rcgs.jp/terms/>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?work ?title WHERE {
    ?work a rcgs:Work ;
          dcterms:title ?title .
}
```

**特定のプラットフォームの作品を検索:**
```sparql
PREFIX rcgs: <https://collection.rcgs.jp/terms/>
PREFIX schema: <https://schema.org/>

SELECT ?work ?title ?platform WHERE {
    ?work a rcgs:Work ;
          dcterms:title ?title ;
          schema:gamePlatform ?platform .
    FILTER(CONTAINS(LCASE(STR(?platform)), "nintendo"))
}
```

## バリデーション

### SHACL検証
提供されるSHACLスキーマを使用してデータの妥当性を検証できます。

```python
from pyshacl import validate

# データとスキーマの検証
conforms, graph, text = validate(
    data_graph="your_data.ttl",
    shacl_graph="rcgs_shacl_schema.ttl"
)
```

## ダウンロード

### スキーマファイル
- [SHACL スキーマ](../src/shacl_and_validation/rcgs_shacl_schema.ttl)
- [DSP Excel仕様](../src/shacl_and_validation/DSPver139.xlsx)

### サンプルデータ
- RDF/XMLサンプル
- TTLサンプル
- JSON-LDサンプル

## 技術仕様

### 名前空間
- `rcgs:` - https://collection.rcgs.jp/terms/
- `dcterms:` - http://purl.org/dc/terms/
- `schema:` - https://schema.org/
- `foaf:` - http://xmlns.com/foaf/0.1/

### エンコーディング
- 文字エンコーディング: UTF-8
- ファイル形式: TTL, RDF/XML, JSON-LD
- 圧縮: gzip対応
