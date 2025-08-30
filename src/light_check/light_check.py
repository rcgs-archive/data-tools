import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_illumination(image_path, grid_size=5):
    """
    画像内の白い紙を検出し、その照度の均一性を分析・可視化する関数。

    Args:
        image_path (str): 分析する画像のファイルパス。
        grid_size (int): 照度を分析するグリッドの分割数 (例: 5だと5x5)。
    """
    # 1. 画像の読み込みと前処理
    img = cv2.imread(image_path)
    if img is None:
        print(f"エラー: 画像ファイル '{image_path}' が読み込めませんでした。")
        return

    # 画像が大きすぎる場合にリサイズ（処理速度向上のため）
    max_dim = 1024
    h, w = img.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img = cv2.resize(img, (int(w*scale), int(h*scale)))
    
    original_img = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # 2. 紙の輪郭を検出
    edged = cv2.Canny(blurred, 30, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        print("エラー: 画像から輪郭を検出できませんでした。撮影環境を確認してください。")
        return

    # 最も面積の大きい輪郭を紙として特定
    paper_contour = max(contours, key=cv2.contourArea)

    # 3. 紙領域の照度を分析
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [paper_contour], -1, 255, -1)
    
    # マスク内のピクセル（紙の領域）のみを抽出
    paper_pixels = gray[mask == 255]

    # 統計情報を計算
    mean_intensity = np.mean(paper_pixels)
    std_dev_intensity = np.std(paper_pixels)

    # 4. 結果をコンソールに出力
    print("--- 照度均一性 分析結果 ---")
    print(f"✅ 平均輝度: {mean_intensity:.2f} (0-255の範囲)")
    print(f"✅ 輝度の標準偏差: {std_dev_intensity:.2f}")
    print("  👉 この値が小さいほど、照明は均一です。目安として10以下を目指しましょう。")
    print("-" * 30)

    # 5. グリッド分割による詳細分析
    x, y, w, h = cv2.boundingRect(paper_contour)
    paper_region_gray = gray[y:y+h, x:x+w]
    paper_region_mask = mask[y:y+h, x:x+w]

    grid_h, grid_w = h // grid_size, w // grid_size
    grid_means = np.zeros((grid_size, grid_size))

    for i in range(grid_size):
        for j in range(grid_size):
            grid_cell = paper_region_gray[i*grid_h:(i+1)*grid_h, j*grid_w:(j+1)*grid_w]
            grid_mask_cell = paper_region_mask[i*grid_h:(i+1)*grid_h, j*grid_w:(j+1)*grid_w]
            
            valid_pixels = grid_cell[grid_mask_cell == 255]
            if valid_pixels.size > 0:
                grid_means[i, j] = np.mean(valid_pixels)

    print(f"--- グリッド別 平均輝度 ({grid_size}x{grid_size}) ---")
    print("  👉 各エリアの明るさです。数値の差が少ないほど理想的です。")
    print(np.round(grid_means, 1))
    print("-" * 30)


    # 6. 結果の可視化 (ヒートマップ)
    # 輪郭を描画した画像を作成
    result_img = original_img.copy()
    cv2.drawContours(result_img, [paper_contour], -1, (0, 255, 0), 3)

    # ヒートマップを作成
    heatmap = cv2.resize(grid_means, (w, h), interpolation=cv2.INTER_LINEAR)
    heatmap_normalized = cv2.normalize(heatmap, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    heatmap_color = cv2.applyColorMap(heatmap_normalized, cv2.COLORMAP_JET)

    # 紙の領域だけにヒートマップを適用
    heatmap_masked = cv2.bitwise_and(heatmap_color, heatmap_color, mask=paper_region_mask)
    
    # 元画像とヒートマップを合成
    target_region = result_img[y:y+h, x:x+w]
    alpha = 0.6 # ヒートマップの透明度
    cv2.addWeighted(heatmap_masked, alpha, target_region, 1 - alpha, 0, target_region)

    # Matplotlibで結果画像を表示
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('照度均一性 分析レポート', fontsize=16)

    # 元画像（紙検出）
    axes[0].imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    cv2.drawContours(original_img, [paper_contour], -1, (0, 255, 0), 3) # こちらにも描画
    axes[0].imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    axes[0].set_title('① 紙の検出結果 (緑の線)')
    axes[0].axis('off')

    # ヒートマップ重ね合わせ画像
    axes[1].imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
    axes[1].set_title('② 照度ヒートマップ (赤:明るい, 青:暗い)')
    axes[1].axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


# --- ここから実行 ---
if __name__ == '__main__':
    # ↓↓↓ ここに分析したい画像のパスを指定してください ↓↓↓
    image_file_path = 'path/to/your/image.jpg' 
    
    # 上記で指定した画像で分析を実行
    analyze_illumination(image_file_path)
