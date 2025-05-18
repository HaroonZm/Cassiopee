import sys
input = sys.stdin.readline
from collections import deque, Counter

N = int(input())
X = [[] for i in range(N)]
L = [0]*N
for i in range(N-1):
    x, y = map(int, input().split())
    X[x-1].append(y-1)
    X[y-1].append(x-1)
    L[x-1] += 1
    L[y-1] += 1

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

C = Counter(P)
##### Settings
unit = 0
merge = lambda a, b: a + b
adj_bu = lambda a, i: (a+1)/C[P[i]]
adj_td = lambda a, i, p: ((XX[p]*L[p]-XX[i]*C[p])/max(1,L[p]-1)+1)/max(1,C[i])
adj_fin = lambda a, i: a*max(1,C[i])/L[i]
#####

ME = [unit] * N
XX = [0] * N
TD = [unit] * N
for i in R[1:][::-1]:
    XX[i] = adj_bu(ME[i], i)
    p = P[i]
    ME[p] = merge(ME[p], XX[i])
XX[R[0]] = adj_fin(ME[R[0]], R[0])

for i in R:
    ac = unit
    for j in reversed(X[i]):
        TD[j] = adj_td(merge(TD[j], ac), j, i)
        ac = merge(ac, XX[j])
        XX[j] = adj_fin(merge(ME[j], TD[j]), j)

print(*XX, sep = "\n")