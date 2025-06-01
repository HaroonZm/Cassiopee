from collections import deque  # Importation de la classe deque, une liste optimisée pour les opérations en file ou pile
from heapq import heappop, heappush  # Importation des fonctions pour gérer une file de priorité sous forme de tas binaire (heap)
inf = float("INF")  # Définition d'une constante 'inf' représentant l'infini, ici un float infini positif
dq = []  # Initialisation d'une liste vide qui sera utilisée comme une file de priorité (tas)

# Lecture des 4 entiers séparés par un espace depuis l'entrée standard, puis décomposition dans variables n,m,k,s
n, m, k, s = map(int, input().split())

# Lecture des 2 entiers p et q, précédemment sur la même ligne
p, q = map(int, input().split())

c = [0] * k  # Création d'une liste de taille k initialisée à zéro. Elle contiendra la liste des sommets spéciaux
z_dist = [inf] * n  # Liste de distances initialisée à l'infini pour chaque sommet parmi n sommets

# Pour chaque sommet spécial, on va lire son index, ajuster l'index pour commencer à zéro et initialiser sa distance à zéro
for i in range(k):
    c[i] = int(input()) - 1  # Lecture de l'indice du sommet spécial, conversion en index 0-based
    z_dist[c[i]] = 0  # La distance du sommet spécial à lui-même est zéro
    heappush(dq, (0, c[i]))  # On pousse un tuple (distance, sommet) dans la file de priorité dq

# Création d'une liste de listes vide avec m listes intérieures pour représenter un graphe non orienté (adjacences)
g = [[] for i in range(m)]
# Listes d’arêtes avec leurs extrémités, initialisé à 0
a = [0] * m
b = [0] * m

# Lecture de m arêtes, chaque arête reliant deux sommets aj et bj
for j in range(m):
    aj, bj = map(int, input().split())
    g[aj - 1].append(bj - 1)  # Ajout de l’arête dans la liste d’adjacence de aj (en index 0-based)
    g[bj - 1].append(aj - 1)  # Graphe non orienté : ajout également dans l'autre sens
    a[j] = aj - 1  # Stockage de l’extrémité a de l’arête j, 0-based
    b[j] = bj - 1  # Stockage de l’extrémité b de l’arête j

cc = [p] * n  # Initialisation de la liste cc où chaque sommet a un coût initial p

# Boucle pour un algorithme de plus court chemin partant des sommets spéciaux contenus dans dq
while dq:
    total, node = heappop(dq)  # Extraction de l’élément avec la plus petite distance (total) et son sommet (node)
    for to in g[node]:  # Pour chaque voisin (adjacent) du sommet courant
        if z_dist[to] > total + 1:  # Si on a trouvé une distance plus courte via ce chemin (total+1)
            z_dist[to] = total + 1  # Mise à jour de la distance minimale pour ce sommet
            heappush(dq, (total + 1, to))  # Ajout de ce nouveau sommet avec sa nouvelle distance dans la file de priorité

# Après calcul des distances minimales z_dist, on met à jour les coûts cc : ceux à distance ≤ s ont coût q
for i in range(n):
    if z_dist[i] <= s:
        cc[i] = q  # Remplacement du coût p initial par q pour ces sommets proches des spéciaux

# Recréation du graphe g comme liste d’adjacence mais cette fois chaque arête est pondérée par le coût de destination
g = [[] for i in range(n)]

# On parcourt les arêtes initiales et on ne les conserve que si ni a[i] ni b[i] ne sont dans la liste des sommets spéciaux c
for i in range(m):
    if (not a[i] in c) and (not b[i] in c):
        # Ajout d’arêtes pondérées dans les deux directions, le poids étant le coût associé au sommet de destination cc[]
        g[a[i]].append((b[i], cc[b[i]]))
        g[b[i]].append((a[i], cc[a[i]]))

hq = []  # Nouvelle file de priorité vide pour l’algorithme de Dijkstra sur ce nouveau graphe pondéré
rst = 0  # Sommet de départ fixé à 0 (premier sommet)

heappush(hq, (0, rst))  # On ajoute le sommet de départ avec distance 0 à la file prioritaire

dist = [inf] * n  # Tableau des distances initialisées à l’infini pour tous les sommets
dist[rst] = 0  # Distance du sommet de départ à lui-même vaut 0

# Algorithme de Dijkstra pour calculer les plus courts chemins depuis le sommet rst
while len(hq) > 0:
    dd, state = heappop(hq)  # Extraction du sommet avec la plus petite distance estimée (dd)
    for v, dv in g[state]:  # Pour chacun des voisins du sommet 'state' avec un coût de trajet dv
        if dist[v] > dist[state] + dv:  # Si un chemin plus court a été trouvé vers v via state
            dist[v] = dist[state] + dv  # Mise à jour de la distance la plus courte vers v
            heappush(hq, (dist[v], v))  # Ajout ou mise à jour du sommet dans la file de priorité

# Affichage du résultat final qui correspond à la distance minimale pour atteindre le dernier sommet (n-1) en soustrayant le coût du sommet d’arrivée
print(dist[n-1] - cc[n-1])  # Affiche la distance minimale corrigée pour ne pas compter deux fois le coût du dernier sommet