# AOJ 2834 Dimension travel
# Python3 2018.7.12 bal4u (réécriture avec commentaires très détaillés)

# Définition d'une constante appelée INF qui représentera l'infini (ici la plus grande valeur entière positive possible dans un int 32 bits).
INF = 0x7fffffff  # 0x7fffffff est égal à 2147483647, c'est la limite supérieure d'un entier signé 32 bits.

# Importation du module heapq pour utiliser la file de priorité (heap),
# qui permet d'accéder et de modifier rapidement le plus petit élément selon l'ordre d'une clé choisie.
import heapq

# Définition de la fonction dijkstra pour trouver le plus court chemin d'un point de départ à une destination,
# adaptée à ce problème particulier.
# V : nombre de sommets dans le graphe
# to : liste d'adjacence, to[i] est la liste de sommets accessibles depuis i
# start : le sommet de départ
# goal : le sommet d'arrivée
def dijkstra(V, to, start, goal):
    # Création d'une liste appelée dist qui va stocker la distance la plus courte connue pour chaque sommet.
    # À l'initialisation, on suppose que tout est à l'infini (très loin).
    dist = [INF] * V

    # Création d'une nouvelle liste Q qui servira de file de priorité (priority queue) pour stocker
    # les couples (distance calculée, sommet atteignable). Elle commence vide.
    Q = []

    # On commence par définir que la distance pour atteindre le sommet de départ (start)
    # est 0 car on y est déjà.
    dist[start] = 0

    # On insère dans la file de priorité le premier couple (0, start) qui signifie que le sommet start est à une
    # distance 0 du départ.
    heapq.heappush(Q, (0, start))

    # Boucle principale de Dijkstra : tant que la file de priorité n'est pas vide, on continue à explorer.
    while Q:
        # On extrait de la file le couple (t, s) avec la plus petite distance t actuellement trouvée pour le sommet s.
        t, s = heapq.heappop(Q)

        # Si on a atteint le sommet but (goal), on stoppe la recherche car on est sûr que c'est la plus courte distance grâce à Dijkstra.
        if s == goal:
            break

        # Si la distance pour le sommet s dans dist est inférieure à t,
        # cela veut dire qu'il existe déjà un chemin plus court vers s, donc on saute cette itération.
        if dist[s] < t:
            continue

        # On explore tous les voisins e du sommet s selon la liste d'adjacence to.
        for e in to[s]:
            # On commence par supposer que le coût nt pour atteindre e est égal au coût déjà parcouru t.
            nt = t

            # Spécificité du problème : si le sommet voisin e a un numéro supérieur à s, 
            # on ajoute à nt le coût d[e] qui est stocké dans la liste d. Cela modélise un coût conditionnel.
            if e > s:
                nt += d[e]

            # Si la distance calculée nt pour e est strictement meilleure que la distance déjà connue dist[e],
            # alors on considère que l'on a trouvé un chemin plus court pour accéder à e et met à jour la distance.
            if dist[e] > nt:
                dist[e] = nt
                # On insère ce nouveau couple (nt, e) dans la file de priorité Q pour examiner les voisins de e par la suite.
                heapq.heappush(Q, (nt, e))

    # Quand la boucle est terminée, la solution est la distance pour atteindre le but goal (qui devrait être t ici),
    # donc on retourne la variable t qui contient la distance minimale trouvée pour atteindre goal à la sortie.
    return t

# On importe le module sys pour utiliser sys.exit, permettant d'arrêter le programme immédiatement.
import sys

# Lecture de la première ligne d'entrée et extraction de quatre entiers N, M, s, t
# N : nombre de sommets
# M : nombre d'arêtes (ou couloirs spéciaux)
# s : numéro du sommet de départ (1-indexé dans l'énoncé)
# t : numéro du sommet d'arrivée (1-indexé dans l'énoncé)
N, M, s, t = map(int, input().split())

# Dans l'énoncé les sommets sont numérotés à partir de 1, mais en Python on indexe les listes à partir de 0,
# donc on décrémente de 1 s et t pour passer à un système 0-indexé.
s, t = s - 1, t - 1

# Cas particulier : si on part d'un sommet s qui est plus loin ou égal à t, alors il n'y a rien à faire,
# la réponse est automatiquement 0 (on ne peut rien atteindre dans ce sens, ou il est déjà atteint).
if s >= t:
    print(0)
    sys.exit(0)  # Arrêt immédiat du programme car il n'y a rien de plus à faire.

# Lecture de la deuxième ligne d'entrée pour remplir la liste d,
# d[i] est le "coût dimensionnel" pour avancer depuis le sommet i (sauf pour des arêtes spéciales).
d = list(map(int, input().split()))

# Construction de la liste d'adjacence to :
# Pour chaque sommet i (de 0 à N-1), 
#   - si i > 0 (tous sauf le premier sommet), alors il peut accéder à i-1 par une arête normale,
#   - sinon, la liste est vide (le sommet 0 n'a pas de voisin dans ce cas basique).
to = [[i - 1] if i > 0 else [] for i in range(N)]

# Pour les M arêtes spéciales, lecture et ajout direct dans la liste d'adjacence.
for i in range(M):
    # Lecture de deux entiers a et b pour chaque arête spéciale,
    # il y a un passage qui permet d'aller du sommet a-1 vers le sommet b-1 (0-indexé).
    a, b = map(int, input().split())
    to[a - 1].append(b - 1)

# Calcul du plus court chemin entre s et t avec la fonction dijkstra.
# Puis impression de la solution.
print(dijkstra(N, to, s, t))