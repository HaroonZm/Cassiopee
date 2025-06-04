# マヤ長期暦と西暦の相互変換プログラム

# 0.0.0.0.0 (マヤ) = 2012.12.21 (西暦) として基準日を決め、
# そこからの日数差で変換を行う。
# マヤ暦の各単位の日数を計算し、
# 西暦の日付処理ではうるう年や月の日数を考慮する。

import sys

# マヤ暦各単位の日数換算
KIN = 1
WINAL = 20 * KIN
TUN = 18 * WINAL
KATUN = 20 * TUN
BAKTUN = 20 * KATUN

# マヤ暦の最大日数（12.19.19.17.19）
MAX_MAYA_DAYS = (12 * BAKTUN +
                 19 * KATUN +
                 19 * TUN +
                 17 * WINAL +
                 19 * KIN)

# 基準日：2012年12月21日を「0.0.0.0.0」とする
# まずは 西暦の日付から通算日を計算し、
# 基準日の通算日との差がマヤ暦の日数になる

def is_leap_year(y):
    # 西暦におけるうるう年の判定
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_month(y, m):
    # 月ごとの日数
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif m in (4, 6, 9, 11):
        return 30
    elif m == 2:
        return 29 if is_leap_year(y) else 28
    else:
        return 0  # 異常値

def ymd_to_ordinal(y, m, d):
    # 基準日を西暦2012年12月21日に設定し、
    # 1年1月1日からの通算日数を計算する代わりに
    # 2012.12.21 の通算日を計算しておくことで、
    # y.m.d の通算日と基準日の差分をとる仕組み
    # まずは西暦1年1月1日からの日数を数える

    # y年1月1日からの通算日
    days = 0
    for year in range(1, y):
        days += 366 if is_leap_year(year) else 365

    # y年の1月1日からm月d日までの日数
    for month in range(1, m):
        days += days_in_month(y, month)
    days += d

    return days

# 基準日（2012.12.21）を通算日で取得
BASE_YEAR = 2012
BASE_MONTH = 12
BASE_DAY = 21
BASE_ORDINAL = ymd_to_ordinal(BASE_YEAR, BASE_MONTH, BASE_DAY)

def mayan_to_days(b, ka, t, w, ki):
    # マヤ暦から日数へ変換
    return b * BAKTUN + ka * KATUN + t * TUN + w * WINAL + ki

def days_to_mayan(days):
    # 日数からマヤ暦に変換
    # daysは0以上であることを想定(マヤ暦基準日の0.0.0.0.0が0日)
    b = days // BAKTUN
    days %= BAKTUN
    ka = days // KATUN
    days %= KATUN
    t = days // TUN
    days %= TUN
    w = days // WINAL
    ki = days % WINAL
    return b, ka, t, w, ki

def days_to_ymd(days):
    # days は 2012.12.21 からの差分
    # それに基準日の通算日を足して、西暦 y.m.d に逆変換
    target_ordinal = BASE_ORDINAL + days

    # 西暦1.1.1からの通算日 target_ordinal を
    # 西暦 y,m,d に変換
    # 2012年から大きく離れるので高速化は必要？
    # 最大年10000000なので単純に1年ずつ足す実装はNG
    # バイナリサーチで年を特定するアプローチを取る

    # 年を推定（西暦1年～最大10000000年）
    low = 1
    high = 10_000_000
    while low < high:
        mid = (low + high) // 2
        # mid年の1月1日までの通算日数
        mid_ordinal = ymd_to_ordinal(mid, 1, 1)
        if mid_ordinal <= target_ordinal:
            low = mid + 1
        else:
            high = mid
    y = low - 1

    # y年の1月1日までの通算日数
    y_start = ymd_to_ordinal(y, 1, 1)
    rem = target_ordinal - y_start

    # 月日を求める
    m = 1
    while True:
        dim = days_in_month(y, m)
        if rem <= dim:
            d = rem
            break
        rem -= dim
        m += 1

    return y, m, d

def parse_mayan_date(s):
    # 形式: b.ka.t.w.ki
    parts = s.split('.')
    if len(parts) != 5:
        return None
    try:
        b, ka, t, w, ki = map(int, parts)
        if not (0 <= b < 13):
            return None
        if not (0 <= ka < 20):
            return None
        if not (0 <= t < 20):
            return None
        if not (0 <= w < 18):
            return None
        if not (0 <= ki < 20):
            return None
        # 範囲内かもチェック
        total_days = mayan_to_days(b, ka, t, w, ki)
        if total_days > MAX_MAYA_DAYS:
            # 範囲外も許可されているが範囲外のマヤはないはず（0~12.19.19.17.19）
            # ただし問題文は範囲外のマヤはありうると示唆あり（次のサイクル）
            # とりあえず許容
            pass
        return b, ka, t, w, ki
    except:
        return None

def parse_gregorian_date(s):
    # 形式: y.m.d
    parts = s.split('.')
    if len(parts) != 3:
        return None
    try:
        y, m, d = map(int, parts)
        if not (2012 <= y <= 10_000_000):
            return None
        if not (1 <= m <= 12):
            return None
        dim = days_in_month(y, m)
        if not (1 <= d <= dim):
            return None
        return y, m, d
    except:
        return None

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        # マヤ暦か西暦か判定し、相互変換
        mayan = parse_mayan_date(line)
        if mayan is not None:
            # マヤ暦 -> 西暦
            # 0.0.0.0.0が2012.12.21に対応
            day_count = mayan_to_days(*mayan)
            # 基準日からの日数差なので
            # 西暦 = 基準日 + day_count日
            y, m, d = days_to_ymd(day_count)
            print(f"{y}.{m}.{d}")
            continue

        greg = parse_gregorian_date(line)
        if greg is not None:
            # 西暦 -> マヤ暦
            # 基準日のordinalとの差を計算しマヤに変換
            y, m, d = greg
            ordinal = ymd_to_ordinal(y, m, d)
            diff = ordinal - BASE_ORDINAL
            # 負の差が入らない範囲なのでそのまま変換可
            b, ka, t, w, ki = days_to_mayan(diff)
            print(f"{b}.{ka}.{t}.{w}.{ki}")
            continue

        # 不正な行は何もしない(問題文に明記なし)
        # ここではスルー
        # pass

if __name__ == "__main__":
    main()