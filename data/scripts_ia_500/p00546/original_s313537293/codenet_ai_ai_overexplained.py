from collections import deque  # Importation de deque depuis collections, pour créer une file à double extrémité (FIFO)
from heapq import heappush, heappop  # Importation de heappush et heappop pour gérer une file de priorité sous forme de tas binaire

# Lecture et conversion de quatre entiers séparés sur une même ligne d'entrée utilisateur
N, M, K, S = map(int, input().split())
# Lecture et conversion de deux entiers séparés sur une même ligne d'entrée utilisateur
P, Q = map(int, input().split())

# Création d'une liste C contenant K entiers convertis depuis les entrées, 
# chaque entier correspond à un indice d'une ville spéciale décrémenté de 1 (pour passer à une indexation base 0)
C = [int(input()) - 1 for i in range(K)]

# Création d'une liste G de N éléments, où chaque élément est une liste vide.
# Cette structure représente un graphe : chaque liste va contenir les voisins d'un sommet donné.
G = [[] for i in range(N)]

# Boucle qui s'exécute M fois pour lire les arêtes du graphe
for i in range(M):
    # Lecture de deux entiers représentant une arête entre deux noeuds a et b
    a, b = map(int, input().split())
    a -= 1  # Passage à une indexation base 0 pour a
    b -= 1  # Passage à une indexation base 0 pour b
    # Ajout du noeud b dans la liste des voisins de a
    G[a].append(b)
    # Ajout du noeud a dans la liste des voisins de b (graphe non orienté)
    G[b].append(a)

# Initialisation d'une liste D de taille N, avec une valeur par défaut égale à N pour chaque ville.
# Cette liste va contenir la distance minimale de chaque ville à la plus proche ville spéciale.
D = [N] * N

# Création d'une file (queue) à double extrémité vide pour faire une recherche en largeur (BFS)
que = deque()

# Pour chaque ville spéciale dans la liste C :
for c in C:
    D[c] = 0  # On marque la distance à elle-même comme 0
    que.append(c)  # On ajoute cette ville dans la file pour démarrer la BFS

# Boucle tant que la file n'est pas vide pour effectuer la recherche en largeur
while que:
    v = que.popleft()  # Extraction de la ville en tête de la file (FIFO)
    d = D[v]  # Récupération de la distance déjà calculée pour cette ville
    # Parcours de tous les voisins de la ville v
    for w in G[v]:
        # Si la distance de w a déjà été calculée (différente de N), on ignore pour éviter les répétitions
        if D[w] != N:
            continue
        D[w] = d + 1  # Mise à jour de la distance comme un cran plus loin que v
        que.append(w)  # Ajout de w à la file pour continuer la propagation

# Déclaration d'une très grande valeur INF représentant en pratique l'infini pour les distances initiales
INF = 10**18
# Initialisation d'une liste dist avec INF pour toutes les villes, représentant la distance minimale connue jusqu'à présent
dist = [INF] * N
dist[0] = 0  # La distance pour la ville de départ (indice 0) est 0, car on y est déjà

# Création d'une liste avec un tuple (distance, ville) pour implémenter un tas (file de priorité),
# Initialement, on met (0, 0) signifiant distance 0 pour ville 0
que = [(0, 0)]

# Variable c n'a pas été initialisée au départ, il faut l'initialiser
c = 0  # Cette variable semble compter le nombre d'itérations ou d'extractions faites, sans impact fonctionnel visible

# Boucle principale qui fonctionne tant qu'il y a des villes dans la file de priorité
while que:
    cost, v = heappop(que)  # Extraction de la ville ayant la plus petite distance estimée (min-heap)
    # Si la distance déjà trouvée pour la ville v est strictement inférieure à cost, ce chemin est ignoré
    if dist[v] < cost:
        continue

    c += 1  # Incrémentation du compteur d'itérations (pas essentiel pour le fonctionnement)

    # Parcours des villes voisines de v
    for w in G[v]:
        # Si la ville voisine est une ville spéciale (distance 0), on ne peut pas s'y rendre, on continue
        if D[w] == 0:
            continue
        # Si la ville est proche (distance à une ville spéciale <= S)
        if D[w] <= S:
            # Calcul du nouveau coût possible en se déplaçant vers w avec le coût Q
            if cost + Q < dist[w]:
                dist[w] = cost + Q  # Mise à jour de la distance minimale pour w
                heappush(que, (cost + Q, w))  # Ajout de w dans le tas avec sa nouvelle distance
        else:
            # Sinon, la ville est éloignée (distance à une ville spéciale > S)
            # Calcul du nouveau coût avec le coût P
            if cost + P < dist[w]:
                dist[w] = cost + P  # Mise à jour de la distance minimale pour w
                heappush(que, (cost + P, w))  # Ajout de w dans le tas avec sa nouvelle distance

# Affichage du résultat final : distance pour atteindre la dernière ville (indice N-1)
# On soustrait le coût Q si la ville finale est proche (distance <= S), sinon on soustrait P.
# Cette correction est faite car le dernier déplacement ajoute un coût superflu dans le calcul précédent.
print(dist[N - 1] - (Q if D[N - 1] <= S else P))