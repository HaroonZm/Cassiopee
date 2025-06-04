import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
a = list(map(int,input().split()))
b = list(map(int,input().split()))

visited = [False]*N
res = 0

def dfs(u):
    global res
    visited[u] = True
    diff = b[u] - a[u]
    for v in g[u]:
        if not visited[v]:
            child_diff = dfs(v)
            diff += child_diff
    res += abs(diff)
    return diff

dfs(0)
print(res)