import sys
from collections import deque

def solve():
    reader = sys.stdin.readline
    writer = sys.stdout.write

    # On va prendre N, M et tous les V d'un seul coup
    tmp = reader().split()
    N = int(tmp[0])
    M = int(tmp[1])
    V = list(map(int, tmp[2:]))

    # Pour le graphe
    G = []
    for _ in range(N):
        G.append([])
    for _ in range(M):
        u, v = map(int, reader().split())
        G[u-1].append(v-1)

    # Multiplication de matrices booléennes
    def matmul(A, B):
        res = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                x = 0
                for k in range(N):
                    if A[i][k] & B[k][j]:
                        x = 1
                        break
                res[i][j] = x
        return res

    # Puissance rapide pour matrices
    def fast_pow(X, k):
        # Identité au début
        R = [[0]*N for nn in range(N)]
        for i in range(N): R[i][i] = 1
        while k > 0:
            if k%2 == 1:
                R = matmul(R, X)
            X = matmul(X, X)
            k //= 2
        return R

    V.sort()  # Bon on fait le tri, c’est sûrement utile
    ES = [[0]*N for _ in range(N)]
    for v in range(N):
        for w in G[v]:
            ES[v][w] = 1

    EE = []
    ds = []
    rgs = []
    # Je boucle sur les V...
    for ind, k in enumerate(V):
        d = [0]*N
        rg = [[] for _ in range(N)]
        ek = fast_pow(ES, k)
        EE.append(ek)
        for v in range(N):
            ts = ek[v]
            for w in range(N):
                if ts[w]:
                    d[v] += 1
                    rg[w].append(v)
        ds.append(d)
        rgs.append(rg)

    D = [0]*N
    # alors ici je fais le cumul des d
    for i in range(3):
        d = ds[i]
        for v in range(N):
            if d[v]:
                D[v] += 1

    U = [-1]*N
    U[N-1] = 0
    que = deque()
    que.append(N-1)
    # Parcours en largeur ?
    while que:
        v = que.popleft()
        u = U[v]
        for i in range(len(rgs)):
            rg = rgs[i]
            d = ds[i]
            for w in rg[v]:
                if not d[w]:
                    continue
                d[w] = 0
                D[w] -= 1
                if D[w] == 0 and U[w] == -1:
                    U[w] = u + 1
                    que.append(w)
    if U[0] != -1:
        writer(f"{U[0]}\n")
    else:
        writer("IMPOSSIBLE\n")

solve()