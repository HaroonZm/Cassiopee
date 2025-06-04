import heapq
from collections import deque

def read_input():
    """
    Lit l'entrée standard pour obtenir le nombre de sommets et d'arêtes,
    puis les arêtes avec leur poids.

    Returns:
        N (int): nombre de sommets
        M (int): nombre d'arêtes
        edges (list): liste de tuples (a, b, c) représentant les arêtes avec leur poids
    """
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, c))
    return N, M, edges

def initialize_graph(N, edges):
    """
    Initialise la table des poids, la liste d'adjacence et la matrice d'utilisation des arêtes.

    Args:
        N (int): nombre de sommets
        edges (list): liste des arêtes (a, b, c)

    Returns:
        table (list): matrice des poids des arêtes
        used (list): matrice d'utilisation des arêtes pour les plus courts chemins
        tree (list): représentation adjacente du graphe
    """
    # Initialiser la matrice des poids avec l'infini (aucune connexion par défaut)
    table = [[float('inf') for _ in range(N)] for _ in range(N)]
    # Initialiser la matrice d'utilisation, -inf servant de marqueur pour les arêtes inexistantes
    used = [[-float('inf') for _ in range(N)] for _ in range(N)]
    # Représentation par liste d'adjacence du graphe
    tree = [[] for _ in range(N)]

    for a, b, c in edges:
        table[a][b] = c
        table[b][a] = c
        tree[a].append(b)
        tree[b].append(a)
        used[a][b] = 0   # Marque l'existence de l'arête, mais non utilisée dans un plus court chemin
        used[b][a] = 0

    # Distance nulle pour les sommets à eux-mêmes
    for i in range(N):
        table[i][i] = 0

    return table, used, tree

def mark_shortest_paths(N, table, used, tree):
    """
    Pour chaque sommet, exécute Dijkstra afin de trouver les plus courts chemins et marque les arêtes utilisées.

    Args:
        N (int): le nombre de sommets
        table (list): matrice des poids des arêtes
        used (list): matrice d'utilisation des arêtes
        tree (list): représentation adjacente du graphe

    Effet de bord:
        Modifie la matrice used pour marquer, via la valeur 1, les arêtes appartenant à au moins un plus court chemin
    """
    for source in range(N):
        # Initialise les distances à l'infini et la distance à la source à 0
        dist = [float('inf')] * N
        dist[source] = 0
        # prev permet de retrouver les prédécesseurs dans le chemin le plus court
        prev = [-1] * N

        # File de priorité pour Dijkstra (heap), on y met (distance, node)
        queue = []
        queue.append([0, source])
        heapq.heapify(queue)

        while queue:
            curr_dist, u = heapq.heappop(queue)
            # Si on a déjà trouvé un chemin plus court, ignorer cette entrée
            if dist[u] < curr_dist:
                continue

            # Remonter la chaîne de prédécesseurs pour retrouver tous les arcs du plus court chemin
            v = u
            piv = prev[u]
            while piv != -1:
                used[piv][v] = 1  # Marque l'arête comme utilisée dans un plus court chemin
                used[v][piv] = 1  # Puisque le graphe est non orienté
                v = piv
                piv = prev[piv]

            # Parcours des voisins pour Dijkstra
            for neighbor in tree[u]:
                alt = dist[u] + table[u][neighbor]
                if dist[neighbor] > alt:
                    dist[neighbor] = alt
                    heapq.heappush(queue, [alt, neighbor])
                    prev[neighbor] = u

def count_unused_edges(N, used):
    """
    Compte le nombre d'arêtes qui n'appartiennent à aucun plus court chemin.

    Args:
        N (int): nombre de sommets
        used (list): matrice d'utilisation des arêtes

    Returns:
        int: nombre d'arêtes inutilisées (chaque arête est comptée une fois)
    """
    ans = 0
    # On parcourt la partie supérieure de la matrice car le graphe est non orienté
    for i in range(N):
        for j in range(i + 1, N):
            if used[i][j] == 0:
                ans += 1
    return ans

def main():
    """
    Fonction principale orchestrant la lecture, le traitement et l'affichage du résultat.
    """
    # Lecture et initialisation
    N, M, edges = read_input()
    table, used, tree = initialize_graph(N, edges)
    # Marque les arêtes utilisées dans au moins un plus court chemin
    mark_shortest_paths(N, table, used, tree)
    # Compte et affiche le nombre d'arêtes inutilisées dans tous les plus courts chemins
    result = count_unused_edges(N, used)
    print(result)

if __name__ == "__main__":
    main()