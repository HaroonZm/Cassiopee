# 初めに、血液型ごとの人数をカウントするための辞書を用意します。
# 入力は複数行で与えられるため、標準入力から EOF（Ctrl+DまたはCtrl+Z）まで読み取ります。
# 各行は「出席番号,血液型」という形式なので、カンマで分割して血液型を取得し、辞書内の該当カウントを増やします。
# 最後に指定された順番（A, B, AB, O）で人数を出力します。

import sys

# 血液型ごとの人数カウントを保存する辞書
blood_type_counts = {
    "A": 0,
    "B": 0,
    "AB": 0,
    "O": 0
}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # 空行があれば無視
    # 出席番号,血液型 の形式で分割
    parts = line.split(",")
    if len(parts) != 2:
        continue  # フォーマットが違う行は無視
    # 出席番号と血液型
    student_number_str, blood_type = parts
    # 出席番号の検証（1～50の整数）
    try:
        student_number = int(student_number_str)
        if not (1 <= student_number <= 50):
            continue  # 範囲外の番号は無視
    except ValueError:
        continue  # 整数変換できなければ無視

    # 血液型が正しいかチェックし、カウントアップ
    if blood_type in blood_type_counts:
        blood_type_counts[blood_type] += 1

# 指定された順序で出力
print(blood_type_counts["A"])
print(blood_type_counts["B"])
print(blood_type_counts["AB"])
print(blood_type_counts["O"])