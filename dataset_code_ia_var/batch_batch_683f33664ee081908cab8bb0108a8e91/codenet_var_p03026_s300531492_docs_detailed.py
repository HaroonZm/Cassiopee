def build_adjacency_list(n, edges):
    """
    Construit la liste d'adjacence d'un graphe non orienté à partir d'une liste d'arêtes.

    Args:
        n (int): Nombre de sommets dans le graphe (numérotés de 1 à n).
        edges (List[Tuple[int, int]]): Liste d'arêtes, chaque arête est un tuple de deux sommets.

    Returns:
        List[List[int]]: Liste d'adjacence (E), où E[i] contient les voisins du sommet i.
    """
    E = [[] for _ in range(n + 1)]
    for A, B in edges:
        E[A].append(B)
        E[B].append(A)
    return E

def find_max_degree_node(E):
    """
    Trouve le nœud ayant le degré maximal dans la liste d'adjacence.

    Args:
        E (List[List[int]]): Liste d'adjacence du graphe.

    Returns:
        int: Sommet ayant le plus de voisins (degré maximal).
    """
    max_degree = 0
    node = 0
    for i in range(1, len(E)):
        if len(E[i]) > max_degree:
            max_degree = len(E[i])
            node = i
    return node

def assign_colors_bfs(E, colors, start):
    """
    Assigne les couleurs aux sommets du graphe en effectuant un parcours BFS à partir d'un sommet donné.

    Args:
        E (List[List[int]]): Liste d'adjacence du graphe.
        colors (List[int]): Liste de couleurs triées à assigner (longueur N).
        start (int): Sommet de départ pour le BFS.

    Returns:
        Dict[int, int]: Dictionnaire associant chaque sommet à sa couleur.
    """
    from collections import deque

    n = len(colors)
    ans = {}
    visited = [False] * len(E)
    q = deque()
    q.append(start)

    # Parcours BFS, en attribuant les couleurs les plus grandes en premier
    for i in range(1, n + 1):
        x = q.popleft()
        visited[x] = True
        ans[x] = colors[-i]
        for neighbor in E[x]:
            if not visited[neighbor]:
                q.append(neighbor)
    return ans

def compute_max_sum(colors):
    """
    Calcule la valeur maximale demandée (somme de toutes les couleurs sauf la plus grande).

    Args:
        colors (List[int]): Liste des couleurs permutées.

    Returns:
        int: La somme maximale.
    """
    return sum(colors) - colors[-1]

def format_answer(ans, n):
    """
    Formate la réponse en chaîne d'entiers séparés par des espaces, dans l'ordre des sommets de 1 à n.

    Args:
        ans (Dict[int, int]): Dictionnaire associant chaque sommet à sa couleur.
        n (int): Nombre total de sommets.

    Returns:
        str: La chaîne formatée avec les couleurs attribuées.
    """
    out = []
    for i in range(1, n + 1):
        out.append(str(ans[i]))
    return " ".join(out)

def main():
    """
    Fonction principale qui exécute tout le processus : lit les entrées, construit le graphe,
    trouve le sommet de plus haut degré, trie les couleurs, attribue les couleurs, affiche les résultats.
    """
    # Lecture du nombre de sommets
    N = int(input())

    # Lecture et stockage des arêtes, au format (A, B)
    edges = []
    for _ in range(N - 1):
        A, B = map(int, input().split())
        edges.append((A, B))

    # Construction de la liste d'adjacence
    E = build_adjacency_list(N, edges)

    # Trouver le nœud avec le degré le plus élevé (le point de départ pour BFS)
    First = find_max_degree_node(E)

    # Lecture et tri des couleurs
    C = list(map(int, input().split()))
    C.sort()

    # Calcul de la somme maximale requise (la somme de toutes les couleurs sauf la plus grande)
    max_sum = compute_max_sum(C)

    # Attribution des couleurs via BFS en partant du sommet choisi
    ans = assign_colors_bfs(E, C, First)

    # Affichage
    print(max_sum)
    print(format_answer(ans, N))

if __name__ == "__main__":
    main()