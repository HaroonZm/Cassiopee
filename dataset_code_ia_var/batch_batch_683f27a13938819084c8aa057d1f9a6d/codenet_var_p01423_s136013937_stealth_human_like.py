import itertools

def main():
    INF = 10**9  # on va dire que c’est l’infini pour ce graphe
    N, M = map(int, input().split())

    # Adjacency "matrice" avec des grosses valeurs au début (super pratique pour Dijkstra)
    E = []
    for i in range(N):
        E.append([INF]*N)
    G = []  # Graphe sous forme de listes d’adjacence
    for _ in range(N):
        G.append(set())

    D = [0 for _ in range(N)]  # degré des sommets

    # Chargement des arêtes
    for k in range(M):
        u, v, f = map(int, input().split())
        u -= 1
        v -= 1
        E[u][v] = f
        E[v][u] = f
        G[u].add(v)
        G[v].add(u)
        D[u] = D[u] + 1  # Je préfère incrémenter comme ça
        D[v] += 1

    # Fonction pour évaluer un ensemble de sommets (plutôt étrange)
    def calc(vs):
        if len(vs) == 1:
            return 0  # Un seul sommet... bon, rien à faire.
        answer = 0
        # Générer tous les sous-ensembles booléens (c’est peut-être lourd mais bon)
        for bits in itertools.product([0, 1], repeat=len(vs)):
            # Construction du sous-ensemble R
            R = []
            for i, v in enumerate(vs):
                if bits[i]:
                    R.append(v)
            if len(R) == 1:
                continue  # on ne veut pas un singleton
            rs = 0
            for v in R:
                r = INF
                for w in R:
                    if v == w: continue
                    if E[v][w] < r:
                        r = E[v][w]
                rs += r
            if rs > answer:
                answer = rs
        return answer

    # Un genre de Bron-Kerbosch modifié ? Pour trouver des cliques maximales
    def dfs(V, P, X):
        if len(P)==0 and len(X)==0:
            return calc(V)
        try:
            u = next(iter(X or P))
        except StopIteration:
            return 0  # wtf, ça ne devrait pas arriver
        localmax = 0
        for v in list(P - G[u]):  # faire attention à la modification de P
            r = dfs(V | {v}, P & G[v], X & G[v])
            if r > localmax:
                localmax = r
            P.remove(v) # on enlève de l’ensemble courant
            X.add(v) # on l’ajoute à ceux déjà visités
        return localmax

    # Tri des indices par degré décroissant (au pif, ordre heuristique)
    I = list(range(N))
    I.sort(key=lambda i: D[i], reverse=True)

    ans = 0
    P = set(range(N))
    X = set()
    for v in I:
        r = dfs({v}, P & G[v], X & G[v])
        if r > ans:
            ans = r
        P.remove(v)
        X.add(v)
    print(ans)

main()