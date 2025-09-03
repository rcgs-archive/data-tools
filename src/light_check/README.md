# ライティングチェッカー (Lighting Checker)

白紙写真のライティング品質を分析し、撮影環境の均一性を評価するPythonツールです。

## 概要

このツールは、白紙を撮影した画像を分析して、ライティングの均一性を測定します。特にアーカイブ撮影や文書デジタル化において、照明の品質を客観的に評価することができます。

## 主な機能

- **グリッド分析**: 画像を指定されたグリッドに分割し、各セルの明度を計算
- **ヒートマップ生成**: 明度分布を視覚的に表示
- **統計分析**: 平均明度、標準偏差、変動係数などの統計情報を提供
- **品質評価**: 一般撮影とアーカイブ撮影の両方に対応した評価基準
- **自動レポート生成**: 分析結果を画像とテキストで出力

## インストール

### 必要な依存関係

```bash
pip install opencv-python numpy matplotlib seaborn japanize-matplotlib
```

### 要件ファイルから一括インストール

```bash
pip install -r requirements.txt
```

#### requirements.txt の内容例:
```
opencv-python>=4.5.0
numpy>=1.20.0
matplotlib>=3.3.0
seaborn>=0.11.0
japanize-matplotlib>=1.1.0
```

## 使用方法

### コマンドライン使用

#### 基本的な使用法
```bash
python light_check.py path/to/your/image.jpg
```

#### グリッドサイズを指定
```bash
python light_check.py path/to/your/image.jpg --grid-rows 15 --grid-cols 15
```

#### 出力ファイルを指定
```bash
python light_check.py path/to/your/image.jpg --save output/analysis_result.png
```

### Pythonスクリプト内での使用

```python
from light_check import LightingChecker

# チェッカーを初期化
checker = LightingChecker(grid_size=(10, 10))

# 分析実行
result = checker.analyze_lighting("path/to/your/image.jpg")

# 結果の取得
print(f"変動係数: {result['cv']:.2f}%")
print(f"平均明度: {result['mean_brightness']:.1f}")
print(f"評価: {result['light_level']}")
```

## 評価基準

### ライティング均一性（変動係数基準）

#### 一般撮影
- **良好**: 変動係数 < 5%
- **要改善**: 5% ≤ 変動係数 < 15%
- **不良**: 変動係数 ≥ 15%

#### アーカイブ撮影（より厳格な基準）
- **優秀**: 変動係数 < 2%
- **良好**: 2% ≤ 変動係数 < 3%
- **要改善**: 3% ≤ 変動係数 < 5%
- **不適格**: 変動係数 ≥ 5%

### 光量評価（平均明度基準）
- **十分**: 240以上
- **適正**: 220以上
- **やや不足**: 200以上
- **不足**: 200未満

### 影リスク評価（最小明度基準）
- **低**: 230以上
- **中**: 210以上
- **高**: 210未満

## 出力情報

### ヒートマップ
- 明度分布の視覚的表現
- 元画像のアスペクト比を保持
- 各グリッドセルの数値表示

### 統計情報
- 平均明度
- 標準偏差
- 最小・最大明度と位置
- 変動係数
- 各種評価結果

### 分析結果ファイル
- PNG形式で自動保存
- ファイル名例: `image_lighting_analysis_20240101_120000.png`
- `output/` フォルダに保存

## 使用例とユースケース

### 1. スタジオ撮影のライティング調整
```bash
# 白紙を撮影してライティングをチェック
python light_check.py studio_test.jpg

# 結果例:
# 変動係数: 1.8% → アーカイブ撮影評価: 優秀
```

### 2. 文書デジタル化プロジェクト
```bash
# より細かいグリッドで詳細分析
python light_check.py document_setup.jpg --grid-rows 20 --grid-cols 20
```

### 3. 複数セットアップの比較
```bash
# 複数の照明設定を比較
python light_check.py setup1.jpg --save comparison/setup1_analysis.png
python light_check.py setup2.jpg --save comparison/setup2_analysis.png
```

## 技術的詳細

### アルゴリズム
1. 画像をグレースケールに変換
2. 指定されたグリッドサイズで画像を分割
3. 各グリッドセルの平均明度を計算
4. 統計分析を実行
5. ヒートマップとレポートを生成

### パフォーマンス
- 処理時間: 一般的な画像（2000x3000px）で約1-3秒
- メモリ使用量: 画像サイズに比例、通常50-100MB程度

## 注意事項と制限

### 測定対象による注意点
- **白紙測定**: 照明の均一性評価には最適
- **実文書での光量**: 反射率差により20-40%低下する可能性
- **推奨追加検証**: グレーカード、実際の文書サンプルでの測定

### 環境要因
- カメラの設定（ISO、露出）による影響
- レンズの周辺減光
- 白紙の材質による反射特性の違い

### 使用上の制限
- 静止画像のみ対応
- グレースケール変換による色情報の損失
- グリッドサイズが大きすぎると局所的な問題を見逃す可能性

## トラブルシューティング

### よくある問題

#### 1. 日本語フォントが表示されない
```python
# フォント設定の確認
import matplotlib.pyplot as plt
print(plt.rcParams['font.family'])
```

#### 2. メモリエラー
- 大きな画像の場合、グリッドサイズを小さくする
- 画像を事前にリサイズする

#### 3. ファイル権限エラー
```bash
# outputフォルダの権限を確認
chmod 755 output/
```

## 開発・カスタマイズ

### クラス構造
```python
class LightingChecker:
    def __init__(self, grid_size=(10, 10))
    def load_image(self, image_path)
    def create_grid_brightness(self, image)
    def create_heatmap(self, brightness_grid, image_shape, save_path=None, show_stats=True)
    def analyze_lighting(self, image_path, save_path=None)
```

### カスタマイズ例

#### 評価基準の変更
```python
# より厳格な基準に変更
archive_quality = "優秀" if cv < 1.5 else "良好" if cv < 2.5 else "要改善"
```

#### グリッドサイズの動的調整
```python
# 画像サイズに応じたグリッド調整
height, width = image.shape
grid_size = (min(20, height//100), min(20, width//100))
```

## ライセンス

このプロジェクトは教育・研究目的で作成されています。

## 作成者・連絡先

立命館大学 ゲーム研究センター

## 更新履歴

- v1.0.0: 初期リリース
  - 基本的なライティング分析機能
  - ヒートマップ生成
  - 統計分析とレポート機能
