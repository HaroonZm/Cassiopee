import sys
input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))

N, M = inpl()

G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]

for i in range(M):
    a, b = inpl()
    G[a-1].append(b-1)
    rG[b-1].append(a-1)

def SCC(G, rG):
    N = len(G)
    def dfs(i):
        nonlocal t, rorder, searched
        searched[i] = True
        for j in G[i]:
            if not searched[j]:
                dfs(j)
        rorder[t] = i
        t += 1

    def rdfs(i):
        nonlocal t, group, g
        group[i] = g
        for j in rG[i]:
            if group[j] == -1:
                rdfs(j)

    t = 0
    rorder = [-1]*N
    searched = [0]*N
    group = [-1]*N

    for i in range(N):
        if not searched[i]:
            dfs(i)
    g = 0
    for i in range(N-1, -1, -1):
        if group[rorder[i]] == -1:
            rdfs(rorder[i])
            g += 1
    return group, g

group, g = SCC(G, rG)

ans = [[] for _ in range(g)]
for i in range(N):
    ans[group[i]].append(i+1)

for i in range(N):
    print(*ans[group[i]])