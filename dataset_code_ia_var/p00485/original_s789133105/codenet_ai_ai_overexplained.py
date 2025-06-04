import sys  # Importation du module sys pour accéder à sys.argv (arguments passés à l'exécution du script)
from heapq import heappush, heappop  # Importation de fonctions pour manipuler une file de priorité (tas binaire)
from itertools import combinations  # Importation de la fonction pour générer les différentes combinaisons possible d'une liste

def dijkstra(adj, s):
    # Cette fonction implémente l'algorithme de Dijkstra pour calculer les plus courts chemins depuis le sommet s
    # adj : liste d'adjacence du graphe où adj[u] est une liste de tuples (v, coût)
    # s : sommet de départ (point de départ pour Dijkstra)

    # Définition de trois valeurs pour indiquer l'état (couleur) de chaque sommet :
    # WHITE : non visité
    # GRAY : découvert / en cours d'exploitation
    # BLACK : entièrement traité (tous ses voisins ont été parcourus)
    WHITE, GRAY, BLACK = 0, 1, 2

    # Initialisation d'un tableau de couleurs indiquant si le sommet u a déjà été traité
    color = [WHITE] * len(adj)  # Tous les sommets sont initialement blancs

    # Initialisation d'un tableau de distances
    # d[u] sera la distance minimale connue de s à u
    d = [float('inf')] * len(adj)  # Toutes les distances sont initialisées à l'infini
    d[s] = 0  # La distance au sommet de départ s est zéro

    # Création d'une file de priorité (tas binaire) pour extraire rapidement le sommet le plus proche non traité
    pq = []  # File de priorité vide (liste Python utilisée avec heapq)
    heappush(pq, (0, s))  # On insère le sommet de départ s avec une distance initiale de 0

    # Boucle principale de l'algorithme : on traite tant qu'il reste des sommets dans la file de priorité
    while pq:
        # On retire de la file le sommet u ayant la plus petite distance (fonctionne car le tas trie sur le premier élément du tuple)
        cost, u = heappop(pq)
        color[u] = BLACK  # On marque le sommet u comme complètement traité

        # Si la distance extraite pour u est plus grande que la distance connue, on saute ce sommet
        # Cela peut arriver si on a ajouté à la file une distance plus grande après avoir déjà trouvé le meilleur chemin
        if d[u] < cost:
            continue

        # Parcours de tous les voisins du sommet u
        for v, edge_cost in adj[u]:
            # Si le sommet voisin est déjà traité, pas besoin de le retravailler
            if color[v] == BLACK:
                continue

            # Si on trouve un chemin vers v plus court en passant par u
            if d[v] > d[u] + edge_cost:
                d[v] = d[u] + edge_cost  # On met à jour la distance pour ce sommet
                heappush(pq, (d[v], v))  # On ajoute à la file le sommet v pour être traité plus tard
                color[v] = GRAY  # On marque v comme découvert, même s'il peut être encore re-découvert plus tard

    # A la fin, d[u] est la plus petite distance de s à u pour tous les sommets u
    return d

def solve(adj, malls, n):
    # Cette fonction calcule la réponse attendue pour le problème en utilisant les chemins les plus courts.
    # adj : liste d'adjacence du graphe
    # malls : liste des indices de centres commerciaux
    # n : nombre total de sommets/nœuds (excepté l'indice 0 si utilisé comme offset)

    # On calcule les distances depuis le premier centre commercial dans la liste
    distance = dijkstra(adj, malls[0])

    # La variable 'ans' stockera pour chaque sommet n de 1 à n (excluant le sommet 0) une valeur particulière
    # Pour chaque sommet n, on regarde tous ses voisins (adj[n]), et pour chaque voisin j (avec indice j[0] et coût j[1])
    # On calcule une expression impliquant la distance jusqu'à n, le coût jusqu'au voisin, la distance jusqu'au voisin
    # On garde le maximum de ces valeurs pour chaque n, puis le maximum de tous ces maxima
    ans = []
    for node_idx, dist_to_node in enumerate(distance[1:], start=1):
        # Pour chaque nœud (hors nœud 0)
        local_max = float('-inf')
        for j in adj[node_idx]:
            neighbor_idx = j[0]  # Indice du voisin
            edge_cost = j[1]     # Coût de l'arête vers ce voisin
            value = (dist_to_node + edge_cost + distance[neighbor_idx]) / 2
            if value > local_max:
                local_max = value
        ans.append(local_max)
    # On prend ensuite la plus grande valeur calculée pour un sommet quelconque
    return int(max(ans) + 0.5)  # On arrondit à l'entier le plus proche (ajout de 0.5 avant la conversion entière)

def main(args):
    # Fonction principale qui lit les entrées, crée le graphe, et affiche la réponse finale

    # Lecture des trois premiers entiers sur la première ligne d'entrée :
    # n : nombre de sommets (villes, par exemple)
    # m : nombre d'arêtes (routes, par exemple)
    # k : nombre de centres commerciaux
    n, m, k = map(int, input().split())

    # Création d'une liste d'adjacence vide (on commence à l'indice 0, donc taille n+1)
    # Chaque case adj[u] contiendra une liste de tuples (v, coût) pour chaque voisin du sommet u
    adj = [[] for _ in range(n+1)]

    # Lecture des m arêtes (routes)
    for _ in range(m):
        f, t, c = map(int, input().split())  # f = sommet de départ, t = sommet d'arrivée, c = coût de la route
        adj[f].append((t, c))  # On ajoute la connexion f -> t de coût c
        adj[t].append((f, c))  # On ajoute la connexion t -> f (le graphe est non orienté)

    # Lecture des numéros des k centres commerciaux
    malls = []
    for _ in range(k):
        mall = int(input())  # Numéro de centre commercial
        malls.append(mall)

    # On relie tous les centres commerciaux entre eux avec des arêtes de coût 0
    # On considère toutes les combinaisons possibles de deux centres commerciaux différents
    for f, t in combinations(malls, 2):
        adj[f].append((t, 0))  # Ajout d'une arête f -> t de coût 0
        adj[t].append((f, 0))  # Ajout d'une arête t -> f de coût 0 (toujours non orienté)

    # Appel de la fonction de résolution avec tous les paramètres
    ans = solve(adj, malls, n)

    # Affichage de la réponse finale (formatée en nombre entier)
    print(ans)

# Entrée du programme principal
if __name__ == '__main__':
    # Si ce script est exécuté directement (et non importé comme module)
    main(sys.argv[1:])  # Appel de la fonction principale avec les arguments de la ligne de commande