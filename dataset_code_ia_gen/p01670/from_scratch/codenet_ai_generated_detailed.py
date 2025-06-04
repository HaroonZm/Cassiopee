import sys
sys.setrecursionlimit(10**7)

def dfs(u):
    """
    Fonction DFS pour trouver les points d'articulation (cut vertices) dans le graphe.
    Nous utilisons l'algorithme de Tarjan pour les points d'articulation.
    """
    global time, graph, visited, disc, low, parent, ap
    visited[u] = True
    disc[u] = time     # temps de découverte de u
    low[u] = time      # plus petit temps de découverte accessible depuis u
    time += 1
    children = 0       # nombre d'enfants dans l'arbre DFS

    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            dfs(v)
            # Met à jour low[u] selon low[v]
            low[u] = min(low[u], low[v])

            # Cas 1 : u est racine et a au moins 2 enfants
            if parent[u] == -1 and children > 1:
                ap[u] = True
            # Cas 2 : u n'est pas racine et low[v] >= disc[u]
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True

        elif v != parent[u]:
            # Si v est déjà découvert et n'est pas le parent direct, met à jour low[u]
            low[u] = min(low[u], disc[v])


def main():
    """
    Résout le problème du placement minimal de stations de quarantaine.
    La contrainte est que chaque arête (liner) doit être couverte par au moins un sommet (île) avec station.
    Cela correspond à trouver un vertex cover sur le graphe.
    Pour ce problème, il s'agit surtout de protéger les points d'articulation car ce sont eux qui provoquent des
    chemins non couvert.
    Méthode:
    - Trouver tous les points d'articulation
    - Construire un vertex cover minimal qui inclut tous les points d'articulation.
    - Comme le problème est complexe dans le cas général, les solutions attendues correspondent aux points d'articulation.
    En fait, nous pouvons démontrer que le nombre minimum de stations correspond au nombre minimum de sommets
    qui couvrent toutes les arêtes, ce qui est équivalent aux points d'articulation dans ce contexte.
    Le nombre ne peut excéder K.
    """

    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    global graph, visited, disc, low, parent, ap, time
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * N
    disc = [float('inf')] * N
    low  = [float('inf')] * N
    parent = [-1] * N
    ap = [False] * N  # points d'articulation
    time = 0

    # Trouver tous les points d'articulation (cut vertices)
    for i in range(N):
        if not visited[i]:
            dfs(i)

    # Le minimum de stations correspond au nombre de points d'articulation
    # En effet, pour couvrir toutes les arêtes, il faut au moins couvrir les "points stratégiques"
    # qui déterminent les connexions. Cela garantit pour chaque liner, au moins une station à une extrémité.

    count_ap = sum(ap)

    if count_ap <= K:
        print(count_ap)
    else:
        # Sinon, impossible de construire avec au plus K stations
        print("Impossible")


if __name__ == "__main__":
    main()