import sys
from collections import deque

sys.setrecursionlimit(100000)  # On met large, au cas où…

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    N_M_K = input().split()
    N = int(N_M_K[0])
    M = int(N_M_K[1])
    K = int(N_M_K[2])

    G = []
    for _ in range(N):
        G.append([])

    # Construction du graphe
    for i in range(M):
        x, y = map(int, input().split())
        G[x-1].append(y-1)
        G[y-1].append(x-1)

    degs = []
    for gs in G:
        degs.append(len(gs))

    # on va trier les indices selon le degré, du plus connecté au moins
    idxs = list(range(N))
    idxs.sort(key=lambda z: degs[z], reverse=True)

    INF = 1000000000

    def dfs(p, used, cnt):
        if p == N:
            return cnt

        v = idxs[p]
        mini = INF

        adj = []
        for j in G[v]:
            if used[j]:
                continue
            adj.append(j)

        # On tente de prendre tous les voisins (si ça passe côté K)
        if cnt+len(adj) <= K:
            # on marque voisins
            for j in adj:
                used[j] = 1

            nxt = p+1
            while nxt < N and used[idxs[nxt]]: nxt +=1
            r = dfs(nxt, used, cnt+len(adj))
            if r < mini:
                mini = r

            for j in adj:
                used[j] = 0 # "démarque"

        # sinon on essaye de prendre ce sommet direct ?
        if len(adj) > 1 and cnt+1 <= K:
            used[v] = 1
            nxt = p
            while nxt < N and used[idxs[nxt]]: nxt+=1
            r = dfs(nxt, used, cnt+1)
            if r < mini:
                mini = r
            used[v] = 0

        return mini

    ans = dfs(0, [0]*N, 0)
    if ans < INF:
        output(str(ans)+'\n')
    else:
        output('Impossible\n')

main()