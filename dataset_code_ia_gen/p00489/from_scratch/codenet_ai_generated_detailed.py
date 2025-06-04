# JOIリーグのサッカー試合結果から各チームの順位を求めるプログラム

# アプローチ:
# 1. 各チームの勝ち点を格納するリストを用意する (インデックスはチーム番号-1に対応)。
# 2. 入力として与えられる試合結果をすべて読み込み、各試合について勝ち点を計算し、該当チームに加算する。
#    - チームAの得点 > チームBの得点ならチームAに3点、チームBに0点
#    - チームAの得点 < チームBの得点ならチームBに3点、チームAに0点
#    - 引き分けなら両方に1点ずつ付与
# 3. すべてのチームの勝ち点が計算できたら、
#    勝ち点が多い順に順位を決定する。
# 4. 勝ち点が同じチームは同順位とし、順位のスキップが発生する方式で処理する。
# 5. 元のチーム番号順に順位を出力する。

N = int(input())  # チーム数

# チームの勝ち点を0で初期化 (チーム番号1~Nなので0-based)
points = [0] * N

# 試合数は N*(N-1)//2
for _ in range(N*(N-1)//2):
    A, B, C, D = map(int, input().split())
    # インデックスは0から始まるので注意
    A_idx = A - 1
    B_idx = B - 1

    # 勝敗判定と勝ち点加算
    if C > D:
        points[A_idx] += 3
    elif C < D:
        points[B_idx] += 3
    else:
        points[A_idx] += 1
        points[B_idx] += 1

# 勝ち点とチーム番号のリストを作成
teams = [(points[i], i) for i in range(N)]

# 勝ち点降順でソート (勝ち点が多い順に並ぶ)
teams_sorted = sorted(teams, key=lambda x: x[0], reverse=True)

# 順位付け
# 勝ち点が同じなら同順位を付与し、スキップ処理を行う
ranks = [0] * N  # チーム番号順に順位を格納
current_rank = 1  # 現在付与している順位
prev_point = None
count_same_rank = 0  # 同じ順位のチーム数

for index, (pt, team_idx) in enumerate(teams_sorted):
    if pt != prev_point:
        # 新しい順位のチームが出たので順位を更新
        current_rank = index + 1
        prev_point = pt
    ranks[team_idx] = current_rank

# 出力: チーム番号の昇順で順位を出力
for r in ranks:
    print(r)