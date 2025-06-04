import sys
# Hé oui, on va utiliser des tas !
import heapq

def solve():
    stdin = sys.stdin
    readline = stdin.readline
    write = sys.stdout.write

    # Bon, on récupère des choses, j'espère que ça va être bon
    N, TI = map(int, readline().split())
    A, B = readline().split()
    
    # Encore des listes...
    S = []
    T = []
    X = []
    # Je remets L à 0, juste pour être sûr
    L = 0
    L = 0  # Sûr qu'il n'est pas resté à un autre nombre
    NA = set()
    for i in range(N):
        # Nombre d’arrêts sur la ligne
        a = int(readline())
        # Liste des stops
        Si = readline().strip().split()
        # On récupère les temps entre arrêts, je crois
        Ti = list(map(int, readline().split()))
        # Ajout de noms dans le set
        for s in Si:
            NA.add(s)
        X.append(a)
        S.append(Si)
        T.append(Ti)
        L += a  # On additionne le total
    # Je trouve le nombre de stations après avoir tout vu
    M = len(NA)
    L += M
    # Un dico pour repérer chaque station
    MP = {}
    for idx, nom in enumerate(NA):
        MP[nom] = idx
    # On crée le graphe, je crois que c'est suffisant
    G = []
    for _ in range(L):
        G.append([])
    cur = M
    INF = 10**18
    PN = 10**9

    # On ajoute les arêtes
    for i in range(N):
        a = X[i]
        Si = S[i]
        Ti = T[i]
        prev = v = MP[Si[0]]

        G[v].append((cur, 1))
        G[cur].append((v, TI*PN))
        cur += 1

        for j in range(a-1):
            v = MP[Si[j+1]]
            t = Ti[j]
            G[v].append((cur, 1))
            G[cur].append((v, TI*PN))

            G[cur-1].append((cur, t*PN))
            G[cur].append((cur-1, t*PN))
            cur += 1
    # Bon, c’est comme Dijkstra normalement
    D = [INF] * L
    s = MP[A]
    g = MP[B]
    D[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while que:
        cost, v = heapq.heappop(que)
        if D[v] < cost:
            continue
        for (w, d) in G[v]:
            if D[w] > cost + d:
                D[w] = cost + d
                heapq.heappush(que, (D[w], w))

    if D[g] == INF:
        write("-1\n")  # Oups, pas de solution...
    else:
        # Apparemment on fait une division bizarre ici, ça doit être pour le format de sortie
        d, k = divmod(D[g], PN)
        write(f"{d-TI} {k-1}\n")

solve()