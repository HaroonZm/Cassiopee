import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
data = list(map(int,read().split()))
A = data[:N+N-2:2]
B = data[1:N+N-2:2]
INF = 10 ** 18 + 100
S = [INF] + data[-N:]

graph = [[] for _ in range(N+1)]
for a,b in zip(A,B):
    graph[a].append(b)
    graph[b].append(a)

root = S.index(min(S))
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

subtree_size = [1] * (N+1)
for v in reversed(order):
    subtree_size[parent[v]] += subtree_size[v]

length = [0] * (N+1)
for v,p in zip(A,B):
    if parent[p] == v:
        v,p = p,v
    s = subtree_size[v]
    d = N - s - s
    length[v] = 0 if d == 0 else(S[v] - S[p]) // d

# 重心間以外は決まった。いったん、重心間を 0 として計算

dist = [0] * (N+1)
for v in order[1:]:
    p = parent[v]
    dist[v] = dist[p] + length[v]

d_root = sum(dist)
x = (S[root] - d_root) * 2 // N
answer = []
for v,p in zip(A,B):
    if parent[p] == v:
        v,p = p,v
    if length[v] == 0:
        length[v] = x
    answer.append(length[v])

print('\n'.join(map(str,answer)))