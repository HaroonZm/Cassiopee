# TSP的なやつ？たしか高校でなんとなく教えられたやつ
#（bit DP苦手なので練習がてら書いてみる）

# こういうページ見ながら実装してみました
# https://algo-logic.info/bit-dp/

# dp[S][v] := 頂点0から S の集合を通って v に来る最小コスト
# S は、どの頂点をもう使ったか（ビットで管理
# v = 今いるところ

INF = 2 ** 31  # 32bitくらいで足りるのかな
from itertools import product  # たしかこれで u-v 全探索できる...はず

def solve(n, graph):
    # n: 頂点の数
    # graph: 隣接行列のつもり（未連結も多分OK）
    sz = 1 << n  # 2^n通り
    dp = []
    for _ in range(sz):
        dp.append([INF] * n)   # 初期値がINF
    dp[0][0] = 0    # 0からスタートするので。
    for S in range(sz):
        # 全部の部分集合、でも S==0...2^n-1
        for u in range(n):
            for v in range(n):
                if (S >> v) & 1:
                    # vが集合Sに含まれてたらスキップ
                    continue
                nxt = S | (1 << v)
                maybe = dp[S][u] + graph[u][v]
                if dp[nxt][v] > maybe:
                    # こっちのが小さいパターン
                    dp[nxt][v] = maybe
                # else:  # まぁ、何もしないとき
    ans = dp[sz - 1][0]  # 最後に0に戻ってこれるか？
    # print(dp)  # debug用
    if ans == INF:
        print(-1) # たしかダメなときは -1
    else:
        print(ans)

# 入力例
# n = 4
# graph = [
#     [INF, 2, 9, INF],
#     [1, INF, 6, 4],
#     [INF, 7, INF, 8],
#     [6, 3, INF, INF]
# ]
# solve(n, graph)


# AOJの入力向け、ちょっと面倒なのでバグってるかも
n, e = map(int, input().split())
graph = [[INF for _ in range(n)] for __ in range(n)]
for _ in range(e):
    s, t, d = map(int, input().split())
    graph[s][t] = d              # 有向なのでこっちだけ
solve(n, graph)