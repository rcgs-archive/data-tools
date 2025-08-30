# GitHub Pages セットアップ手順

このドキュメントでは、`rcgs_archive` リポジトリでGitHub Pagesを有効にする手順を説明します。

## 1. GitHub リポジトリでの設定

### 1.1 Pagesの有効化
1. GitHubの[リポジトリページ](https://github.com/fukudakz/rcgs_archive)にアクセス
2. **Settings** タブをクリック
3. 左サイドバーから **Pages** を選択
4. **Source** セクションで以下を設定：
   - **Source**: "Deploy from a branch"
   - **Branch**: "main" (またはメインブランチ)
   - **Folder**: "/docs"
5. **Save** ボタンをクリック

### 1.2 公開URL
設定完了後、サイトは以下のURLで公開されます：
```
https://fukudakz.github.io/rcgs_archive/
```

## 2. 現在のフォルダ構造

```
rcgs_archive/
├── docs/                    # GitHub Pages のルートディレクトリ
│   ├── _config.yml         # Jekyll 設定ファイル
│   ├── index.md            # トップページ
│   ├── schema/             # スキーマ関連ドキュメント
│   │   ├── index.md        # スキーマ概要
│   │   └── rcgs_schema_specification.md  # 詳細仕様書
│   ├── tools/              # ツール・スクリプト説明
│   │   └── index.md
│   ├── api/                # API・データ形式説明
│   │   └── index.md
│   └── SETUP.md           # このファイル
├── src/                    # ソースコード
├── metadata_schema/        # スキーマファイル
└── README.md              # プロジェクトREADME
```

## 3. Jekyll 設定

### 3.1 テーマ
現在の設定では `minima` テーマを使用しています。

### 3.2 主要設定
- **baseurl**: `/rcgs_archive`
- **url**: `https://fukudakz.github.io`
- **markdown**: Kramdown
- **highlighter**: Rouge (コードハイライト)

### 3.3 プラグイン
- jekyll-feed (RSS)
- jekyll-sitemap (サイトマップ)
- jekyll-seo-tag (SEO最適化)

## 4. コンテンツ更新方法

### 4.1 ドキュメント追加
1. `docs/` ディレクトリ内に Markdown ファイルを作成
2. Jekyll Front Matter を追加：
   ```yaml
   ---
   layout: default
   title: ページタイトル
   permalink: /path/to/page/
   ---
   ```
3. Git でコミット・プッシュ

### 4.2 スキーマ仕様書の更新
1. `src/shacl_and_validation/shacl_to_markdown.py` を実行
2. 生成された仕様書を `docs/schema/` にコピー
3. Jekyll Front Matter を追加
4. Git でコミット・プッシュ

### 4.3 自動更新
GitHub Actions を使用して、スキーマファイルの更新時に自動でドキュメントを生成・更新することも可能です。

## 5. カスタマイズオプション

### 5.1 テーマ変更
他のJekyllテーマを使用する場合は、`_config.yml` の `theme` を変更：
```yaml
theme: jekyll-theme-cayman  # 例
```

### 5.2 カスタムCSS
`docs/assets/css/style.scss` を作成してスタイルをカスタマイズ可能。

### 5.3 カスタムレイアウト
`docs/_layouts/` ディレクトリにカスタムレイアウトを追加可能。

## 6. トラブルシューティング

### 6.1 サイトが表示されない
- GitHub Pages の設定を確認
- ブランチとフォルダの設定が正しいか確認
- `_config.yml` の構文エラーをチェック

### 6.2 スタイルが適用されない
- `baseurl` の設定を確認
- CSS ファイルのパスを確認

### 6.3 ページが404になる
- `permalink` の設定を確認
- ファイル名とパスの整合性を確認

## 7. 追加リソース

- [GitHub Pages ドキュメント](https://docs.github.com/en/pages)
- [Jekyll ドキュメント](https://jekyllrb.com/docs/)
- [Minima テーマ](https://github.com/jekyll/minima)
