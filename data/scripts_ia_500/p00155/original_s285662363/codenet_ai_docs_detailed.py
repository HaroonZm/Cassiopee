from heapq import heappush, heappop

INF = 10 ** 20  # Constante représentant une distance infiniment grande

while True:
    # Lecture du nombre de bâtiments (points)
    n = int(input())
    if n == 0:
        # Condition d’arrêt du programme
        break

    # Initialisation de la liste des coordonnées des bâtiments
    buil_point = [None] * n
    for _ in range(n):
        # Lecture de l’identifiant du bâtiment et de ses coordonnées (x, y)
        b, x, y = map(int, input().split())
        # Stockage des coordonnées dans la liste à l’index correspondant au bâtiment -1
        buil_point[b - 1] = (x, y)

    # Création de la liste d’adjacence pour représenter le graphe
    # Chaque élément contient des tuples (coût, noeud voisin)
    edges = [[] for _ in range(n)]

    # Construction des arêtes entre bâtiments accessibles (distance <= 50)
    for i in range(n):
        for j in range(i + 1, n):
            ix, iy = buil_point[i]
            jx, jy = buil_point[j]
            # Calcul de la distance euclidienne entre les deux points
            cost = ((jx - ix) ** 2 + (jy - iy) ** 2) ** 0.5
            if cost <= 50:
                # Ajout des arêtes dans les deux sens, car le graphe est non orienté
                edges[i].append((cost, j))
                edges[j].append((cost, i))

    # Lecture du nombre de requêtes de chemin
    m = int(input())
    for _ in range(m):
        # Lecture des points de départ (s) et d’arrivée (g)
        s, g = map(int, input().split())
        # Initialisation des distances à l’infini pour tous les noeuds
        costs = [INF] * n
        # Distance du noeud de départ à lui-même = 0
        costs[s - 1] = 0
        # Initialisation des chemins, liste de liste pour stocker le chemin minimal vers chaque noeud
        paths = [[]] * n
        # Chemin vers le départ est juste le noeud lui-même
        paths[s - 1] = [s - 1]
        # File de priorité (heap) pour l’algorithme de Dijkstra
        que = []
        # Ajout du point de départ dans la queue, avec distance 0 et chemin initial
        heappush(que, (0, [s - 1]))

        # Boucle principale de l’algorithme de Dijkstra
        while que:
            dist, path = heappop(que)  # Extraction du chemin avec la plus petite distance
            last = path[-1]  # Dernier noeud du chemin actuel

            # Parcours des voisins du dernier noeud
            for cost, to in edges[last]:
                # Si on trouve un chemin plus court vers 'to'
                if costs[to] > dist + cost:
                    # Mise à jour du coût minimum pour atteindre 'to'
                    costs[to] = dist + cost
                    # Stockage du chemin amélioré
                    paths[to] = path + [to]
                    # Ajout à la queue avec la nouvelle distance et chemin
                    heappush(que, (dist + cost, path + [to]))

        # Affichage du résultat pour la requête:
        # Si on a trouvé un chemin jusque 'g'
        if paths[g - 1]:
            # Afficher les noeuds du chemin en ajoutant 1 pour revenir à la numérotation d’origine
            print(*map(lambda x: x + 1, paths[g - 1]))
        else:
            # Sinon, afficher "NA" (pas de chemin)
            print("NA")