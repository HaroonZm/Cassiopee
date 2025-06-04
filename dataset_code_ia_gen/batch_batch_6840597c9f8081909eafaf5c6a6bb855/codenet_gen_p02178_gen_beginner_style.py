import sys
sys.setrecursionlimit(10**7)

N, T, S, E = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

# 初心者らしい単純なDFSでSからEへのすべての経路を探索し、
# 最小の訪問数(=頂点数)を求める
visited = [False]*(N+1)
res = -1

def dfs(v, depth):
    global res
    if v == E:
        if res == -1 or res > depth:
            res = depth
        return
    visited[v] = True
    for nv, w in edges[v]:
        # 魔力で減る耐久度の総和は到達した島の訪問回数×T,
        # 到達した島の数はdepth(=訪問した島の数)
        # 一番橋の耐久度が低い橋が壊れないことが必要なので、
        # その橋の耐久度 >= T * depth
        if not visited[nv] and w >= T * depth:
            dfs(nv, depth+1)
    visited[v] = False

dfs(S, 1)

if res == -1:
    print("No")
else:
    print("Yes")