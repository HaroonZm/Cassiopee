while True:
    t = int(input())
    if t == 0:
        break  # 入力終了
    n = int(input())
    total_study_time = 0  # 総勉強時間の初期化
    for _ in range(n):
        s, f = map(int, input().split())
        # 開始時刻から終了時刻の間の時間を加算
        total_study_time += (f - s)
    # 目標時間と比較して判定
    if total_study_time >= t:
        print("OK")
    else:
        print(t - total_study_time)  # 足りない時間を出力