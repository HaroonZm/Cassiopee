#!/usr/bin/env python3

# Importation du module sys pour utiliser des fonctionnalités du système, 
# comme la lecture d'entrée standard et la modification de la limite de récursion.
import sys

# Importation du module math pour des fonctions mathématiques avancées,
# qui n'est pas utilisé ici mais souvent importé par convention dans les concours.
import math

# Importation de fonctions bisect_right et bisect_left depuis le module bisect,
# utilisées pour la recherche binaire sur des listes triées
from bisect import bisect_right as br
from bisect import bisect_left as bl

# Modification de la limite maximale de la profondeur de récursion de Python.
# Utile si le code utilise la récursion profonde (ce qui n'est pas le cas ici,
# mais souvent fait pour des raisons de sécurité dans les problèmes d'algorithme).
sys.setrecursionlimit(2147483647)

# Importation de fonctions utiles pour gérer des files de priorité min-heap:
# heappush: ajoute un élément au tas,
# heappop: retire et retourne le plus petit élément du tas,
# heappushpop: pousse puis pop dans un seul mouvement.
from heapq import heappush, heappop, heappushpop

# Importation de defaultdict depuis collections qui permet d'avoir des dictionnaires
# avec une valeur par défaut, ce qui évite les erreurs de clé.
from collections import defaultdict

# Importation de accumulate depuis itertools, qui crée des accumulations (sommes partielles)
from itertools import accumulate

# Importation de Counter depuis collections, qui permet de compter les occurrences d'éléments dans une liste.
from collections import Counter

# Importation de deque (double-ended queue) depuis collections, 
# une file où l'on peut ajouter/enlever des éléments aux deux extrémités avec rapidité.
from collections import deque

# Importation de itemgetter depuis operator, utilisé pour obtenir des éléments à des positions spécifiques dans des objets.
from operator import itemgetter

# Importation de permutations depuis itertools, pour générer toutes les permutations possibles d'une séquence.
from itertools import permutations

# Définition d'une constante mod avec la valeur 10**9 + 7,
# une grande valeur première fréquemment utilisée pour prendre le reste lors de calculs
# afin d'éviter les surcharges de grands entiers. Non utilisée ci-dessous.
mod = 10**9 + 7

# Définition de l'infini positif, utilisé pour initialiser des distances infinies
# dans des algorithmes comme Dijkstra.
inf = float('inf')

# Fonction I: lit une ligne de l'entrée standard, supprime l'espace en fin de ligne,
# convertit la chaîne de caractères en entier et renvoie cet entier.
def I():
    return int(sys.stdin.readline())

# Fonction LI: lit une ligne de l'entrée standard, la divise en sous-chaînes avec split(),
# chaque sous-chaîne est convertie en entier avec map(int, ...), puis tout est converti en liste (list(...)).
# Cela est utile pour lire une liste d'entiers sur une seule ligne.
def LI():
    return list(map(int, sys.stdin.readline().split()))

# Définition de la fonction dijkstra qui calcule les plus courts chemins depuis
# un sommet source s dans un graphe pondéré à l'aide de l'algorithme de Dijkstra.
# Le graphe est attendu sous forme de liste d'adjacence, où chaque sommet a une liste
# de couples (voisin, coût).
def dijkstra(s, graph):
    # Création d'une liste pour stocker les distances minimales entre s et chaque sommet du graphe.
    # Elle est initialisée à l'infini pour tous les sommets.
    d = [inf]*n

    # La distance du sommet de départ s à lui-même est toujours 0.
    d[s] = 0

    # Initialisation du tas (heap) qui contiendra les sommets à traiter.
    # Le tas contiendra des tuples (distance, sommet).
    # On commence par mettre le sommet source avec une distance de 0.
    h = [(0, s)]

    # Boucle tant qu'il reste des éléments dans le tas, c'est-à-dire qu'il reste des sommets à explorer.
    while h:
        # On retire du tas le sommet avec la plus petite distance.
        c, v = heappop(h)

        # Si on a déjà trouvé une distance plus courte jusqu'à ce sommet,
        # on saute cette itération, car elle est obsolète.
        if d[v] < c:
            continue

        # Parcours de tous les voisins (t) du sommet v et des coûts associés.
        for t, cost in graph[v]:
            # Si le chemin passant par v vers t offre une distance plus courte,
            if d[v] + cost < d[t]:
                # On met à jour la distance minimale vers t.
                d[t] = d[v] + cost
                # Et on ajoute ce nouveau sommet à traiter dans le tas (avec sa nouvelle distance).
                heappush(h, (d[t], t))
    # Retourne la liste complète des distances minimales du sommet s à tous les sommets.
    return d

# Lecture des entiers n et m à partir de l'entrée standard.
# n représente le nombre de sommets (ou noeuds), m le nombre d'arêtes supplémentaires à lire ensuite.
n, m = LI()

# Initialisation d'une liste appelée edges, composée de n sous-listes vides.
# Chaque sous-liste edges[i] représentera la liste des voisins directs atteignables depuis le sommet i,
# chaque voisin étant représenté comme un tuple (sommet, coût).
edges = [[] for _ in range(n)]

# Cette boucle relie chaque sommet (sauf le premier) à son précédent (pour i variant de 1 à n-1) avec un coût de 0.
# Cela signifie que d'indice en indice, on peut avancer gratuitement.
for i in range(1, n):
    # edges[i] est la liste des voisins du sommet i.
    # On y ajoute le sommet i-1 avec un coût de 0.
    edges[i].append((i-1, 0))

# On lit ensuite m lignes décrivant des arêtes supplémentaires avec leur coût.
for _ in range(m):
    # Lecture de trois entiers sur la ligne: l (début), r (fin), c (coût).
    l, r, c = LI()
    # On ajoute une arête du sommet l-1 (en Python les indices commencent à 0) vers r-1 avec le coût c.
    edges[l-1].append((r-1, c))

# Calcul des distances minimales du sommet 0 à tous les autres sommets avec Dijkstra.
d = dijkstra(0, edges)

# Si la distance minimale au dernier sommet (indice n-1) reste l'infini, cela signifie qu'il n'est pas atteignable,
# donc on imprime -1 pour signaler l'absence de chemin.
if d[-1] == inf:
    print(-1)
# Sinon, on affiche la distance minimale trouvée du sommet 0 au sommet n-1.
else:
    print(d[-1])