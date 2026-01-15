# DNG to WebP 変換スクリプト

VueScanでスキャンしたDNGファイルをWebP形式に一括変換するスクリプトです。

## 必要な環境

- Python 3.6以上
- ImageMagick

### ImageMagickのインストール

```bash
brew install imagemagick
```

## 使い方

```bash
python3 convert_dng_to_webp.py
```

または

```bash
./convert_dng_to_webp.py
```

## 動作

1. `/Users/fukudakazufumi/Pictures/VueScan/ポスプロ作業_beta/` フォルダ内のDNGファイルを検索
2. 各DNGファイルをWebP形式に変換
3. 変換後のファイルは `webp_output/` フォルダに保存されます

## 設定

スクリプト内の以下の変数を変更することで設定を変更できます：

- `input_dir`: 入力DNGファイルが格納されているディレクトリ
- `output_dir`: 出力WebPファイルの保存先ディレクトリ
- `webp_quality`: WebPの品質（0-100、デフォルト85）
- `icc_profile`: ICCプロファイルのパス（photo.iniから取得）

## 注意事項

- 既に存在するWebPファイルはスキップされます
- 変換には時間がかかる場合があります（1ファイルあたり数秒〜数分）
- 大きなDNGファイルの場合は、メモリを多く使用する可能性があります
