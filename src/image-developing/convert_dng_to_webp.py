#!/usr/bin/env python3
"""
DNGファイルをWebP形式に一括変換するスクリプト
VueScanでスキャンしたDNGファイルを処理します
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional


def check_imagemagick() -> bool:
    """ImageMagickがインストールされているか確認"""
    try:
        result = subprocess.run(
            ['convert', '-version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def convert_dng_to_webp(
    input_file: Path,
    output_file: Path,
    quality: int = 85,
    icc_profile: Optional[str] = None
) -> bool:
    """
    DNGファイルをWebPに変換
    
    Args:
        input_file: 入力DNGファイルのパス
        output_file: 出力WebPファイルのパス
        quality: WebPの品質（0-100、デフォルト85）
        icc_profile: ICCプロファイルのパス（オプション）
    
    Returns:
        変換が成功した場合True
    """
    try:
        # ImageMagickのconvertコマンドを構築
        cmd = ['convert']
        
        # ICCプロファイルを適用（指定されている場合）
        if icc_profile and os.path.exists(icc_profile):
            cmd.extend(['-profile', icc_profile])
        
        # DNGファイルを読み込み
        cmd.append(str(input_file))
        
        # WebP形式で出力
        # -quality: WebPの品質
        # -define webp:lossless=false: 可逆圧縮を無効化（ファイルサイズを小さく）
        # -define webp:method=6: 圧縮方法（0-6、6が最高品質だが遅い）
        cmd.extend([
            '-quality', str(quality),
            '-define', 'webp:lossless=false',
            '-define', 'webp:method=6',
            str(output_file)
        ])
        
        # 変換実行
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5分のタイムアウト
        )
        
        if result.returncode != 0:
            print(f"エラー: {input_file.name} の変換に失敗しました")
            print(f"  エラーメッセージ: {result.stderr}")
            return False
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"タイムアウト: {input_file.name} の変換が時間切れになりました")
        return False
    except Exception as e:
        print(f"エラー: {input_file.name} の変換中に例外が発生しました: {e}")
        return False


def find_dng_files(directory: Path) -> List[Path]:
    """指定ディレクトリ内のDNGファイルを検索"""
    dng_files = list(directory.glob("*.dng"))
    dng_files.extend(directory.glob("*.DNG"))
    return sorted(dng_files)


def main():
    # 設定
    input_dir = Path("/Users/fukudakazufumi/Pictures/VueScan/ポスプロ作業_beta")
    output_dir = input_dir / "webp_output"  # 出力先ディレクトリ
    
    # photo.iniからICCプロファイルのパスを取得（オプション）
    icc_profile = "/Users/fukudakazufumi/Pictures/VueScan/icc_profile/DS-50000.icc"
    
    # WebPの品質設定（0-100、高いほど品質が良いがファイルサイズが大きい）
    webp_quality = 85
    
    # ImageMagickの確認
    if not check_imagemagick():
        print("エラー: ImageMagickがインストールされていません")
        print("インストール方法: brew install imagemagick")
        sys.exit(1)
    
    # 入力ディレクトリの確認
    if not input_dir.exists():
        print(f"エラー: 入力ディレクトリが見つかりません: {input_dir}")
        sys.exit(1)
    
    # 出力ディレクトリの作成
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # DNGファイルを検索
    dng_files = find_dng_files(input_dir)
    
    if not dng_files:
        print(f"警告: {input_dir} にDNGファイルが見つかりませんでした")
        sys.exit(0)
    
    print(f"見つかったDNGファイル: {len(dng_files)} 件")
    print(f"出力先: {output_dir}")
    print(f"WebP品質: {webp_quality}")
    print("-" * 60)
    
    # 変換処理
    success_count = 0
    fail_count = 0
    
    for i, dng_file in enumerate(dng_files, 1):
        # 出力ファイル名（拡張子を.webpに変更）
        output_file = output_dir / f"{dng_file.stem}.webp"
        
        # 既に存在する場合はスキップ
        if output_file.exists():
            print(f"[{i}/{len(dng_files)}] スキップ: {dng_file.name} (既に存在)")
            continue
        
        print(f"[{i}/{len(dng_files)}] 変換中: {dng_file.name} -> {output_file.name}")
        
        # 変換実行
        if convert_dng_to_webp(dng_file, output_file, webp_quality, icc_profile):
            success_count += 1
            # ファイルサイズを表示
            input_size = dng_file.stat().st_size / (1024 * 1024)  # MB
            output_size = output_file.stat().st_size / (1024 * 1024)  # MB
            compression_ratio = (1 - output_size / input_size) * 100
            print(f"  成功: {input_size:.2f}MB -> {output_size:.2f}MB ({compression_ratio:.1f}% 圧縮)")
        else:
            fail_count += 1
    
    # 結果サマリー
    print("-" * 60)
    print(f"変換完了: 成功 {success_count} 件, 失敗 {fail_count} 件")
    print(f"出力先: {output_dir}")


if __name__ == "__main__":
    main()
