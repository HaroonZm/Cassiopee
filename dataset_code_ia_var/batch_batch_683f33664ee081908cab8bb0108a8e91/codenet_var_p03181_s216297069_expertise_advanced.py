import sys
from collections import deque
from operator import mul

sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline

N, M = map(int, input().split())
X = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    X[x].append(y)
    X[y].append(x)

P = [-1] * N
Q = deque([0])
R = []
while Q:
    u = Q.popleft()
    R.append(u)
    for v in X[u][:]:
        if v != P[u]:
            P[v] = u
            X[v].remove(u)
            Q.append(v)

unit = 1
def merge(a, b, m): return a * b % m
def adj_bu(a, i):   return a + 1
def adj_td(a, i):   return a + 1

ME = [unit] * N
XX = [0] * N
TD = [unit] * N

for i in reversed(R[1:]):
    XX[i] = adj_bu(ME[i], i)
    p = P[i]
    ME[p] = merge(ME[p], XX[i], M)
XX[R[0]] = adj_bu(ME[R[0]], R[0])

for i in R:
    ac = TD[i]
    for j in X[i]:
        TD[j] = ac
        ac = merge(ac, XX[j], M)
    ac = unit
    for j in reversed(X[i]):
        TD[j] = adj_td(merge(TD[j], ac, M), i)
        ac = merge(ac, XX[j], M)
        XX[j] = adj_bu(merge(ME[j], TD[j], M), j)

print(*(x - 1 for x in XX), sep='\n')