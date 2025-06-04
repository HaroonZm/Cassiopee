import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R = map(int, input().split())
t = [0]*(N+1)
e = [0]*(N+1)
for i in range(1, N+1):
    ti, ei = map(int, input().split())
    t[i] = ti
    e[i] = ei

# 差分制約のグラフを作る（辺は b -> a が c を示す）
# 制約: x_a - x_b <= c なので、b -> a に重み c の辺を張る
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

# 目的：各 x_i(利用回数)は 0 <= x_i <= t_i
# 差分制約を満たしつつ、sum e_i*x_i を最大化する
# e_i >= 0 なので x_i をできるだけ大きくすることがよい

# 差分制約を考慮すると、x_j >= x_i - c の関係がある（経路制約）
# 最大化のために x_i をできるだけ大きくできる値の上限を求める必要がある
# 差分制約は最大値の上限を制限するので、x_i <= t_i の範囲内で、
# x_i <= x_j + c の制約で各 i の最大値を決定する

# 制約を満たす最大値を決めるには、逆辺からの最短距離を求めて、
# x_i <= t_i かつ x_i - x_j <= c を満たす最大値を見つける（差分制約最大値問題）
# 差分制約を用いて最大値制約を付ける変数に 対し SPFA / Bellman-Ford を行う

# 0を起点とした差分約束問題の形に変換し、x_i <= t_i 制約も追加
# i番ノードに「x_0 - x_i <= -min値(0)」などの制約は、0 <= x_i <= t_iとして扱う
# 最大値問題のため x_i は t_i 以下だから、x_i <= t_i は制約
# x_i >= 0 なので x_i - x_0 >= 0 => x_0 - x_i <= 0 と考える
# 上の問題を扱いやすくするために「0番ノード」を追加し、
# x_0 = 0 に固定する。x_i は上限 t_i 下限0の範囲内

# 各変数 x_i の上限制約 x_i <= t_i は、x_i - x_0 <= t_i (0を原点)
# よって辺: 0->i 重み t_i を追加
# 下限制約 0 <= x_i は x_0 - x_i <= 0 に対応し、辺: i->0 重み 0 を追加

graph[0] = []
for i in range(1, N+1):
    graph[0].append((i, t[i]))
for i in range(1, N+1):
    graph[i].append((0, 0))

# 差分制約問題で最大 x_i を決めるために、
# x_i を表す距離 dist[i] := x_i の最大値を表す

# Bellman-Fordで最長距離を求めるが負閉路がないことが保証されているのでOK
dist = [-10**15] * (N+1)
dist[0] = 0

from collections import deque

def spfa():
    q = deque([0])
    inqueue = [False]*(N+1)
    inqueue[0] = True
    while q:
        u = q.popleft()
        inqueue[u] = False
        for v, w in graph[u]:
            if dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                if not inqueue[v]:
                    inqueue[v] = True
                    q.append(v)

spfa()

# dist[i] は x_i の最大値の候補だが、0<=x_i<=t_iで制約しているので
# dist[i] が負になることはない(0<=x_iであるから)、また dist[i] <= t_i になっているか確認
# 何らかの理由で dist[i] > t_i になっても、t[i]が上限なので t[i]に制限する
for i in range(1, N+1):
    if dist[i] > t[i]:
        dist[i] = t[i]
    if dist[i] < 0:
        dist[i] = 0

ans = 0
for i in range(1, N+1):
    ans += dist[i]*e[i]

print(ans)