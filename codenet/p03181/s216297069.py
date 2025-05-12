import sys
input = sys.stdin.readline
from collections import deque
 
N, M = map(int, input().split())
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    X[x-1].append(y-1)
    X[y-1].append(x-1)

P = [-1] * N
Q = deque([0])
R = []
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            deque.append(Q, a)

##### Settings
unit = 1
merge = lambda a, b, m: a * b % m
adj_bu = lambda a, i: a + 1
adj_td = lambda a, i: a + 1
#####

ME = [unit] * N
XX = [0] * N
TD = [unit] * N
for i in R[1:][::-1]:
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
    for j in X[i][::-1]:
        TD[j] = adj_td(merge(TD[j], ac, M), i)
        ac = merge(ac, XX[j], M)
        XX[j] = adj_bu(merge(ME[j], TD[j], M), j)

print(*[x - 1 for x in XX], sep = "\n")