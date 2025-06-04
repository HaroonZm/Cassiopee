import sys  # Importation du module sys pour accéder aux fonctions système, notamment l'entrée standard

input = sys.stdin.readline  # Redéfinition de la fonction input pour une lecture rapide ligne par ligne sur stdin

def dijkstra(start, matrix):
    # Implémentation de l'algorithme de Dijkstra classique en complexité O(V^2)
    # start : sommet de départ (index entier)
    # matrix : matrice d'adjacence représentant les coûts d'arête entre les sommets
    INF = 10 ** 18  # Valeur représentant l'infini, ici utilisée pour initialiser les distances à un grand entier
    n = len(matrix)  # Nombre de sommets (nœuds) dans le graphe, déduit de la taille de la matrice
    used = [False] * n  # Tableau pour garder en mémoire les sommets déjà traités par Dijkstra

    # dist[v] représente la "distance composite" pour atteindre chaque sommet v
    # Ici la "distance" encode deux choses à la fois :
    #   - le nombre de ravitaillements, pondéré fortement pour prioriser les moins nombreux
    #   - la quantité de carburant utilisée
    # Le calcul est : dist[v] = nb_ravitaillements * (10 ** 15) + carburant_utilisé
    dist = [INF] * n  # Initialisation du tableau dist avec 'INF' pour tous les sommets
    dist[start] = 0   # La distance pour atteindre le sommet de départ est de 0

    while True:  # Boucle principale de l'algorithme de Dijkstra
        v = -1  # Variable pour stocker le prochain sommet à traiter (valeur initiale impossible)
        for u in range(n):  # Parcourt tous les sommets du graphe
            # Si 'u' n'est pas encore traité et que sa distance est plus faible que celle de 'v', on met à jour 'v'
            if not used[u] and (v == -1 or dist[u] < dist[v]):
                v = u  # 'v' pointe désormais sur le sommet atteignable au coût minimum non encore traité
        if v == -1:  # Si aucun sommet n'est disponible, sortie de la boucle principale
            break
        used[v] = True  # Marque le sommet 'v' comme traité

        for nxt_v in range(n):  # Pour chaque sommet 'nxt_v', regarde si le chemin via 'v' est améliorant
            tmp = merge(dist[v], matrix[v][nxt_v])  # Calcule le coût composite pour atteindre 'nxt_v' via 'v'
            # Si ce nouveau chemin est meilleur, met à jour la valeur
            dist[nxt_v] = min(dist[nxt_v], tmp)
    return dist  # Retourne la liste finale de distances composites

def merge(d, cost):
    # Fonction pour fusionner le coût courant 'd' et le coût d'un nouveau segment 'cost'
    # Encode la logique de ravitaillement :
    #   - Si la somme carburant dépasse la capacité maximale 'l', il faut ravitailler et ajouter un "palier"
    #   - Sinon, simplement additionner au coût courant

    div_d, mod_d = divmod(d + cost, 10 ** 15)  # div_d = nombre de ravitaillements, mod_d = reste de carburant
    if mod_d > l:  # Si le carburant restant dépasse la capacité maximale autorisée 'l'
        # On doit ravitailler, donc on passe au palier supérieur
        new_d = (div_d + 1) * 10 ** 15 + cost
    else:
        # Pas besoin de ravitailler, on additionne juste les coûts
        new_d = d + cost
    return new_d  # Retourne la nouvelle distance composite

# Lecture des entrées du problème
n, m, l = map(int, input().split())  # n = nombre de sommets, m = nombre d'arêtes, l = capacité maximum sans ravitaillement
info = [list(map(int, input().split())) for i in range(m)]  # Liste des arêtes, chacune sous forme [a, b, cost]
q = int(input())  # Nombre de requêtes
query = [list(map(int, input().split())) for i in range(q)]  # Liste des requêtes : chaque requête est [a, b]

INF = 10 ** 18  # Définition globale de la constante infini pour initialiser les matrices

# Construction de la matrice d'adjacence : matrix[i][j] représente le coût direct de i à j
matrix = [[INF] * n for i in range(n)]  # Initialisation de la matrice avec l'infini partout
for i in range(n):
    matrix[i][i] = 0  # Le coût pour aller d'un sommet à lui-même est 0

# Remplissage de la matrice avec les coûts fournis par les arêtes
for a, b, cost in info:
    a -= 1  # Passage à l'indexation 0 (alors que l'entrée est probablement en indexation 1)
    b -= 1
    if cost > l:
        continue  # On ignore les arêtes dont le coût excède la capacité maximale sans ravitaillement
    matrix[a][b] = cost  # On assigne le coût dans la matrice pour l'arête allant de a à b
    matrix[b][a] = cost  # Le graphe est non orienté : le coût est le même dans l'autre sens

# Préparation d'une matrice de réponses : ans[i][j] contiendra le nombre minimal de ravitaillements de i à j
ans = [[0] * n for i in range(n)]  # Matrice initialisée à 0

for i in range(n):  # Pour chaque sommet de départ possible
    tmp = dijkstra(i, matrix)  # On utilise Dijkstra pour calculer toutes les distances composites depuis ce sommet
    for j in range(n):  # Pour chaque sommet d'arrivée possible
        # On extrait le nombre de ravitaillements uniquement (quotient euclidien par 10**15)
        ans[i][j] = tmp[j] // (10 ** 15)

for a, b in query:  # Pour chaque requête posée
    a -= 1  # On réajuste les indices à partir de 0
    b -= 1
    if ans[a][b] == 1000:  # Convention : si la distance est "impossible" (en pratique, si <= 1000 ravitos c'est possible)
        print(-1)  # On affiche -1 si la route est impossible
    else:
        print(ans[a][b])  # Sinon, on affiche le nombre minimal de ravitaillements nécessaires