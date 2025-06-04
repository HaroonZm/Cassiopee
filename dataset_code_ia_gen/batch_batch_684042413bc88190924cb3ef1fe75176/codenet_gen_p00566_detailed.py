# 問題の要約：
# H本の東西道路(北から1〜H本目)、W本の南北道路(西から1〜W本目)がある。
# 各交差点(i,j)に住んでいる人数A[i][j]が与えられる。
# H本の道路から1本、W本の道路から1本、合計2本の幹線道路を選ぶ。
# 住人全員に対して「最寄りの交差点から近い方の幹線道路までの距離」の総和の最小値を求める。

# 考え方：
# - 2本の幹線道路は、東西方向から1本、南北方向から1本選ぶ。
# - 東西方向の幹線道路は北から選択
# - 南北方向の幹線道路は西から選択
# - 交差点(i,j)に対し、
#   幹線道路までの距離は min(|i - selected_row|, |j - selected_col|)
# - すべての交差点の住民数A[i][j]に対して、その距離をかけて合計を求める
# - 全ての選択肢に対して総和を計算し、最小のものを答える

# HとWは最大で25なので全探索可能
# 時間計算量は O(H*W*H*W) = 25*25*25*25= 約39万程度で十分高速


# 実装：

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_distance_sum = float('inf')

# 北からの道路の一つを選ぶ
for selected_row in range(H):
    # 西からの道路の一つを選ぶ
    for selected_col in range(W):
        total_distance = 0
        for i in range(H):
            for j in range(W):
                # 住人数
                population = A[i][j]
                # 距離は交差点(i,j)と選んだ幹線道路までの距離の最小値
                distance = min(abs(i - selected_row), abs(j - selected_col))
                total_distance += distance * population
        if total_distance < min_distance_sum:
            min_distance_sum = total_distance

print(min_distance_sum)