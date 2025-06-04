import heapq

def read_graph_and_init():
    """
    Lit les entrées utilisateur pour créer un graphe non orienté pondéré, initialiser la structure des coûts, 
    et identifier les sommets sources.
    
    Returns:
        n (int): Nombre de sommets.
        m (int): Nombre d'arêtes.
        K (int): Nombre de sommets sources.
        g (list of list of int): Liste d'adjacence du graphe.
        cost (list of list of int): Matrice des coûts entre chaque paire de sommets (10^5 si pas d'arête).
        sources (list of int): Liste des indices des sommets sources (0-indexés).
    """
    n, m, K = map(int, raw_input().split())
    # Initialisation de la liste d'adjacence
    g = [[] for _ in xrange(n)]
    # Initialisation de la matrice des coûts (valeur arbitrairement grande pour non connectés)
    cost = [[10**5]*n for _ in xrange(n)]

    # Lecture des arêtes et remplissage de la structure
    for _ in xrange(m):
        a, b, l = map(int, raw_input().split())
        a -= 1  # Indices en base 0
        b -= 1
        g[a].append(b)
        g[b].append(a)
        cost[a][b] = l
        cost[b][a] = l

    # Lecture des sommets sources
    sources = []
    for _ in xrange(K):
        c = int(raw_input()) - 1
        sources.append(c)
        
    return n, m, K, g, cost, sources

def dijkstra_from_sources(n, g, cost, sources):
    """
    Exécute l'algorithme de Dijkstra multi-sources pour calculer les distances minimales 
    de chaque sommet aux sources.
    
    Args:
        n (int): Nombre de sommets.
        g (list of list of int): Liste d'adjacence du graphe.
        cost (list of list of int): Matrice des coûts entre chaque paire de sommets.
        sources (list of int): Sommets considérés comme sources.

    Returns:
        d (list of float): Distances minimales de chaque sommet à la source la plus proche.
    """
    # File de priorité pour Dijkstra
    pq = []
    # Initialisation du tableau des distances à l'infini
    d = [float('inf')] * n
    
    # Ajouter tous les sommets sources à la file de priorité, distance = 0
    for c in sources:
        heapq.heappush(pq, [0, c])
        d[c] = 0
    
    # Exploration du graphe
    while pq:
        t, u = heapq.heappop(pq)
        if d[u] < t:
            continue  # On a déjà trouvé un plus court chemin vers u
        for v in g[u]:
            # Relâchement de l'arête (u, v) si une meilleure distance est trouvée
            if d[u] + cost[u][v] < d[v]:
                d[v] = d[u] + cost[u][v]
                heapq.heappush(pq, [d[v], v])
    return d

def compute_max_pseudo_diameter(n, g, cost, d):
    """
    Calcule la valeur maximale selon la formule donnée sur toutes les arêtes du graphe.
    La formule considère les distances issues de Dijkstra pour une espèce de "pseudo-diamètre".

    Args:
        n (int): Nombre de sommets.
        g (list of list of int): Liste d'adjacence du graphe.
        cost (list of list of int): Matrice des coûts entre chaque paire de sommets.
        d (list of float): Distances minimales de chaque sommet à la source la plus proche.

    Returns:
        ans (float): Valeur maximale selon la formule.
    """
    ans = 0
    for i in xrange(n):
        for j in g[i]:
            val = (1 + d[i] + d[j] + cost[i][j]) / 2.0
            ans = max(ans, val)
    return ans

def main():
    """
    Fonction principale. Gère la lecture des entrées, l'exécution de Dijkstra multi-sources,
    le calcul de la valeur maximum et affiche le résultat.
    """
    n, m, K, g, cost, sources = read_graph_and_init()
    d = dijkstra_from_sources(n, g, cost, sources)
    ans = compute_max_pseudo_diameter(n, g, cost, d)
    print(ans)

# Exécution du programme principal
main()