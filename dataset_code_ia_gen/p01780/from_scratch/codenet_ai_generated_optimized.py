import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())
parents = [0] + list(map(int, sys.stdin.readline().split())) if n > 1 else [0]

adj = [[] for _ in range(n+1)]
for i in range(2, n+1):
    adj[parents[i-1]].append(i)
for i in range(1, n+1):
    adj[i].sort()

size = [0]*(n+1)
total = 0
def dfs(u):
    global total
    size[u] = 1
    for v in adj[u]:
        dfs(v)
        total += 2*size[v]
        size[u] += size[v]

dfs(1)
print(total)