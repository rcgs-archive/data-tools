# RCGS メタデータスキーマ仕様書

このドキュメントは SHACL スキーマから自動生成されています。

## 目次

- [AdminMetadata](#adminmetadata)
- [Agent](#agent)
- [ContentRating](#contentrating)
- [Contribution](#contribution)
- [Device](#device)
- [Item](#item)
- [MediaFormat](#mediaformat)
- [MediaTypeOrExtent](#mediatypeorextent)
- [OnlinePackage](#onlinepackage)
- [Organization](#organization)
- [Package](#package)
- [Person](#person)
- [PhysicalPackage](#physicalpackage)
- [Platform](#platform)
- [ProvisionActivity](#provisionactivity)
- [RelatedInstance](#relatedinstance)
- [Topic](#topic)
- [Variation](#variation)
- [Work](#work)

## AdminMetadata

**対象クラス:** `rcgs:AdminMetadata`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| 出典 | dcterms:source | 0 | - | 文字列 |  | リソースを作成する上で参照した情報源 |
| 作成日 | dcterms:created | 0 | - | 構造化 |  | リソースが創造された日付 |
| 修正日 | dcterms:modified | 0 | - | 構造化 |  | リソースが修正された日付 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースについての説明 |

## Agent

**対象クラス:** `foaf:Agent`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| 種別 | rdf:type | 1 | 1 | 構造化 |  | リソースが属するサブクラス |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 名前 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他の名前 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| ウェブサイト | foaf:homepage | 0 | - | 文字列 |  | リソースのウェブサイト |
| 略歴 | dcterms:description | 0 | - | 文字列 |  | リソースの略歴 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部の典拠の識別子 |
| 国立国会図書館典拠ID | rcgs:ndlAuthoritiesID | 0 | - | 文字列 |  | リソースの国立国会図書館典拠ファイルによる識別子 |
| バーチャル国際典拠ファイルID | rcgs:viafID | 0 | - | 文字列 |  | リソースのバーチャル国際典拠ファイルによる識別子 |
| Wikidata ID | rcgs:wikidataID | 0 | - | 文字列 |  | リソースのWikidataによる識別子 |
| twitter ID | rcgs:twitterID | 0 | - | 文字列 |  | リソースのTwitterアカウントの識別子 |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 構造化 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| 言語 | dcterms:language | 0 | - | 構造化 |  | リソースが表現や記録に用いる言語 |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | リソースの他の属性で記録されない識別的特徴 |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## ContentRating

**対象クラス:** `rcgs:ContentRating`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 名称 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いる名称 |
| その他の名称 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いる名称 |
| 地理的範囲 | dcterms:spatial | 0 | - | 文字列 |  | リソースに関する場所 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースの識別子を示す外部のウェブサイト |
| Wikidata ID | rcgs:wikidataID | 0 | - | 文字列 |  | リソースのWikidataによる識別子 |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| 日付 | dcterms:date | 0 | - | 構造化 |  | リソースに関連する日付 |
| 発行地 | dcndl:location | 0 | - | 文字列 |  | リソースの発行に関連する場所 |
| 発行者 | dcterms:publisher | 0 | - | 構造化 |  | リソースを発行する主体 |
| 発行者名 | rcgs:publisherStatement | 0 | - | 文字列 |  | リソースを発行する主体の表示される名称 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースに関する説明 |
| ロゴ | schema:logo | 0 | - | 文字列 |  | リソースのロゴ |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## Contribution

**対象クラス:** `rcgs:Contribution`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| 主体 | rcgs:agent | 1 | 1 | 構造化 |  | 貢献者である主体 |
| 役割 | schema:roleName | 0 | - | 文字列 |  | 個人や組織が果たした役割 |
| 表示名 | rcgs:agentNameStatement | 0 | - | 文字列 |  | リソースの名前の表示や表記 |
| 演じたキャラクター名 | rcgs:actedCharacterName | 0 | - | 文字列 |  | 貢献者が演じたキャラクターの名前や名称 |
| キャラクター | rcgs:actedCharacter | 0 | - | 構造化 |  | 貢献者が演じたキャラクターの指定 |
| メンバーである主体 | rcgs:agentAffiliation | 0 | - | 構造化 |  | 貢献者がメンバーである主体 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースに関する説明 |

## Device

**対象クラス:** `rcgs:Device`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| サブタイプ | schema:additionalType | 0 | 1 | enumeration | rcgs:GameDevice", \| rcgs:PeripheralEquipment | リソースが所属するクラスにおけるサブタイプの指定 |
| 名称 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他の名称 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| エディション | dcndl:edition | 0 | - | 文字列 |  | リソースの版の識別のための指定 |
| 放送標準 | schema:videoFormat | 0 | - | 文字列 |  | リソースの実装に用いられるテレビ放送のシステム |
| 接続する装置 | rcgs:connects | 0 | - | 構造化 |  | リソースに接続するリソース |
| メディア形式 | schema:encodingFormat | 0 | - | 構造化 |  | リソースに実装するメディア形式 |
| 地理的範囲 | dcterms:spatial | 0 | - | 文字列 |  | リソースに関連する場所 |
| 素材 | schema:material | 0 | - | 文字列 |  | リソースを物理的に構成する素材 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| 型番 | rcgs:modelNumber | 0 | - | 文字列 |  | パッケージの供給者が定義する型番による識別子 |
| 商品ナンバー | schema:gtin13 | 0 | - | 文字列 |  | パッケージの主にバーコードで提供されるGTINによる識別子 |
| 頒布者 | rcgs:distributor | 0 | - | 構造化 |  | リソースを創作した主体 |
| 頒布日 | dcterms:issued | 0 | 1 | 構造化 |  | リソースを頒布した主体 |
| 頒布地 | dcndl:location | 0 | - | 文字列 |  | リソースの頒布に関連する場所 |
| 挿入されたパッケージ | rcgs:inserts | 0 | - | 構造化 |  | リソースに挿入されたパッケージ |
| 実装されたプラットフォーム | schema:gamePlatform | 0 | - | 構造化 |  | リソースに実装されたプラットフォーム |
| ブランド | schema:brand | 0 | - | 文字列 |  | リソースの創作や頒布の責任に関するブランド |
| 接続仕様 | rcgs:specConnection | 0 | - | 文字列 |  | リソースの機器接続に関する仕様 |
| 操作入力 | rcgs:controller | 0 | - | 文字列 |  | リソースのコントローラーの数量や入力端子などの仕様 |
| 大きさ | rcgs:dimension | 0 | - | 文字列 |  | リソースの大きさの測定値 |
| 重量 | schema:weight | 0 | 1 | 文字列 |  | リソースの重量の測定値 |
| 数量 | dcterms:extent | 0 | - | 文字列 |  | リソースを構成するユニットの数量 |
| サブユニットリスト | dcterms:tableOfContents | 0 | - | 文字列 |  | リソースを構成するサブユニットのリスト |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | リソースの他の属性で記録されない識別的特徴 |
| 映像出力の解像度 | schema:videoFrameSize | 0 | - | 文字列 |  | リソースの映像出力の解像度 |
| 音声出力 | schema:sound | 0 | - | 文字列 |  | リソースの音声出力 |
| 消費電力 | rcgs:powerConsumption | 0 | - | 文字列 |  | リソースの消費電力 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースに関する説明 |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## Item

**対象クラス:** `rcgs:Item`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 0 | - | 文字列 |  | 文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 管理者 | dcndl:holdlingAgent | 0 | 1 | 構造化 |  | リソースを合法的に補完する主体 |
| 所有者 | schema:owns | 0 | - | 構造化 |  | 合法的に所有する主体 |
| 例示されたパッケージ | rcgs:exemplarOf | 0 | 1 | 構造化 |  | 個別資料により例示されるリソース |
| 寄贈者 | rcgs:donor | 0 | - | 構造化 |  | リソースを寄贈した前の所有者である主体 |
| 売却者 | schema:seller | 0 | - | 構造化 |  | リソースを売却した前の所有者である主体 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じリソースを示す外部の典拠の識別子 |
| 保管場所 | dcterms:spatial | 0 | - | 文字列 |  | リソースに関連する場所 |
| 状態 | schema:itemCondition | 0 | - | 文字列 |  | リソースと同一のパッケージのリソースとの状態や数量や大きさに関する記録 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースの説明や注記とその他の属性で記録されない識別的特徴 |
| 出所 | dcterms:provenance | 0 | - | 文字列 |  | リソースを入手した情報源とそれが受け取られた状況 |

## MediaFormat

**対象クラス:** `rcgs:MediaFormat`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 種別 | rcgs:mediaFormatType | 1 | 1 | enumeration | 物理メディア \| ソフトウェア | リソースの一般形による分類 |
| 名称 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いる名称 |
| その他の名称 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いる名称 |
| 大きさ | rcgs:dimension | 0 | 1 | 文字列 |  | リソースの大きさの測定値 |
| データ容量 | schema:fileSize | 0 | 1 | 文字列 |  | リソースのファイル容量 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースの識別子を示す外部のウェブサイト |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | リソースの他の属性で記録されない識別的特徴 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースに関する説明 |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## MediaTypeOrExtent

**対象クラス:** `dcterms:MediaTypeOrExtent`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| キャリア種別 | rcgs:carrierType | 0 | 1 | enumeration | http://rdaregistry.info/termList/RDACarrierType/1001 \| http://rdaregistry.info/termList/RDACarrierType/1002 \| http://rdaregistry.info/termList/RDACarrierType/1003... | メディアの一般形の種別 |
| 数量 | dcterms:extent | 0 | 1 | 文字列 |  | メディアの数量 |
| 大きさ | rcgs:dimension | 0 | 1 | 文字列 |  | メディアの大きさの測定値 |
| メディアフォーマット | schema:encodingFormat | 0 | 1 | 構造化 |  | パッケージのメインユニットのメディア形式 |
| ファイルサイズ | schema:contentSize | 0 | - | 文字列 |  | メディアのファイルサイズ |

## OnlinePackage

**対象クラス:** `rcgs:OnlinePackage`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| URL | schema:downloadUrl | 0 | - | 文字列 |  | リソースを取得するためのURL |

## Organization

**対象クラス:** `foaf:Organization`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| サブタイプ | schema:additionalType | 0 | 1 | 構造化 |  | 団体の一般形の分類 |
| 設立日 | schema:startDate | 0 | 1 | 構造化 |  | 団体の設立日 |
| 廃止日 | schema:endDate | 0 | 1 | 構造化 |  | 団体の廃止日 |
| 住所 | schema:address | 0 | - | 文字列 |  | 団体の住所 |
| 緯度 | schema:latitude | 0 | 1 | 実数 |  | 団体の所在地の緯度 |
| 経度 | schema:longitude | 0 | 1 | 実数 |  | 団体の所在地の経度 |
| 関連する団体 | rcgs:relatedOrganization | 0 | - | 構造化 |  | 団体に関連のある団体 |
| メンバー | foaf:member | 0 | - | 構造化 |  | 団体のメンバーの個人 |
| ロゴ | foaf:logo | 0 | - | 文字列 |  | 団体のロゴ |

## Package

**対象クラス:** `rcgs:Package`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| 種別 | rdf:type | 1 | 1 | enumeration | rcgs:PhysicalPackage", \| rcgs:OnlinePackage | リソースが属するサブクラス |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| タイトル | schema:name | 1 | 1 | 文字列 |  | リソースに表記される主要なタイトル |
| 翻字タイトル | dcndl:titleTranscription | 0 | - | 文字列 |  | リソースのタイトルのカタカナかローマ字による翻字形 |
| 並列タイトル | rcgs:parallelTitle | 0 | - | 文字列 |  | リソースの主要なタイトル以外の表記されるタイトル |
| その他のタイトル | rcgs:variantTitle | 0 | - | 文字列 |  | リソースの他のタイトルの属性で記録されないタイトル |
| 省略タイトル | rcgs:abbreviatedTitle | 0 | - | 文字列 |  | リソースのタイトルの省略形 |
| エディション | dcndl:edition | 0 | - | 文字列 |  | リソースの版の識別のための指定 |
| 部編 | dcndl:volume | 0 | - | 文字列 |  | リソースがある作品やシリーズの一部であることを示す表示 |
| 責任表示 | rcgs:responsibilityStatement | 0 | - | 文字列 |  | リソースのタイトルの責任に関する表示 |
| 制作者 | rcgs:producer | 0 | - | 構造化 |  | 非複製物であるリソースを制作した主体 |
| 出版者 | rcgs:publisher | 0 | - | 構造化 |  | リソースを出版した主体 |
| 頒布者 | rcgs:distributor | 0 | - | 構造化 |  | リソースを頒布した主体 |
| 製造者 | rcgs:manufacturer | 0 | - | 構造化 |  | リソースを製造した主体 |
| ブランド | schema:brand | 0 | - | 文字列 |  | リソースの責任に関するブランド |
| 供給活動 | rcgs:provisionActivity | 0 | - | 構造化 |  | リソースの供給に関連する主体や場所や日付の情報 |
| 公開日 | dcterms:issued | 0 | - | 文字列 |  | リソースが公開された日付 |
| 著作権年 | schema:copyrightYear | 0 | 1 | 文字列 |  | リソースの著作権など保護の主張に関連する日付 |
| シリーズ表示 | rcgs:seriesStatement | 0 | - | 文字列 |  | リソースが属するシリーズのタイトルやシリーズ内ナンバーの表示 |
| サブシリーズ表示 | rcgs:subseriesStatement | 0 | - | 文字列 |  | リソースが属するサブシリーズのタイトルやサブシリーズ内ナンバーの表示 |
| 刊行方式 | rcgs:modeOfIssuance | 0 | - | enumeration | http://rdaregistry.info/termList/ModeIssue/1001 \| http://rdaregistry.info/termList/ModeIssue/1002 \| http://rdaregistry.info/termList/ModeIssue/1003... | 単独、複数部分での発行、更新方法ないしは終了の決定を反映した分類 |
| 刊行頻度 | dcndl:publicationPeriodicity | 0 | 1 | enumeration | http://rdaregistry.info/termList/frequency/1001 \| http://rdaregistry.info/termList/frequency/1002 \| http://rdaregistry.info/termList/frequency/1003... | リソースの刊行の頻度の分類 |
| 巻 | schema:volumeNumber | 0 | 1 | 整数 |  | シリアルにおける出版の巻の指定、もしくは整数による号の指定 |
| 号 | schema:issueNumber | 0 | 1 | 整数 |  | シリアルにおける出版の号の指定 |
| シリアルナンバー | schema:serialNumber | 0 | - | 文字列 |  | シリアルにおける部分を示す順番に基づく指定の表示 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部の典拠の識別子 |
| 商品ナンバー | schema:gtin13 | 0 | - | 文字列 |  | リソースの主にバーコードで提供されるGTINによる識別子 |
| ISBN | schema:isbn | 0 | - | 文字列 |  | リソースのISBNによる識別子 |
| ISSN | schema:issn | 0 | - | 文字列 |  | リソースのISSNによる識別子 |
| 型番 | rcgs:modelNumber | 0 | - | 文字列 |  | リソースの供給者が定義する型番による識別子 |
| 全国書誌番号 | rcgs:jpNumber | 0 | - | 文字列 |  | リソースの全国書誌場号による識別子 |
| 国会図書館書誌ID | rcgs:ndlBibID | 0 | - | 文字列 |  | リソースの国会図書館書誌IDによる識別子 |
| OCLCナンバー | rcgs:oclcNumber | 0 | - | 文字列 |  | リソースのOCLCによる識別子 |
| メインユニット形式 | dcterms:format | 1 | - | 構造化 |  | リソースのメインユニットのメディア形式とその数量や大きさ |
| サブユニット形式 | rcgs:formatOfSubunit | 0 | - | 構造化 |  | リソースのサブユニットのメディア形式とその数量や大きさ |
| 放送標準 | schema:videoFormat | 0 | 1 | 文字列 |  | リソースのプレイに用いられるテレビ放送のシステム |
| デジタルファイル種別 | rcgs:digitalFileType | 0 | - | enumeration | http://rdaregistry.info/termList/fileType/1001 \| http://rdaregistry.info/termList/fileType/1002 \| http://rdaregistry.info/termList/fileType/1003... | コンピュータファイルとして符号化されたデータの内容の一般形の分類 |
| 解像度 | schema:videoFrameSize | 0 | - | 文字列 |  | デジタル画像の明瞭度または細かさ |
| リージョンコード | schema:regionsAllowed | 0 | 1 | 文字列 |  | キャリアの再生においてデバイスの限定を示す符号化の単独または複数の地域の指定 |
| ミドルウェア・ゲームエンジン | rcgs:middlewareOrGameEngine | 0 | - | 文字列 |  | リソースの制作に用いられたミドルウェアもしくはゲームエンジン |
| DRM | rcgs:drm | 0 | - | 文字列 |  | ゲーム利用制御のためのデジタルライツ技術 |
| 代表的イメージ | rcgs:representativeImage | 0 | - | 文字列 |  | ゲームを代表する公式に公開されたパッケージなどの画像 |
| サムネイル画像 | schema:thumbnailUrl | 0 | - | 文字列 |  | ゲームパッケージのサムネイル画像 |
| ゲームプラットフォーム | schema:gamePlatform | 0 | - | 構造化 |  | リソースをプレイするためのゲームプラットフォーム |
| 価格 | schema:price | 0 | - | 文字列 |  | リソースの供給者による希望小売価格 |
| 年齢レーティング | schema:contentRating | 0 | - | 構造化 |  | リソースが想定する対象者を示す年齢レーティングの分類 |
| レーティング内容記述子 | rcgs:ratingContentDescriptor | 0 | - | 文字列 |  | 年齢レーティングの要因を示す内容の種別の分類 |
| アクセス制限 | dcterms:accessRights | 0 | - | 文字列 |  | リソースのアクセス制限 |
| プレイヤー数 | schema:numberOfPlayers | 0 | - | 文字列 |  | リソースを同時にプレイする人数 |
| システム要件 | schema:requirement | 0 | - | 文字列 |  | リソースのプレイの要件となる装置もしくはシステムの要件 |
| 収録するバリエーション | rcgs:embodimentOf | 0 | - | 構造化 |  | パッケージにより具体化されるバリエーション |
| 収録する作品 | rcgs:embodiedWork | 0 | - | 構造化 |  | パッケージにより具体化される作品 |
| 例示としての個別資料 | rcgs:exemplar | 0 | - | 構造化 |  | リソースを例示する個別資料 |
| 下位のリソース | dcterms:hasPart | 0 | - | 構造化 |  | リソースの論理的・物理的に部分として持つリソース |
| 上位のリソース | dcterms:isPartOf | 0 | - | 構造化 |  | リソースの論理的・物理的な部分であるリソース |
| コンタクト情報 | schema:contactPoints | 0 | - | 文字列 |  | リソースに表記されるアクセス先である電話番号 |
| オフィシャルウェブサイト | schema:url | 0 | - | 文字列 |  | リソースの制作者や供給者によるオフィシャルウェブサイト |
| 著作権表記 | dcterms:rights | 0 | - | 文字列 |  | リソースの権利の表記 |
| サブユニットリスト | dcterms:tableOfContents | 0 | - | 文字列 |  | リソースを構成するサブユニットのリスト |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースの説明や注記とその他の属性で記録されない識別的特徴 |

## Person

**対象クラス:** `foaf:Person`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| 職業専門分野 | schema:hasOccupation | 0 | - | 文字列 |  | 個人の本業や副業 |
| 生年 | schema:birthDate | 0 | 1 | 構造化 |  | 個人の生年 |
| 没年 | schema:deathDate | 0 | 1 | 構造化 |  | 個人の没年 |
| 出生地 | schema:birthPlace | 0 | 1 | 文字列 |  | 個人の誕生した場所 |
| 死没地 | schema:deathPlace | 0 | 1 | 文字列 |  | 個人の死没した場所 |
| 居住地等 | schema:homeLocation | 0 | - | 文字列 |  | 個人の居住地 |
| メールアドレス | foaf:mbox | 0 | - | 文字列 |  | 個人の公開されたメールアドレス |
| 国 | schema:addressCountry | 0 | - | 文字列 |  | 個人を識別するための国 |
| フルネーム | schema:additionalName | 0 | - | 文字列 |  | 個人の名称の展開形 |
| 敬称 | foaf:title | 0 | - | 文字列 |  | 個人の称号 (Mr, Mrs, Ms, Dr. etc)  |

## PhysicalPackage

**対象クラス:** `rcgs:PhysicalPackage`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| 大きさ | rcgs:dimension | 0 | 1 | 文字列 |  | リソースの大きさの測定値 |
| 素材 | dcterms:medium | 0 | - | enumeration | http://rdaregistry.info/termList/RDAMaterial/1001 \| http://rdaregistry.info/termList/RDAMaterial/1002 \| http://rdaregistry.info/termList/RDAMaterial/1003... | リソースを物理的に構成する素材の分類 |

## Platform

**対象クラス:** `rcgs:Platform`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| サブタイプ | schema:additionalType | 0 | - | 構造化 |  | リソースが所属するクラスにおけるサブタイプの指定 |
| 名称 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他の名称 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| 地理的範囲 | dcterms:spatial | 0 | - | 文字列 |  | リソースの用いられる場所 |
| 公開者 | dcterms:publisher | 0 | - | 構造化 |  | リソースを公開した主体 |
| 公開地 | dcndl:location | 0 | - | 文字列 |  | リソースの公開に関連する場所 |
| 公開日 | dcterms:issued | 0 | - | 構造化 |  | リソースの公開に関連する日付 |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | リソースの他の属性で記録されない識別的特徴 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| 実装される装置 | rcgs:deviceImplimented | 0 | - | 構造化 |  | リソースを実装する装置 |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 構造化 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| URL | schema:url | 0 | - | 文字列 |  | リソースに関連するURL |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## ProvisionActivity

**対象クラス:** `rcgs:ProvisionActivity`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 種別 | rdf:type | 1 | 1 | enumeration | rcgs:Production \| rcgs:Publication \| rcgs:Distribution... | リソースの一般形による分類（制作、出版、頒布、製造） |
| 発行者名表示 | rcgs:publisherStatement | 0 | - | 文字列 |  | リソースを発行する主体の表示される名称 |
| 日付 | dcterms:date | 0 | 1 | 構造化 |  | リソースに関連する日付 |
| 出所 | dcterms:spatial | 0 | - | 文字列 |  | リソースに関連する場所 |
| 出典 | dcterms:source | 0 | - | 文字列 |  | レコードを作成する上で参照したリソース |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |

## RelatedInstance

**対象クラス:** `rcgs:RelatedInstance`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| 資料種別 | rdf:type | 1 | 1 | 構造化 |  | リソースの一般形による分類 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| タイトル | schema:name | 1 | 1 | 文字列 |  | リソースに表記される主要なタイトル |
| 翻字タイトル | dcndl:titleTranscription | 0 | - | 文字列 |  | リソースのタイトルのカタカナかローマ字による翻字形 |
| 並列タイトル | rcgs:parallelTitle | 0 | - | 文字列 |  | リソースの主要なタイトル以外の表記されるタイトル |
| その他のタイトル | dcterms:alternative | 0 | - | 文字列 |  | リソースの他のタイトルの属性で記録されないタイトル |
| 省略タイトル | rcgs:abbreviatedTitle | 0 | - | 文字列 |  | リソースのタイトルの省略形 |
| エディション | dcndl:edition | 0 | - | 文字列 |  | リソースの版の識別のための指定 |
| 部編 | dcndl:volume | 0 | - | 文字列 |  | リソースがある作品やシリーズの一部であることを示す表示 |
| 責任表示 | rcgs:responsibilityStatement | 0 | - | 文字列 |  | リソースのタイトルの責任に関する表示 |
| 創作者 | dcterms:creator | 0 | - | 構造化 |  | リソースの創作に責任を持つ主体 |
| 貢献者 | rcgs:contribution | 0 | - | 構造化 |  | リソースに貢献した主体 |
| 公開日 | dcterms:issued | 0 | - | 文字列 |  | リソースが公開された日付 |
| 形式 | dcterms:format | 1 | - | 構造化 |  | リソースのメディア形式とその数量や大きさ |
| サブユニット形式 | rcgs:formatOfSubunit | 0 | - | 構造化 |  | リソースのサブユニットのメディア形式とその数量や大きさ |
| 大きさ | rcgs:dimension | 0 | 1 | 文字列 |  | リソースの大きさの測定値 |
| 素材 | dcterms:medium | 0 | - | enumeration | http://rdaregistry.info/termList/RDAMaterial/1001 \| http://rdaregistry.info/termList/RDAMaterial/1002 \| http://rdaregistry.info/termList/RDAMaterial/1003... | リソースを物理的に構成する素材 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースの識別子を示す外部のウェブサイト |
| GTIN | schema:gtin13 | 0 | - | 文字列 |  | リソースの主にバーコードで提供されるGTINによる識別子 |
| ISBN | schema:isbn | 0 | - | 文字列 |  | リソースのISBNによる識別子 |
| ISSN | schema:issn | 0 | - | 文字列 |  | リソースのISSNによる識別子 |
| 型番 | rcgs:modelNumber | 0 | - | 文字列 |  | リソースの供給者が定義する型番による識別子 |
| 全国書誌番号 | rcgs:jpNumber | 0 | - | 文字列 |  | リソースの全国書誌番号による識別子 |
| 国会図書館書誌ID | rcgs:ndlBiBID | 0 | - | 文字列 |  | リソースの国会図書館書誌IDによる識別子 |
| OCLCナンバー | rcgs:oclcNumber | 0 | - | 文字列 |  | リソースのOCLCナンバーによる識別子 |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| 著作権年 | schema:copyrightYear | 0 | 1 | 文字列 |  | リソースの著作権など保護の主張に関連する日付 |
| アクセス制限 | dcterms:accessRights | 0 | - | 文字列 |  | リソースのアクセス制限 |
| 下位の関連資料 | dcterms:hasPart | 0 | - | 構造化 |  | リソースの論理的・物理的に部分として持つリソース |
| 上位の関連資料 | dcterms:isPartOf | 0 | - | 構造化 |  | リソースの論理的・物理的な部分であるリソース |
| 概要 | dcterms:abstract | 0 | - | 文字列 |  | リソースの内容の概要 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースの説明や注記とその他の属性で記録されない識別的特徴 |
| 言語 | dcterms:language | 0 | - | 構造化 |  | リソースの内容で用いられる言語 |
| 主題 | schema:about | 0 | - | 構造化 |  | リソースのトピック |
| サブユニットリスト | dcterms:tableOfContents | 0 | - | 文字列 |  | リソースを構成するサブユニットのリスト |
| ブランド | schema:brand | 0 | - | 文字列 |  | リソースの責任に関連するブランド |
| 供給活動 | rcgs:provisionActivity | 0 | - | 構造化 |  | リソースの供給に関連する主体や場所や日付の情報 |
| 制作者 | rcgs:producer | 0 | - | 構造化 |  | 非複製物であるリソースを制作した主体 |
| 出版者 | rcgs:publisher | 0 | - | 構造化 |  | リソースを出版した主体 |
| 頒布者 | rcgs:distributor | 0 | - | 構造化 |  | リソースを頒布した主体 |
| 製造者 | rcgs:manufacturer | 0 | - | 構造化 |  | リソースを製造した主体 |
| シリーズ表示 | rcgs:seriesStatement | 0 | - | 文字列 |  | リソースが属するシリーズのタイトルやシリーズ内ナンバーの表示 |
| サブシリーズ表示 | rcgs:subseriesStatement | 0 | - | 文字列 |  | リソースが属するサブシリーズのタイトルやサブシリーズ内ナンバーの表示 |
| 刊行方式 | rcgs:modeOfIssuance | 0 | - | enumeration | http://rdaregistry.info/termList/ModeIssue/1001 \| http://rdaregistry.info/termList/ModeIssue/1002 \| http://rdaregistry.info/termList/ModeIssue/1003... | 単独、複数部分での発行、更新方法ないしは終了の決定を反映した分類 |
| 刊行頻度 | dcndl:publicationPeriodicity | 0 | 1 | enumeration | http://rdaregistry.info/termList/frequency/1001 \| http://rdaregistry.info/termList/frequency/1002 \| http://rdaregistry.info/termList/frequency/1003... | リソースの刊行の頻度の分類 |
| シリアルナンバー | schema:serialNumber | 0 | - | 文字列 |  | シリアルにおける部分を示す順番に基づく指定 |
| 巻 | schema:volumeNumber | 0 | 1 | 整数 |  | シリアルにおける出版の巻の指定、もしくは整数による号の指定 |
| 号 | schema:issueNumber | 0 | 1 | 整数 |  | シリアルにおける出版の号の指定 |
| 価格 | schema:price | 0 | - | 文字列 |  | リソースの供給者による希望小売価格 |
| 例示としての個別資料 | rcgs:exemplar | 0 | - | 構造化 |  | リソースを例示する個別資料 |
| URL | schema:downloadUrl | 0 | - | 文字列 |  | リソースを取得するためのウェブサイト |
| 制作日 | dcterms:created | 0 | 1 | 文字列 |  | リソースの創作に関する日付 |
| 制作地 | schema:locationCreated | 0 | 1 | 文字列 |  | リソースの創作に関する場所 |
| サムネイル画像 | schema:thumbnailUrl | 0 | - | 文字列 |  | ゲームパッケージのサムネイル画像 |

## Topic

**対象クラス:** `rcgs:Topic`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| 名称 | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他の名称 | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| カテゴリ | rcgs:category | 0 | - | 文字列 |  | リソースの一般化された形式（e.g. テーマ，場所，キャラクター） |
| 概念体系 | skos:inScheme | 0 | - | 文字列 |  | リソースが所属する概念体系 |
| 日付 | dcterms:date | 0 | - | 構造化 |  | リソースに関する日付 |
| 地理的範囲 | dctems:spatial | 0 | - | 文字列 |  | リソースに関する場所 |
| 上位のリソース | dcterms:isPartOf | 0 | - | 構造化 |  | リソースを論理的・物理的に部分として持つリソース |
| 下位のリソース | dcterms:hasPart | 0 | - | 構造化 |  | リソースの論理的・物理的な部分であるリソース |
| 同一のリソース | owl:sameAs | 0 | - | 文字列 |  | 全く同じものを示すリソース |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 文字列 |  | 同じもしくは関連する外部のリソース |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別についての注記 |

## Variation

**対象クラス:** `rcgs:Variation`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| タイトル | skos:prefLabel | 0 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他のタイトル | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| バージョン | schema:version | 0 | - | 文字列 |  | リソースの識別のための版の指定 |
| 出演者 | schema:actor | 0 | - | 構造化 |  | リソースの内容に出演した主体 |
| 貢献 | rcgs:contribution | 0 | - | 構造化 |  | リソースに貢献した主体 |
| 賞 | schema:award | 0 | - | 文字列 |  | リソースの内容に授与された賞 |
| 日付 | dcterms:date | 0 | 1 | 構造化 |  | リソースに関連する日付 |
| スクリーンショット | rcgs:screenShot | 0 | - | 文字列 |  | ゲームプレイの画面イメージ |
| ゲームプレイ映像 | rcgs:gamePlayImage | 0 | - | 文字列 |  | 紹介やカットシーンを除くゲームプレイの映像 |
| ミドルウェア・ゲームエンジン | rcgs:middlewareOrGameEngine | 0 | - | 文字列 |  | リソースの制作に用いられたミドルウェアもしくはゲームエンジン |
| ゲームプラットフォーム | schema:gamePlatform | 0 | - | 構造化 |  | リソースをプレイするためのゲームプラットフォーム |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部の典拠の識別子 |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | 他の属性や関連で記録されないリソースの識別的特徴 |
| 概要 | dcterms:abstract | 0 | - | 文字列 |  | リソースの内容の概要 |
| 内容種別 | rcgs:contentType | 0 | - | enumeration | http://rdaregistry.info/termList/RDAContentType/1001 \| http://rdaregistry.info/termList/RDAContentType/1002 \| http://rdaregistry.info/termList/RDAContentType/1003... | リソースの形態の一般形による種別 |
| 音声 | schema:audio | 0 | - | enumeration | http://rdaregistry.info/termList/soundCont/1001 \| http://rdaregistry.info/termList/soundCont/1002 | リソースの内容における音声の有無 |
| 色彩 | schema:color | 0 | - | enumeration | http://rdaregistry.info/termList/RDAColourContent/1002 \| http://rdaregistry.info/termList/RDAColourContent/1003 | リソースの内容における色や色調 |
| アスペクト比 | rcgs:aspectRatio | 0 | - | enumeration | http://rdaregistry.info/termList/AspectRatio/1001 \| http://rdaregistry.info/termList/AspectRatio/1002 \| http://rdaregistry.info/termList/AspectRatio/1003 | リソースの動画の幅と高さの数値の比率 |
| 言語 | dcterms:language | 0 | - | 構造化 |  | リソースの内容の言語 |
| 作品 | rcgs:variationOf | 0 | 1 | 構造化 |  | リソースにより実現される作品 |
| 専用装置 | rcgs:specialHardware | 0 | - | 構造化 |  | ゲームプレイに推奨されるもしくは必要とされる追加の装置 |
| カスタマイズオプション | rcgs:customizationOption | 0 | - | 文字列 |  | プレイヤー個人の経験のためのキャラクターや難易度についてのゲーム内の選択 |
| ネットワーク機能 | rcgs:networkedFutures | 0 | - | 文字列 |  | 企業や他のプレイヤーと接続しゲーム経験を提供するための機能や特徴 |
| 接続性 | rcgs:connectivity | 0 | - | 文字列 |  | ネットワーク機能を実現する技術 |
| エンディング | rcgs:ending | 0 | - | 真偽値 |  | エンディングの有無 |
| マルチエンディング | rcgs:multipleEnding | 0 | - | 真偽値 |  | マルチエンディングの有無 |
| ポストゲームコンテンツ | rcgs:postGameContents | 0 | - | 真偽値 |  | エンディング後のさらなるゲームプレイのための内容の有無 |
| プレイ時間 | rcgs:estimatedTimeOfCompletion | 0 | - | 文字列 |  | ゲームを完了するまでに必要とされる時間の平均 |
| ビジュアルスタイル | rcgs:visualStyle | 0 | - | 文字列 |  | ゲームの認識可能な外観に共通する主要な形式 |
| 次元 | rcgs:dimension | 0 | - | 構造化 |  | ゲーム内の表象的実体の深さや奥行きについての意図された形式や見方 |
| 視点 | rcgs:pointOfView | 0 | - | 構造化 |  | ゲーム内におけるプレイヤーが経験する視点の形式 |
| トレイラー | rcgs:trailer | 0 | - | 文字列 |  | プロモーションのためにゲーム開発者か出版者によりリリース・承認された映像 |
| 難易度の選択 | rcgs:difficultyOption | 0 | - | 文字列 |  | 選択できる難易度の段階やリスト |
| 収録されたパッケージ | rcgs:embodiment | 0 | - | 構造化 |  | リソースを具体化するパッケージ |
| 関連するバリエーション | dcterms:relation | 0 | - | 構造化 |  | リソースの関連を持つリソース |
| 下位のリソース | dcterms:hasVersion | 0 | - | 構造化 |  | リソースの論理的・物理的に部分として持つリソース |
| 上位のリソース | dcterms:isVersionOf | 0 | 1 | 構造化 |  | リソースの論理的・物理的な部分であるリソース |
| 先行のリソース | rcgs:procedes | 0 | - | 構造化 |  | リソースの同一作品の先行するリソース |
| 後続のリソース | rcgs:succeeds | 0 | - | 構造化 |  | リソースの同一作品の後続するリソース |
| 補完されたリソース | rcgs:supplements | 0 | - | 構造化 |  | リソースの同一作品の補完されたリソース |
| 相互補完のリソース | rcgs:complements | 0 | - | 構造化 |  | リソースと同一作品の相互補完的なリソース |
| クロスプレイ可能なリソース | rcgs:crossPlay | 0 | - | 構造化 |  | リソースと同一作品のクロスプラットフォームプレイ可能なリソース |
| ローカライズされたリソース | rcgs:localizedAs | 0 | - | 構造化 |  | リソースが同一作品のローカライズされたリソース |
| 移植されたリソース | rcgs:porting | 0 | - | 構造化 |  | リソースの同一作品の移植であるリソース |
| 増補されたリソース | rcgs:expandedAs | 0 | - | 構造化 |  | リソースの同一作品の増補であるリソース |
| バグフィックスされたリソース | rcgs:bugfix | 0 | - | 構造化 |  | リソースの同一作品のバグが修正されたリソース |
| 体験版のリソース | rcgs:trial | 0 | - | 構造化 |  | リソースの同一作品の体験版のリソース |
| 集約されたリソース | rcgs:aggregates | 0 | - | 構造化 |  | リソースが集約するリソース |
| 集約元のリソース | rcgs:aggregatedBy | 0 | - | 構造化 |  | リソースが集約されるリソース |
| 注記 | skos:note | 0 | - | 文字列 |  | リソースの識別に関する注記 |
| 内容記述 | dcterms:description | 0 | - | 文字列 |  | リソースの内容に関する記述 |

## Work

**対象クラス:** `rcgs:Work`

| 項目名 | プロパティ | 最小 | 最大 | 値タイプ | 値制約 | コメント |
|--------|------------|------|------|----------|--------|----------|
| レコードID | rcgs:recordID | 1 | 1 | 文字列 |  | リソースの記述単位毎に付与される識別子 |
| 管理メタデータ | rcgs:adminMetadata | 0 | 1 | 構造化 |  | メタデータの管理情報 |
| 形式 | rdf:type | 0 | - | 構造化 |  | リソースの形式 |
| ラベル | dcterms:title | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| ラベル | rdfs:label | 1 | 1 | 文字列 |  | リソースの文字列構造化もしくは符号化による識別のための名称 |
| タイトル | skos:prefLabel | 1 | 1 | 文字列 |  | リソースの優先的に用いられる名称 |
| その他のタイトル | skos:altLabel | 0 | - | 文字列 |  | リソースの代替的に用いられる名称 |
| 地理的範囲 | dcterms:spatial | 0 | - | 文字列 |  | リソースに関する場所 |
| 日付 | dcterms:date | 0 | 1 | 構造化 |  | リソースに関する日付 |
| 説明 | dcterms:description | 0 | - | 文字列 |  | リソースの内容に関する説明 |
| 識別子 | dcterms:identifier | 0 | - | 文字列 |  | 同じもしくは関連するリソースを示す外部の典拠の識別子 |
| マッピング | skos:closeMatch | 0 | - | 文字列 |  | レコードを作成するにあたって基準となるWikidataのレコード |
| Youtube Gaming ID | rcgs:youtubeGaming | 0 | - | 文字列 |  | Youtube Gamingのリソースの識別子 |
| Twitch Game ID | rcgs:twitch | 0 | - | 文字列 |  | Twitchののリソースの識別子 |
| Freebase ID | rcgs:freebase | 0 | - | 文字列 |  | Freebaseのリソースの識別子 |
| MobyGames ID | rcgs:mobyGames | 0 | - | 文字列 |  | MobyGamesのリソースの識別子 |
| Metacritic ID | rcgs:metacritic | 0 | - | 文字列 |  | Metacriticsのリソースの識別子 |
| 外部の関連リソース | rdfs:seeAlso | 0 | - | 構造化 |  | 同じもしくは関連するリソースを示す外部のウェブサイト |
| Imdb ID | rcgs:imdb | 0 | - | 文字列 |  | Imdbのリソースの識別子 |
| ゲームプレイジャンル | schema:genre | 0 | - | 構造化 |  | ゲームの目的やルールの形式や特徴などに基づくゲームの全般的性質 |
| 物語ジャンル | rcgs:narrativeGenre | 0 | - | 構造化 |  | ゲーム世界やプロットの一般的形式 |
| 概要 | dcterms:abstract | 0 | - | 文字列 |  | リソースの内容の短い説明や表示 |
| テーマ | rcgs:theme | 0 | - | 構造化 |  | ゲームで繰り返し登場する筋道やモチーフや主題やアイデア |
| ムード | rcgs:mood | 0 | - | 構造化 |  | 特定の感情や心情を喚起するゲームの雰囲気やトーンの形式 |
| 時期設定 | rcgs:setting | 0 | - | 文字列 |  | ゲーム内で位置づけられる時期 |
| シリーズ | rcgs:series | 0 | - | 構造化 |  | しばしばナンバリングで示される物語の継続やゲームプレイやテーマの類似性を示す複数のゲーム作品に共通する名称 |
| フランチャイズ | rcgs:franchise | 0 | - | 構造化 |  | 知的財産やデータの関連やコンテンツの共有などに関連する一般的な名称 |
| メカニクス | rcgs:mechanic | 0 | - | 文字列 |  | ゲームの進展と状態との相互作用に用いられる主要な方法とルール |
| 主人公 | rcgs:protagonist | 0 | - | 構造化 |  | プレイヤーが操作する主人公 |
| 対象者 | dcterms:audience | 0 | - | 文字列 |  | リソースが想定する対象者 |
| 内容の性質 | rcgs:natureOfContent | 0 | - | 文字列 |  | リソースの主要なコンテンツの特性 |
| ナンバー指示子 | schema:serialNumber | 0 | 1 | 文字列 |  | シリアルのリソースの一部である場合の部分の指定 |
| その他の識別的特徴 | schema:disambiguatingDescription | 0 | - | 文字列 |  | 他の属性や関連で記録されないリソースの識別的特徴 |
| 出所 | schema:locationCreated | 0 | - | 文字列 |  | リソースの創作に関する場所 |
| 主題 | schema:about | 0 | - | 構造化 |  | リソースのトピック |
| 主題とするリソース | schema:subjectOf | 0 | - | 構造化 |  | リソースを主題とするリソース |
| キャラクター | schema:character | 0 | - | 構造化 |  | リソースのコンテンツに登場するキャラクター |
| 舞台 | schema:gameLocation | 0 | - | 構造化 |  | ゲーム内で舞台となる場所 |
| 創作者 | dcterms:creator | 0 | - | 構造化 |  | リソースの創作に責任を持つ主体 |
| 制作企業 | schema:productionCompany | 0 | - | 構造化 |  | リソースの制作に責任を持つ団体 |
| 関連する主体 | rcgs:relatedAgent | 0 | - | 構造化 |  | リソースに関連を持つ主体 |
| ロゴ | schema:logo | 0 | - | 文字列 |  | リソースを示すロゴ画像 |
| 作品のバリエーション | rcgs:variation | 0 | - | 構造化 |  | 作品を実現するバリエーション |
| 作品のパッケージ | rcgs:embodiment | 0 | - | 構造化 |  | 作品を具体化するパッケージ |
| 関連するリソース | dcterms:relation | 0 | - | 構造化 |  | リソースに関連を持つリソース |
| 上位のリソース | dcterms:isPartOf | 0 | 1 | 構造化 |  | リソースを論理的・物理的に部分として持つリソース |
| 下位のリソース | dcterms:hasPart | 0 | - | 構造化 |  | リソースの論理的・物理的な部分であるリソース |
| 先行のリソース | rcgs:precedes | 0 | - | 構造化 |  | リソースに先行するリソース |
| 後続のリソース | rcgs:succeeds | 0 | - | 構造化 |  | リソースに後続するリソース |
| 物語上の先行のリソース | rcgs:sequelTo | 0 | - | 構造化 |  | リソースに物語上先行するリソース |
| 物語上の後続のリソース | rcgs:sequel | 0 | - | 構造化 |  | リソースに物語上後続するリソース |
| リメイクされたリソース | rcgs:remadeAs | 0 | - | 構造化 |  | リソースのリメイク元であるリソース |
| 補完されたリソース | rcgs:complements | 0 | - | 構造化 |  | リソースの補完されたリソース |
| 増補されたリソース | rcgs:expandedAs | 0 | - | 構造化 |  | リソースの増補されたリソース |
| スピンオフされたリソース | rcgs:spinOff | 0 | - | 構造化 |  | リソースのスピンオフされたリソース |
| 注記 | skos:note | 0 | - | 文字列 |  | リソース識別に関する注記 |
