from PIL import Image
from PIL.ExifTags import TAGS
import os
import csv
import datetime

# 画像フォルダのパス
IMAGE_DIR = r"\\192.168.0.19\luigi共有d\ゲームアーカイブ撮影バックアップ\撮影(2025)"

# 出力CSV
OUTPUT_CSV = "scanner_list.csv"

results = []

for root, dirs, files in os.walk(IMAGE_DIR):
    for filename in files:
        if not filename.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff", ".png","dng")):
            continue

        filepath = os.path.join(root, filename)

        try:
            img = Image.open(filepath)
            exif_data = img.getexif()

            make = model = software = ""
            date_taken = ""

            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == "Make":
                        make = str(value)
                    elif tag == "Model":
                        model = str(value)
                    elif tag == "Software":
                        software = str(value)
                    elif tag == "DateTimeOriginal":
                        date_taken = str(value)

            # EXIFが無い場合はファイル作成日時
            if not date_taken:
                ctime = os.path.getctime(filepath)
                dt = datetime.datetime.fromtimestamp(ctime)
                date_taken = dt.strftime("%Y/%m/%d")

            results.append([
                filepath,  
                make,
                model,
                software,
                date_taken
            ])

        except Exception as e:
            results.append([filepath, "ERROR", "", str(e), ""])

# CSV 出力
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow([
        "ファイルパス",
        "撮影機材メーカー名",
        "撮影機材名",
        "ソフトウェア",
        "スキャン日時"
    ])
    writer.writerows(results)

print("完了しました")