N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    s, t = map(int, input().split())
    G[s].append(t)

ans = []
V = set()

def dfs(n):
    for e in G[n]:
        if e not in V:
            dfs(e)
    ans.append(n)
    V.add(n)

for i in range(N):
    if i not in V:
        if i not in V:
            dfs(i)
            print()

print(*ans[::-1], sep="\n")