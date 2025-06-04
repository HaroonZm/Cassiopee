def bfs(x, visited, order):
    """
    Effectue un parcours en profondeur (DFS) à partir du sommet x.
    Marque les sommets visités, visite récursivement tous les voisins accessibles via le graphe orienté 'edges',
    puis ajoute le sommet x à la liste 'order' après avoir visité tous ses enfants.

    Args:
        x (int): Le sommet de départ pour le parcours DFS.
        visited (list of bool): Tableau représentant si un sommet a été visité ou non.
        order (list of int): Liste dans laquelle les sommets sont ajoutés selon l'ordre de fin de parcours.

    Returns:
        None
    """
    if visited[x]:
        return
    visited[x] = True
    for to in edges[x]:
        bfs(to, visited, order)
    order.append(x)

def bfs_rev(x):
    """
    Effectue un parcours en profondeur (DFS) à partir du sommet x dans le graphe transposé 'rev_edges'.
    Marque les sommets visités, retourne la liste de tous les sommets accessibles dans la composante connexes.

    Args:
        x (int): Le sommet de départ pour le parcours DFS.

    Returns:
        list of int: Liste de tous les sommets appartenant à la composante fortement connexe contenant x.
    """
    if visited[x]:
        return []
    visited[x] = True
    ret = [x]
    for to in rev_edges[x]:
        ret += bfs_rev(to)
    return ret

# Lecture du nombre d'arêtes
n = int(input())

# Initialisation des listes d'adjacence pour les graphes originaux et transposés
edges = [[] for _ in range(200)]      # Graphe orienté normal
rev_edges = [[] for _ in range(200)]  # Graphe transposé (arcs inversés)

# Construction du graphe selon le format des entrées
for _ in range(n):
    u, s, d = input().split()
    u = int(u) - 1                     # Conversion de l'identifiant source en index de 0 à 99
    d = int(d) - 1 + 100               # Conversion de l'identifiant destination en index de 100 à 199

    if s == "lock":
        # Pour un arc de type 'lock', l'arc dirigé va de d vers u
        edges[d].append(u)
        rev_edges[u].append(d)
    else:
        # Sinon, l'arc va de u vers d
        edges[u].append(d)
        rev_edges[d].append(u)

# Construction de l'ordre de parcours en profondeur (utilisé pour Kosaraju)
order = []
visited = [False] * 200

for i in range(200):
    if not visited[i]:
        bfs(i, visited, order)

# Inversion de l'ordre pour obtenir l'ordre de traitement (Kosaraju)
order.reverse()

# Initialisation du tableau des sommets visités pour le second parcours
visited = [False] * 200

# Recherche d'une composante fortement connexe de taille >= 2 via le parcours du graphe transposé
for i in order:
    if not visited[i]:
        if len(bfs_rev(i)) >= 2:
            print(1)
            break
else:
    # Si aucune composante fortement connexe de taille >= 2 n'est trouvée
    print(0)