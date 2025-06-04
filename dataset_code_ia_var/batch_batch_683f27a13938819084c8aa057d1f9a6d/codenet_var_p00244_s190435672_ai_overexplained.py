from heapq import heappush, heappop  # Importation de la fonction heappush et heappop à partir du module heapq qui permet d'utiliser une file de priorité (min-heap) pour le traitement efficace de minimums

INF = 10 ** 20  # Définition d'une variable constante INF (infini) pour représenter une distance très grande, ici choisie arbitrairement comme 10^20

while True:  # Démarrage d'une boucle infinie pour traiter plusieurs ensembles d'entrée tant qu'aucune condition d'arrêt n'est rencontrée
    # Ici on attend deux entiers en entrée, séparés par des espaces : n (nombre de sommets) et m (nombre d'arêtes)
    n, m = map(int, input().split())  # Lecture d'une ligne de l'entrée standard, découpage puis conversion des éléments en entiers et affectation à n et m
    if n == 0:  # Condition d'arrêt : si le nombre de sommets est nul, alors il n'y a rien à traiter, on sort de la boucle
        break
    
    # Création d'une liste d'adjacence pour représenter le graphe. 
    # Ici, on double le nombre de sommets pour pouvoir les distinguer selon certains états.
    # edges[i] sera la liste des arêtes sortant du noeud i.
    edges = [[] for _ in range(n * 2)]  # On crée n*2 listes vides, une pour chaque sommet (état normal et état 'marqué')

    # Boucle de lecture des arêtes du graphe
    for _ in range(m):  # On répète l'opération m fois, une par arête
        a, b, c = map(int, input().split())  # Lecture des extrémités de l'arête (a et b) et de son coût (c)
        a -= 1  # On convertit de la numérotation 1-based vers 0-based pour faciliter l'accès aux listes en Python
        b -= 1

        # On ajoute l'arête dans les deux sens car le graphe est non orienté (l'arête va et vient entre a et b)
        # Pour les n premiers sommets (état normal)
        edges[a].append((b, c))      # On ajoute (b, c) à la liste d'adjacence du sommet a
        edges[b].append((a, c))      # On ajoute (a, c) à la liste d'adjacence du sommet b

        # Pour les n suivants, qui représentent le même sommet mais dans un autre état (état 'marqué')
        edges[a + n].append((b + n, c))  # On ajoute dans la case décalée à droite de n pour garder la correspondance d'état
        edges[b + n].append((a + n, c))
    
    # Cette boucle sert à créer des arêtes supplémentaires permettant des sauts d'état gratuits selon une règle
    for i in range(n):  # Pour chaque sommet original (de 0 à n-1)
        adds = []  # Liste tampon pour stocker les ajouts d'arêtes gratuites
        for to, _ in edges[i]:  # Pour chaque voisin to du sommet i (dans son état normal)
            if to < n:  # Si le voisin est aussi dans l'état normal (non 'marqué')
                for toto, _ in edges[to]:  # On regarde à son tour les voisins de 'to'
                    if toto < n and toto != i:  # Si le voisin du voisin est un sommet normal différent du sommet de départ
                        # On prépare une arête gratuite (coût 0) vers l'état 'marqué' de ce sommet (toto + n)
                        adds.append((toto + n, 0))
        # On ajoute toutes ces arêtes à la liste d'adjacence de i pour permettre ces transitions instantanées
        edges[i].extend(adds)

    # On ajoute une arête gratuite depuis la version normale du sommet final (n-1) jusqu'à sa version 'marquée'
    edges[n - 1].append((2 * n - 1, 0))
    
    # On prépare maintenant l'algorithme de Dijkstra pour trouver le plus court chemin
    # Initialisation des coûts de chaque sommet à INF (on considère qu'ils sont inaccessibles au départ)
    costs = [INF] * (2 * n)
    # Création de la file de priorité (priority queue) qui va contenir les paires (coût_total, numéro_de_noeud)
    que = []
    heappush(que, (0, 0))  # On commence depuis le sommet 0 (état normal) avec un coût total de 0
    
    # Boucle principale de Dijkstra
    while que:  # Tant qu'il y a des noeuds à traiter dans la file de priorité
        total, node = heappop(que)  # On retire la paire (coût minimal actuel, sommet) en tête de la file (le coût minimum)
        # On parcourt tous les voisins accessibles depuis ce sommet
        for to, cost in edges[node]:  # pour chaque voisin 'to' et le coût 'cost' de l'arête
            if costs[to] > total + cost:  # Si venir jusqu'à 'to' par ce chemin est meilleur que tout ce qu'on a déjà trouvé
                costs[to] = total + cost  # On met à jour le coût minimal connu pour 'to'
                heappush(que, (total + cost, to))  # Et on ajoute ce sommet à la file pour explorer ses voisins à l'avenir
    # A la fin du Dijkstra, costs[2 * n - 1] contient le coût le plus bas pour rejoindre le dernier sommet dans sa version 'marquée'
    print(costs[2 * n - 1])  # On affiche ce résultat. Si unreachable, cela affichera la valeur 'INF' choisie.