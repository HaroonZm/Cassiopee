W = int(input())
a = list(map(int, input().split()))

# 出口のユニットのインデックスを集める
exits = [i for i, v in enumerate(a) if v == 0]

if not exits:
    # 出口がない場合は0を出力
    print(0)
    exit()

max_time = 100000 + 10000  # 十分大きい時間の上限を設定
# dp[t][i]: 時刻tにユニットiにいる人の数（存在可能な場合）
# メモリ制限を考慮し、各時刻ごとに状態を更新していく
# 今回は単純で遅い解法なので計算量やメモリは無視する

# ここでは各時刻に何人がどこにいるかを辞書で管理する
from collections import defaultdict

# 初期状態: t=0にa[i]>0のユニットに人数がいる
# 各入り口ユニット i は時刻0〜a[i]-1に1人ずつ発生し、
# その人はt+1から移動開始

# 状態は時刻ごとに場所ごとに人数を持つ辞書で管理
people = defaultdict(int)  # {(time, unit): number_of_people}

# 入り口からの人の出現を登録
max_appearance_time = 0
for i, v in enumerate(a):
    if v > 0:
        for t in range(v):
            people[(t, i)] += 1
            if t > max_appearance_time:
                max_appearance_time = t

# 防火扉の情報を記録
fire_door_close_time = {}
for i, v in enumerate(a):
    if v < 0:
        fire_door_close_time[i] = abs(v)

# 各時刻 t から t+1 への遷移を計算
# 最大時刻は max_appearance_time + W くらいとする
max_sim_time = max_appearance_time + W + 10
# 時刻ごとの状態を持つ配列を用意しないで、辞書だけで進める

for t in range(max_sim_time):
    # (t,i) にいる人を次の時刻に移す
    # ただし、(t+1)が防火扉閉鎖以降ならそのユニットには入れない
    new_people = defaultdict(int)
    for (time, unit), num in people.items():
        if time != t:
            continue
        # 時刻 t の unit に num 人いる
        # 1人の人は i-1, i, i+1 に移動可能（範囲内かつ防火扉閉鎖時間を超えてないこと）
        if unit in fire_door_close_time and t >= fire_door_close_time[unit]:
            # このユニットに閉鎖以降なら人は動けない→閉じ込められる
            # ここでは移動しない＝消える扱いでよい（救出不可）
            continue
        for nxt in [unit - 1, unit, unit + 1]:
            if 0 <= nxt < W:
                if nxt in fire_door_close_time and (t + 1) >= fire_door_close_time[nxt]:
                    continue
                new_people[(t + 1, nxt)] += num
    # 入り口から新たに出現した人も加える
    for i, v in enumerate(a):
        if v > 0 and t + 1 < v:
            new_people[(t + 1, i)] += 1
    # 次の時刻へ更新
    for key, val in new_people.items():
        people[key] += val

# 最終的に出口ユニットに到達した人数の合計を数える
result = 0
for (time, unit), num in people.items():
    if unit in exits:
        # 防火扉で閉鎖されていなければカウント
        if unit in fire_door_close_time and time >= fire_door_close_time[unit]:
            continue
        result += num

print(result)