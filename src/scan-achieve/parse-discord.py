import re
import pandas as pd
import sys
from datetime import datetime, timedelta

# コマンドライン引数からファイルパスを取得、またはデフォルトファイル名を使用
if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'discord_log.txt'  # デフォルトファイル名

try:
    # テキストファイルから読み込み
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
except FileNotFoundError:
    print(f"エラー: ファイル '{input_file}' が見つかりません。", file=sys.stderr)
    print(f"使用方法: python parse-discord.py [ファイルパス]", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"エラー: ファイルの読み込みに失敗しました: {e}", file=sys.stderr)
    sys.exit(1)

def parse_scan_report(text):
    data = []
    # 現在のコンテキスト（日付）を保持する変数
    current_date = None
    current_year = 2025 # ログの年
    
    # 行ごとに処理
    lines = text.strip().split('\n')
    
    # 正規表現パターン
    # 日時行: 2025/10/13 17:52
    re_timestamp = re.compile(r'(\d{4})/(\d{1,2})/(\d{1,2}) \d{1,2}:\d{1,2}')
    # 相対日時: 昨日 18:49
    re_relative = re.compile(r'昨日 \d{1,2}:\d{1,2}')
    
    # 報告行: 作業時間PT2H、撮影完了4資料70ページ (PT省略やHのみ、Mのみにも対応)
    re_report = re.compile(r'作業時間(PT)?(?:(\d+)H)?(?:(\d+)M)?.*?(\d+)資料(\d+)ページ')
    
    # 日付指定の抽出: （11/4日のぶん）
    re_date_override = re.compile(r'（(\d{1,2})/(\d{1,2})')

    # 「昨日」の計算用（本日の日付を2025/11/25と仮定）
    system_today = datetime(2025, 11, 25)
    yesterday_date = system_today - timedelta(days=1)

    for line in lines:
        line = line.strip()
        
        # 1. 日時の行かチェック
        match_ts = re_timestamp.match(line)
        if match_ts:
            current_date = datetime(int(match_ts.group(1)), int(match_ts.group(2)), int(match_ts.group(3)))
            continue
            
        match_rel = re_relative.match(line)
        if match_rel:
            current_date = yesterday_date
            continue
            
        # 2. 報告の行かチェック
        match_rep = re_report.search(line)
        if match_rep:
            # 時間、分、資料数、ページ数を取得
            hours = int(match_rep.group(2)) if match_rep.group(2) else 0
            minutes = int(match_rep.group(3)) if match_rep.group(3) else 0
            docs = int(match_rep.group(4))
            pages = int(match_rep.group(5))
            
            # 時間を数値（float）に変換
            duration_hours = hours + (minutes / 60.0)
            
            # 日付の決定（上書き指定があるか確認）
            effective_date = current_date
            match_ovr = re_date_override.search(line)
            if match_ovr:
                month = int(match_ovr.group(1))
                day = int(match_ovr.group(2))
                effective_date = datetime(current_year, month, day)
            
            if effective_date:
                data.append({
                    'Date': effective_date.strftime('%Y-%m-%d'),
                    'Duration_Hours': duration_hours,
                    'Documents': docs,
                    'Pages': pages
                })
    
    return pd.DataFrame(data)

# データ解析
df = parse_scan_report(raw_text)

# 日毎の集計
daily_stats = df.groupby('Date')[['Duration_Hours', 'Documents', 'Pages']].sum()
# 生産性（ページ/時間）の計算
daily_stats['Pages_Per_Hour'] = (daily_stats['Pages'] / daily_stats['Duration_Hours']).round(1)
daily_stats['Duration_Hours'] = daily_stats['Duration_Hours'].round(2)

print("=== 日毎の出来高と生産性 ===")
print(daily_stats)

print("\n=== 全期間合計 ===")
print(f"総ページ数: {df['Pages'].sum()}")
print(f"総資料数: {df['Documents'].sum()}")
print(f"総作業時間: {df['Duration_Hours'].sum():.2f} 時間")
