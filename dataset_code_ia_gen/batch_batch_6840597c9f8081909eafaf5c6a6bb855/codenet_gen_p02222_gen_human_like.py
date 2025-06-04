import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

# BFSで頂点0を根として各頂点の距離を求める
from collections import deque
dist = [-1]*N
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for nv in edges[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            q.append(nv)

max_dist = max(dist)

# 条件を整理すると：
# "距離がkの倍数の頂点同士は同じ色、倍数でなければ異なる色"
# これは距離をkで割った余りごとに色を分けることと同値
# したがってk <= 最大距離であればk通りの余りがあり、この条件は実現可能
# 逆にk > 最大距離なら、距離の余りは0のみで全て同じ色になってしまい、
# 距離がkの倍数でない頂点同士が異なる色になることは不可能になるか検証する

# しかし、距離がkの倍数でない任意の2頂点は異なる色、距離がkの倍数の頂点同士は同じ色
# のため、k=1のときはすべて距離0で同じ色だから可能（1色でよい）
# k > max_dist のときは条件を満たせるか考える
# k > max_distのときは、距離がkの倍数の距離0の頂点のみが同色で、
# 他はすべて異なる色で塗る必要がある。これは可能。
# よってすべてのkで可能でありそうに見えるが、そうとも限らない。

# 距離がkの倍数でない任意の2頂点が異なる色であるためには、
# 距離がkの倍数である頂点だけが同じ色、
# 他の頂点は別々の色でなくてはならない

# つまり、同じ距離dの頂点が二つ以上ある場合、
# k > 0でkがd1 - d2の最大公約数の約数のとき、kにより色分けが不可能になることがある

# 距離差の最大公約数(G) を求めると、
# kの倍数で等色となる条件を満たすためには、
# kはGの約数であれば色分け可能、それ以外は不可能

# よって解法は距離の差の最大公約数 (G) を求めること
# そしてkがGの約数なら1、そうでなければ0

from math import gcd

dist_sorted = sorted(dist)
g = 0
for i in range(1, N):
    g = gcd(g, dist_sorted[i] - dist_sorted[i-1])

res = []
for k in range(1, N+1):
    if g % k == 0:
        res.append('1')
    else:
        res.append('0')
print(''.join(res))