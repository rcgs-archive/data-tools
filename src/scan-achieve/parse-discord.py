import re
import pandas as pd
import sys
from datetime import datetime, timedelta
from pathlib import Path

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
    # 現在のコンテキスト（日付・報告者）を保持する変数
    current_date = None
    current_person = None
    current_year = datetime.now().year

    # 行ごとに処理
    lines = text.strip().split('\n')

    # 正規表現パターン
    # 発言ヘッダ: 名前 — 2026/09/15 18:02 / 名前 — 昨日 17:58
    re_header = re.compile(
        r'^(.+?)\s*[—–\-]\s*(?:(\d{4})/(\d{1,2})/(\d{1,2})|昨日)\s+\d{1,2}:\d{1,2}\s*$'
    )
    # 日時だけの行: 2025/10/13 17:52
    re_timestamp = re.compile(r'(\d{4})/(\d{1,2})/(\d{1,2}) \d{1,2}:\d{1,2}')
    # 相対日時: 昨日 18:49
    re_relative = re.compile(r'昨日 \d{1,2}:\d{1,2}')

    # 報告行: 作業時間PT2H30M、作業完了25資料26ページ
    # H/h、M/m、分、PT30分 のように時間だけの表記にも対応
    re_report = re.compile(
        r'作業時間\s*(?:PT)?(?:(\d+)\s*[hH])?(?:(\d+)\s*(?:[mM]|分))?.*?(\d+)資料(\d+)ページ'
    )

    # 日付指定の抽出: （11/4日のぶん）
    re_date_override = re.compile(r'（(\d{1,2})/(\d{1,2})')

    # 「昨日」はスクリプト実行日の前日
    yesterday_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

    for line in lines:
        line = line.strip()

        # 1. 発言ヘッダ（報告者＋日時）かチェック
        match_header = re_header.match(line)
        if match_header:
            current_person = match_header.group(1).strip()
            if match_header.group(2):
                current_year = int(match_header.group(2))
                current_date = datetime(
                    current_year, int(match_header.group(3)), int(match_header.group(4))
                )
            else:
                current_date = yesterday_date
            continue

        match_ts = re_timestamp.search(line)
        if match_ts:
            current_year = int(match_ts.group(1))
            current_date = datetime(current_year, int(match_ts.group(2)), int(match_ts.group(3)))
            continue

        if re_relative.search(line):
            current_date = yesterday_date
            continue

        # 2. 報告の行かチェック
        match_rep = re_report.search(line)
        if match_rep:
            hours = int(match_rep.group(1)) if match_rep.group(1) else 0
            minutes = int(match_rep.group(2)) if match_rep.group(2) else 0
            docs = int(match_rep.group(3))
            pages = int(match_rep.group(4))

            duration_hours = hours + (minutes / 60.0)

            effective_date = current_date
            match_ovr = re_date_override.search(line)
            if match_ovr:
                month = int(match_ovr.group(1))
                day = int(match_ovr.group(2))
                effective_date = datetime(current_year, month, day)

            if effective_date:
                # デジカメ撮影はスキャナ作業と分けて管理する
                kind = 'digicam' if 'デジカメ' in line else 'scanner'
                data.append({
                    'Date': effective_date.strftime('%Y-%m-%d'),
                    'Person': current_person or '不明',
                    'Kind': kind,
                    'Duration_Hours': duration_hours,
                    'Documents': docs,
                    'Pages': pages
                })

    return pd.DataFrame(data)


def summarize(df, group_cols):
    columns = ['Duration_Hours', 'Documents', 'Pages', 'Pages_Per_Hour']
    if df.empty:
        return pd.DataFrame(columns=columns)
    stats = df.groupby(group_cols, dropna=False)[['Duration_Hours', 'Documents', 'Pages']].sum()
    hours = stats['Duration_Hours']
    stats['Pages_Per_Hour'] = (stats['Pages'] / hours.where(hours > 0)).round(1)
    stats['Duration_Hours'] = stats['Duration_Hours'].round(2)
    return stats


def print_summary(title, df, daily_stats):
    print(f"=== {title} ===")
    if df.empty:
        print("該当なし")
        return
    print(daily_stats)
    print(f"総ページ数: {int(df['Pages'].sum())}")
    print(f"総資料数: {int(df['Documents'].sum())}")
    print(f"総作業時間: {df['Duration_Hours'].sum():.2f} 時間")
    print()


# データ解析
df = parse_scan_report(raw_text)
scanner_df = df[df['Kind'] == 'scanner'] if not df.empty else df
digicam_df = df[df['Kind'] == 'digicam'] if not df.empty else df

scanner_daily = summarize(scanner_df, ['Date'])
digicam_daily = summarize(digicam_df, ['Date'])
# スキャナとデジカメはページ/時間が大きく違うので、人×種別で生産性を出す
by_person = summarize(df, ['Person', 'Kind'])
if not by_person.empty:
    by_person = by_person.sort_values(['Kind', 'Pages_Per_Hour'], ascending=[True, False])

print_summary("スキャナ（日毎）", scanner_df, scanner_daily)
print_summary("デジカメ（日毎）", digicam_df, digicam_daily)
print_summary("人ごと（種別別のページ/時間）", df, by_person)

input_path = Path(input_file)
out_dir = input_path.parent
scanner_path = out_dir / f"{input_path.stem}_scanner.csv"
digicam_path = out_dir / f"{input_path.stem}_digicam.csv"
person_path = out_dir / f"{input_path.stem}_by_person.csv"
scanner_daily.to_csv(scanner_path, encoding='utf-8-sig')
digicam_daily.to_csv(digicam_path, encoding='utf-8-sig')
by_person.to_csv(person_path, encoding='utf-8-sig')
print(f"出力: {scanner_path}")
print(f"出力: {digicam_path}")
print(f"出力: {person_path}")
