import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse
import sys
import japanize_matplotlib
import os
from datetime import datetime
import warnings

# フォント警告を無効化
warnings.filterwarnings('ignore', category=UserWarning, module='matplotlib')

# 日本語フォントの設定
plt.rcParams['font.family'] = ['DejaVu Sans', 'Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

class LightingChecker:
    """白紙の写真のライティングをチェックするクラス"""
    
    def __init__(self, grid_size=(10, 10)):
        """
        初期化
        
        Args:
            grid_size (tuple): グリッドサイズ (行, 列)
        """
        self.grid_size = grid_size
        
    def load_image(self, image_path):
        """
        画像を読み込む
        
        Args:
            image_path (str): 画像ファイルのパス
            
        Returns:
            numpy.ndarray: 読み込んだ画像（グレースケール）
        """
        if not Path(image_path).exists():
            raise FileNotFoundError(f"画像ファイルが見つかりません: {image_path}")
        
        # 画像を読み込み、グレースケールに変換
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"画像を読み込めませんでした: {image_path}")
        
        return image
    
    def create_grid_brightness(self, image):
        """
        画像をグリッドに分割し、各セルの明度を計算
        
        Args:
            image (numpy.ndarray): 入力画像（グレースケール）
            
        Returns:
            numpy.ndarray: 各グリッドセルの平均明度を格納した2次元配列
        """
        height, width = image.shape
        grid_height = height // self.grid_size[0]
        grid_width = width // self.grid_size[1]
        
        brightness_grid = np.zeros(self.grid_size)
        
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                # グリッドセルの範囲を計算
                y_start = i * grid_height
                y_end = (i + 1) * grid_height if i < self.grid_size[0] - 1 else height
                x_start = j * grid_width
                x_end = (j + 1) * grid_width if j < self.grid_size[1] - 1 else width
                
                # セル内の平均明度を計算
                cell = image[y_start:y_end, x_start:x_end]
                brightness_grid[i, j] = np.mean(cell)
        
        return brightness_grid
    
    def create_heatmap(self, brightness_grid, image_shape, save_path=None, show_stats=True):
        """
        明度のヒートマップを作成
        
        Args:
            brightness_grid (numpy.ndarray): 明度グリッド
            image_shape (tuple): 元画像の形状 (height, width)
            save_path (str, optional): 保存パス
            show_stats (bool): 統計情報を表示するかどうか
        """
        # 元画像のアスペクト比を計算
        height, width = image_shape
        aspect_ratio = width / height
        
        # ヒートマップのサイズを元画像の比率に合わせて調整
        if aspect_ratio > 1:  # 横長の画像
            heatmap_width = 8
            heatmap_height = 8 / aspect_ratio
        else:  # 縦長または正方形の画像
            heatmap_height = 8
            heatmap_width = 8 * aspect_ratio
        
        # 統計情報用の幅を追加
        total_width = heatmap_width + 6 if show_stats else heatmap_width
        
        plt.figure(figsize=(total_width, max(heatmap_height, 6)))
        
        if show_stats:
            # メインのヒートマップ（統計情報ありの場合）
            plt.subplot(1, 2, 1)
            ax1 = plt.gca()
            ax1.set_aspect(aspect_ratio)
        else:
            # メインのヒートマップのみ
            ax1 = plt.gca()
            ax1.set_aspect(aspect_ratio)
        
        sns.heatmap(brightness_grid, 
                   annot=True, 
                   fmt='.1f', 
                   cmap='viridis',
                   cbar_kws={'label': '明度 (0-255)'},
                   square=False)
        plt.title('ライティング明度ヒートマップ')
        plt.xlabel('X方向グリッド')
        plt.ylabel('Y方向グリッド')
        
        if show_stats:
            # 統計情報のサブプロット
            plt.subplot(1, 2, 2)
            plt.axis('off')
            
            # 統計計算
            mean_brightness = np.mean(brightness_grid)
            std_brightness = np.std(brightness_grid)
            min_brightness = np.min(brightness_grid)
            max_brightness = np.max(brightness_grid)
            brightness_range = max_brightness - min_brightness
            cv = (std_brightness / mean_brightness) * 100  # 変動係数
            
            # 最も明るい位置と暗い位置
            max_pos = np.unravel_index(np.argmax(brightness_grid), brightness_grid.shape)
            min_pos = np.unravel_index(np.argmin(brightness_grid), brightness_grid.shape)
            
            # アーカイブ撮影用の評価基準
            archive_quality = "優秀" if cv < 2 else "良好" if cv < 3 else "要改善" if cv < 5 else "不適格"
            general_quality = "良好" if cv < 5 else "要改善" if cv < 15 else "不良"
            
            # 光量（明度）評価
            light_level = "十分" if mean_brightness >= 240 else "適正" if mean_brightness >= 220 else "やや不足" if mean_brightness >= 200 else "不足"
            shadow_risk = "低" if min_brightness >= 230 else "中" if min_brightness >= 210 else "高"
            
            stats_text = f"""ライティング統計情報

平均明度: {mean_brightness:.1f}
標準偏差: {std_brightness:.1f}
最小明度: {min_brightness:.1f} at ({min_pos[1]}, {min_pos[0]})
最大明度: {max_brightness:.1f} at ({max_pos[1]}, {max_pos[0]})
明度範囲: {brightness_range:.1f}
変動係数: {cv:.1f}%

光量評価: {light_level} (平均明度 {mean_brightness:.1f})
影リスク: {shadow_risk} (最小明度 {min_brightness:.1f})

一般撮影評価: {general_quality}
アーカイブ撮影評価: {archive_quality}

【評価基準】
均一性 - 一般: <5%(良好), アーカイブ: <2%(優秀)
光量 - 十分:≥240, 適正:≥220, やや不足:≥200
影リスク - 低:≥230, 中:≥210, 高:<210
"""
            
            plt.text(0.1, 0.9, stats_text, transform=plt.gca().transAxes, 
                    fontsize=10, verticalalignment='top', fontfamily='sans-serif')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"ヒートマップを保存しました: {save_path}")
        
        plt.show()
        
        return brightness_grid
    
    def create_output_filename(self, image_path):
        """
        出力ファイル名を自動生成
        
        Args:
            image_path (str): 入力画像のパス
            
        Returns:
            str: 出力ファイルのパス
        """
        # outputフォルダを作成
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # 入力ファイル名から拡張子を除いた名前を取得
        input_name = Path(image_path).stem
        
        # タイムスタンプを追加
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 出力ファイル名を生成
        output_filename = f"{input_name}_lighting_analysis_{timestamp}.png"
        output_path = output_dir / output_filename
        
        return str(output_path)
    
    def analyze_lighting(self, image_path, save_path=None):
        """
        ライティング分析のメイン関数
        
        Args:
            image_path (str): 分析する画像のパス
            save_path (str, optional): 結果の保存パス（指定されない場合は自動生成）
            
        Returns:
            dict: 分析結果
        """
        # 画像読み込み
        image = self.load_image(image_path)
        print(f"画像を読み込みました: {image_path}")
        print(f"画像サイズ: {image.shape[1]} x {image.shape[0]}")
        print(f"アスペクト比: {image.shape[1]/image.shape[0]:.2f}")
        
        # グリッド明度計算
        brightness_grid = self.create_grid_brightness(image)
        print(f"グリッドサイズ: {self.grid_size[1]} x {self.grid_size[0]}")
        
        # 保存パスが指定されていない場合は自動生成
        if save_path is None:
            save_path = self.create_output_filename(image_path)
        
        # ヒートマップ作成（画像の形状も渡す）
        self.create_heatmap(brightness_grid, image.shape, save_path)
        
        # 結果をまとめて返す
        mean_bright = np.mean(brightness_grid)
        min_bright = np.min(brightness_grid)
        result = {
            'brightness_grid': brightness_grid,
            'mean_brightness': mean_bright,
            'std_brightness': np.std(brightness_grid),
            'min_brightness': min_bright,
            'max_brightness': np.max(brightness_grid),
            'cv': (np.std(brightness_grid) / mean_bright) * 100,
            'light_level': "十分" if mean_bright >= 240 else "適正" if mean_bright >= 220 else "やや不足" if mean_bright >= 200 else "不足",
            'shadow_risk': "低" if min_bright >= 230 else "中" if min_bright >= 210 else "高",
            'output_path': save_path
        }
        
        return result


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='白紙写真のライティングチェック')
    parser.add_argument('image_path', help='分析する画像ファイルのパス')
    parser.add_argument('--grid-rows', type=int, default=10, help='グリッドの行数 (デフォルト: 10)')
    parser.add_argument('--grid-cols', type=int, default=10, help='グリッドの列数 (デフォルト: 10)')
    parser.add_argument('--save', help='結果画像の保存パス')
    
    args = parser.parse_args()
    
    try:
        # ライティングチェッカーを初期化
        checker = LightingChecker(grid_size=(args.grid_rows, args.grid_cols))
        
        # 分析実行
        result = checker.analyze_lighting(args.image_path, args.save)
        
        print("\n=== 分析完了 ===")
        print(f"変動係数: {result['cv']:.2f}%")
        print(f"平均明度: {result['mean_brightness']:.1f}")
        print(f"最小明度: {result['min_brightness']:.1f}")
        print(f"光量評価: {result['light_level']}")
        print(f"影リスク: {result['shadow_risk']}")
        print(f"出力ファイル: {result['output_path']}")
        
        # 白紙測定の限界に関する警告
        print("\n⚠️  測定対象による注意事項:")
        print("• 白紙測定: 照明の均一性評価には最適")
        print("• 実文書での光量: 反射率差により20-40%低下する可能性")
        print("• 推奨追加検証: グレーカード、実際の文書サンプルでの測定")
        
        # 一般撮影評価
        if result['cv'] < 5:
            print("一般撮影評価: 良好なライティング")
        elif result['cv'] < 15:
            print("一般撮影評価: ライティング要改善")
        else:
            print("一般撮影評価: ライティング不良")
        
        # アーカイブ撮影評価
        if result['cv'] < 2:
            print("アーカイブ撮影評価: 優秀（アーカイブ撮影に最適）")
        elif result['cv'] < 3:
            print("アーカイブ撮影評価: 良好（アーカイブ撮影に適している）")
        elif result['cv'] < 5:
            print("アーカイブ撮影評価: 要改善（アーカイブ撮影には改善が必要）")
        else:
            print("アーカイブ撮影評価: 不適格（アーカイブ撮影には使用不可）")
        
        # 光量に関する警告
        if result['light_level'] in ['やや不足', '不足']:
            print(f"\n⚠️  光量警告: {result['light_level']} - ISO感度調整や露出補正を検討してください")
        if result['shadow_risk'] == '高':
            print("⚠️  影警告: 暗部でのディテール損失リスクが高いです")
            
    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
