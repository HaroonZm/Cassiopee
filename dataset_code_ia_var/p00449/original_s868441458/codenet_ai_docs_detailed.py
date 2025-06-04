from heapq import heappush, heappop, heapify

def dijkstra(start, target, links):
    """
    Calcule le coût minimal entre deux nœuds dans un graphe pondéré non orienté
    en utilisant l'algorithme de Dijkstra.

    Args:
        start (int): Indice du nœud de départ.
        target (int): Indice du nœud d'arrivée.
        links (list of set): Liste d'adjacence où chaque élément est un ensemble de 
            tuples (coût, voisin) représentant une arête pondérée.

    Returns:
        int: Le coût minimal pour atteindre le nœud target depuis start. 
             Retourne -1 si le nœud n'est pas atteignable.
    """
    # Initialisation du tas de priorité avec les voisins directs de start
    heap = list(links[start])
    heapify(heap)  # Construction du tas de priorité selon le coût
    visited = set()  # Ensemble des nœuds déjà visités

    # Parcours tant que le tas n'est pas vide
    while heap:
        fare, node = heappop(heap)  # Extraction du nœud avec le coût minimal
        if node == target:
            return fare  # Retourne le coût si le nœud cible est atteint
        if node in visited:
            continue  # Ignore si déjà visité
        visited.add(node)  # Marque comme visité

        # Explore les voisins du nœud courant
        for fare2, node2 in links[node]:
            if node2 not in visited:
                # Ajoute le voisin dans le tas avec le coût cumulé
                heappush(heap, (fare + fare2, node2))
    return -1  # Retourne -1 si le nœud cible n'est pas atteignable

def main():
    """
    Gère l'entrée interactive pour la résolution répétée de problèmes de plus court chemin.
    Permet l'ajout d'arêtes et la requête de plus court chemin dans un graphe modifiable.
    """
    while True:
        # Lecture du nombre de nœuds (n) et du nombre d'opérations (k)
        n, k = map(int, input().split())
        if not n:
            break  # Sort de l'entrée si n == 0

        # Initialisation de la liste d'adjacence des liens (graphe)
        links = [set() for _ in range(n)]

        for _ in range(k):
            # Lecture des paramètres de l'opération courante
            # Deux types d'opérations : ajout d'arête ou requête de chemin
            inp = list(map(int, input().split()))
            if inp[0]:  # Cas où la première valeur est non nulle : ajout d'arête
                c, d, e = inp
                c, d = c - 1, d - 1  # Passage à des indices 0-based
                # Ajout de l'arête non orientée entre c et d avec le coût e
                links[c].add((e, d))
                links[d].add((e, c))
            else:  # Cas où la première valeur est 0 : requête de plus court chemin
                _, b = inp
                # Appel de Dijkstra entre le nœud 0 et b-1, puis affichage du résultat
                print(dijkstra(0, b - 1, links))

if __name__ == "__main__":
    main()