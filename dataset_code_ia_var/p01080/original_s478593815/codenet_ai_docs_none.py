import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[x].append(y)
    edge[y].append(x)

topo = []
parent = [-1] * N
node = [0]
while node:
    s = node.pop()
    topo.append(s)
    for t in edge[s]:
        if t == parent[s]:
            continue
        parent[t] = s
        node.append(t)

memo = [0] * N
res = [0] * N
for s in reversed(topo):
    for t in edge[s]:
        if t == parent[s]:
            continue
        memo[s] = max(memo[s], res[t])
    res[s] = memo[s] + 1

TD = [0] * N
for s in topo:
    acc = TD[s]
    for t in edge[s]:
        if t == parent[s]:
            continue
        TD[t] = max(TD[t], acc)
        acc = max(acc, res[t])
    acc = 0
    for t in reversed(edge[s]):
        if t == parent[s]:
            continue
        TD[t] = max(TD[t], acc) + 1
        acc = max(acc, res[t])
        res[t] = max(memo[t], TD[t]) + 1

ans = [2 * (N - 1) - res[i] + 1 for i in range(N)]
print(*ans, sep="\n")