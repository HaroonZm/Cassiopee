from collections import deque

def read_ints():
    """
    Lit une ligne de l'entrée standard et la découpe en entiers.

    Returns:
        list: Liste d'entiers lus sur la ligne courante d'entrée.
    """
    return list(map(int, input().split()))

def build_graph(x, y, z, n, m, s, t):
    """
    Construit le graphe non orienté selon les contraintes du problème.

    Args:
        x (int): Nombre de sommets dans la première partition.
        y (int): Nombre de sommets dans la deuxième partition.
        z (int): Nombre de sommets dans la troisième partition.
        n (int): Nombre d'arêtes entre la 1ère et la 2e partition.
        m (int): Nombre d'arêtes entre la 2e et la 3e partition.
        s (int): Index (1-based) de l'arête particulière dans n (pour p, q).
        t (int): Index (1-based) de l'arête particulière dans m (pour u, v).

    Returns:
        g (list): Graphe sous forme de liste d'adjacence.
        p, q, u, v (int): Indices particuliers pour le calcul final.
    """
    # Initialiser une liste d'adjacence vide pour tous les sommets
    g = [[] for _ in range(x + y + z)]
    p = q = u = v = None

    # Traitement des arêtes entre la première et la deuxième partition
    for i in range(n):
        a, b = read_ints()
        # Conversion en indices 0-based :
        a_idx = a - 1
        b_idx = b + x - 1  # Décalé après la première partition (taille x)
        # Ajout des arêtes de façon non orientée
        g[a_idx].append(b_idx)
        g[b_idx].append(a_idx)
        # Sauvegarder les positions spéciales si l'indice correspond à 's'
        if i == s - 1:
            p, q = a_idx, b_idx

    # Traitement des arêtes entre la deuxième et la troisième partition
    for j in range(m):
        a, b = read_ints()
        # Conversion en indices 0-based :
        a_idx = a + x - 1    # Début de la deuxième partition (taille x)
        b_idx = b + x + y - 1  # Début de la troisième partition
        # Ajout des arêtes de façon non orientée
        g[a_idx].append(b_idx)
        g[b_idx].append(a_idx)
        # Sauvegarder les positions spéciales si l'indice correspond à 't'
        if j == t - 1:
            u, v = a_idx, b_idx

    return g, p, q, u, v

def bfs_min_path(g, d, start_nodes):
    """
    Effectue un BFS à partir d'un ensemble de nœuds de départ pour calculer les distances minimales.

    Args:
        g (list): Liste d'adjacence représentant le graphe.
        d (list): Liste des distances (-2 si non atteint).
        start_nodes (list): Liste d'indices de départ pour le BFS.

    Modifie:
        d : Remplit les distances minimales depuis les start_nodes jusqu'à tous les nœuds accessibles.
    """
    q = deque(start_nodes)
    for idx in start_nodes:
        d[idx] = 0  # Distance des nœuds de départ = 0

    # Parcours BFS standard
    while q:
        curr = q.popleft()
        for neighbor in g[curr]:
            if d[neighbor] == -2:  # Si le nœud n'a pas encore été découvert
                d[neighbor] = d[curr] + 1
                q.append(neighbor)

def main():
    """
    Fonction principale :
    1. Lit les entrées,
    2. Construit le graphe et identifie les nœuds d'intérêt,
    3. Calcule les distances minimales via BFS,
    4. Affiche le résultat demandé par le problème.
    """
    # Lire les paramètres principaux
    x, y, z, n, m, s, t = read_ints()  # partitions, nombre d'arêtes, etc.
    # Construction du graphe et récupération des indices particuliers
    g, p, q_, u, v = build_graph(x, y, z, n, m, s, t)
    # Initialisation des distances comme 'non visité' (-2 pour tous)
    d = [-2] * (x + y + z)
    # Effectuer un BFS avec les deux nœuds de départ p et q_
    bfs_min_path(g, d, [p, q_])
    # Afficher la plus petite distance parmi les deux nœuds cibles + 1 (pour inclure le dernier déplacement)
    print(min(d[u], d[v]) + 1)

# Lancement du programme principal
if __name__ == "__main__":
    main()