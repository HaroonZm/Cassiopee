import sys
import heapq

def main():
    # Lire l'entrée
    N, M, K = map(int, sys.stdin.readline().split())
    INF = 10 ** 18

    # Initialiser les poids des arêtes
    E = []
    for i in range(N):
        E.append([-INF] * N)

    # Lire les arêtes
    for i in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        if E[a][b] < c:
            E[a][b] = c

    # Construire le graphe G à partir de E
    G = []
    for v in range(N):
        tmp = []
        for w in range(N):
            if E[v][w] >= 0:
                tmp.append((w, E[v][w]))
        G.append(tmp)

    # Initier la recherche (type BFS amélioré)
    T = 100
    dist = []
    prv = []
    for i in range(N):
        dist.append([0] * (T + 1))
        prv.append([None] * (T + 1))
    que = []
    for i in range(N):
        que.append((0, i, 0))
    heapq.heapify(que)
    t0 = T + 1

    while que:
        v = heapq.heappop(que)
        cost, node, t = v
        cost = -cost
        if cost >= K and t < t0:
            t0 = t
        if t == T or cost < dist[node][t]:
            continue
        for w, d in G[node]:
            if dist[w][t + 1] < cost + d:
                dist[w][t + 1] = cost + d
                prv[w][t + 1] = node
                heapq.heappush(que, (-(cost + d), w, t + 1))

    # Si chemin trouvé avec coût >= K en t0 mouvements ou moins
    if t0 != T + 1:
        v0 = 0
        d = 0
        for v in range(N):
            e = dist[v][t0]
            if d < e:
                d = e
                v0 = v
        res = [v0]
        v = v0
        t = t0
        while t > 0:
            v = prv[v][t]
            t -= 1
            res.append(v)
        res.reverse()
        print(t0)
        print(' '.join(str(x) for x in res))
        return

    # Sinon, utiliser la méthode matrice
    for v in range(N):
        E[v][v] = 0

    E2 = []
    for i in range(N):
        E2.append([-INF] * N)
    A = (K - 1).bit_length()
    RS = [E]
    E_tmp = E
    ok = False
    for k in range(A):
        F = []
        for i in range(N):
            F.append([-INF] * N)
        for v in range(N):
            for w in range(N):
                E2[w][v] = E_tmp[v][w]
        for i in range(N):
            for j in range(N):
                r = -INF
                for ii in range(N):
                    a = E_tmp[i][ii]
                    b = E2[j][ii]
                    if a >= 0 and b >= 0:
                        if a + b > r:
                            r = a + b
                F[i][j] = r
                if r >= K:
                    ok = True
        RS.append(F)
        E_tmp = F
        if ok:
            A = k
            break

    D = [0] * N
    ans = 0
    for i in range(A, -1, -1):
        E3 = RS[i]
        D0 = [-INF] * N
        ok = False
        for v in range(N):
            r = -INF
            for j in range(N):
                if D[j] >= 0 and E3[j][v] >= 0:
                    if D[j] + E3[j][v] > r:
                        r = D[j] + E3[j][v]
            D0[v] = r
            if r >= K:
                ok = True
        if not ok:
            ans += 1 << i
            D = D0
    ans += 1
    if ans > K:
        print(-1)
    else:
        print(ans)

main()