N, K = map(int, input().split())
P = list(map(int, input().split()))
if K == N:
    print(1)
    exit()
cum_asc = [0]
for i in range(N-1):
    cum_asc.append(cum_asc[-1] + int(P[i] < P[i+1]))
all_asc = []
for i in range(N-K+1):
    all_asc.append(cum_asc[i+K-1] - cum_asc[i] == K-1)
from collections import deque
sldmin = []
sldmax = []
qmin = deque()
qmax = deque()
for i in range(N):
    p = P[i]
    while qmin and qmin[-1] > p:
        qmin.pop()
    qmin.append(p)
    if i-K-1 >= 0 and P[i-K-1] == qmin[0]:
        qmin.popleft()
    while qmax and qmax[-1] < p:
        qmax.pop()
    qmax.append(p)
    if i-K-1 >= 0 and P[i-K-1] == qmax[0]:
        qmax.popleft()
    if i >= K:
        sldmin.append(qmin[0])
        sldmax.append(qmax[0])
parent = list(range(N-K+2))
rank = [0] * (N-K+2)
count = 0
def root(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def unite(a, b):
    global count
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    count += 1
def components():
    return len(parent) - count
for i in range(N-K+1):
    l = P[i]
    r = P[i+K]
    mn = sldmin[i]
    mx = sldmax[i]
    if l == mn and r == mx:
        unite(i, i+1)
if all(f == False for f in all_asc):
    print(components() - 1)
    exit()
def_i = N-K+1
for i in range(N-K+1):
    if all_asc[i]:
        unite(i, def_i)
print(components())