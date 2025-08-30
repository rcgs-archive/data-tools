# RCGS Archive

立命館大学ゲーム研究センター（RCGS）のゲームアーカイブプロジェクト

## 📖 ドキュメント

**🌐 GitHub Pages**: https://fukudakz.github.io/rcgs_archive/

完全なドキュメントとスキーマ仕様書はGitHub Pagesサイトで公開しています。

## 概要

このプロジェクトは、デジタルゲームアーカイブのためのメタデータスキーマとデータ変換ツールを提供します。SHACL（Shapes Constraint Language）ベースの包括的なメタデータスキーマにより、ゲーム作品、バリエーション、パッケージ、個別資料の詳細な記述が可能です。

### 主要コンポーネント

- **メタデータスキーマ**: W3C SHACL標準に準拠した19クラスのメタデータ定義
- **変換ツール**: Excel/DSP仕様からSHACLスキーマへの自動変換
- **ドキュメント生成**: SHACLスキーマからMarkdown仕様書の自動生成
- **RDFデータ**: Linked Dataとしての利用が可能

## 🗂️ ディレクトリ構造

```
rcgs_archive/
├── docs/                          # GitHub Pages ドキュメント
│   ├── schema/                    # メタデータスキーマ仕様
│   ├── tools/                     # ツール・スクリプト説明
│   ├── api/                       # API・データ形式
│   └── _config.yml               # Jekyll設定
├── src/                           # ソースコード
│   └── shacl_and_validation/      # SHACL関連ツール
├── metadata_schema/               # スキーマファイル
└── README.md                      # このファイル
```

## 🛠️ 主要ツール

### DSP to SHACL 変換
```bash
cd src/shacl_and_validation
python dsp_convert_to_shacl.py
```

Excel形式のDSP仕様書からSHACL TTLファイルを生成します。

### SHACL to Markdown 変換
```bash
cd src/shacl_and_validation
python shacl_to_markdown.py
```

SHACL TTLファイルからMarkdown形式の仕様書を生成します。

## 📊 メタデータスキーマ

### クラス階層
- **Work** (作品): ゲーム作品の基本情報
- **Variation** (バリエーション): 作品の版や移植版
- **Package** (パッケージ): 物理的・デジタル的な配布形態
- **Item** (個別資料): 具体的なコレクション資料

### その他のクラス
- **Agent** (主体): 個人・組織情報
- **Platform** (プラットフォーム): ゲーム機・システム
- **Device** (装置): ハードウェア機器
- **Topic** (主題): ジャンル・テーマ・キャラクター
- その他11クラス

## 🌐 データ形式

- **RDF/Turtle**: 主要なデータ交換形式
- **JSON-LD**: Web API向けJSON形式
- **SHACL**: スキーマ定義・バリデーション
- **SPARQL**: データクエリ・検索

## 🔧 環境構築

### 依存関係
```bash
pip install pandas rdflib pyshacl openpyxl
```

### 必要なソフトウェア
- Python 3.8+
- Git

## 📄 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🏛️ 組織

**立命館大学ゲーム研究センター（RCGS）**
- 研究・アーカイブ活動
- デジタルゲーム文化の保存と研究

## 🤝 コントリビューション

プロジェクトへの貢献を歓迎します。Issues やPull Requestsをお気軽にお送りください。

---

**詳細なドキュメント**: https://fukudakz.github.io/rcgs_archive/
