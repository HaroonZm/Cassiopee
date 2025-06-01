import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

# Large constant used to represent infinity or a very large number
BIG_NUM = 2000000000

# Modulo constant (not used in this code, but commonly used in algorithmic problems)
MOD = 1000000007

# Epsilon for floating point comparison (not used here but defined)
EPS = 0.000000001

class Edge:
    """
    Classe représentant une arête dans un graphe pondéré.

    Attributs :
    ----------
    to : int
        Le noeud de destination de l'arête.
    cost : int
        Le coût ou poids associé à cette arête.
    """
    def __init__(self, arg_to, arg_cost):
        self.to = arg_to
        self.cost = arg_cost

class Info:
    """
    Classe utilisée pour stocker les informations nécessaires dans la file de priorité
    pendant l'exécution de l'algorithme de Dijkstra.

    Attributs :
    ----------
    node_id : int
        L'identifiant du noeud courant.
    sum_cost : int
        Le coût total minimal accumulé jusqu'à ce noeud depuis la source.
    
    Méthodes :
    ---------
    __lt__(another)
        Permet de comparer deux instances de Info selon leur coût total pour 
        permettre le bon fonctionnement de la heap.
    """
    def __init__(self, arg_node_id, arg_sum_cost):
        self.node_id = arg_node_id
        self.sum_cost = arg_sum_cost

    def __lt__(self, another):
        return self.sum_cost < another.sum_cost

# Lecture des entrées : N = nombre de noeuds, R = nombre de routes supplémentaires
N, R = map(int, input().split())

# Initialisation du graphe sous forme de liste d'adjacence.
# G[i] contiendra les arêtes issues du noeud i.
# On ajoute un noeud 'root' supplémentaire à l'indice 0, utilisé comme source initiale.
G = [[] for _ in range(N + 1)]

# Tableau des valeurs associées à chaque noeud (indexé de 1 à N).
value = [None] * (N + 1)

root = 0  # Noeud racine artificiel à partir duquel on connecte tous les noeuds initiaux

# Lecture des coûts initiaux et des valeurs correspondantes de chaque noeud
# On ajoute des arêtes allant du noeud racine vers chaque noeud i avec le coût donné
for i in range(1, N + 1):
    cost, tmp = map(int, input().split())
    G[root].append(Edge(i, cost))
    value[i] = tmp

# Lecture des R routes supplémentaires ensuite (arêtes dirigées)
for _ in range(R):
    to_, from_, cost = map(int, input().split())
    # On connecte l'arête de from_ vers to_ avec un coût réduit de 1 selon l'énoncé
    G[from_].append(Edge(to_, cost - 1))

# Initialisation du tableau des coûts minimaux pour atteindre chaque noeud
min_cost = [BIG_NUM] * (N + 1)
min_cost[root] = 0  # Coût d'atteindre la racine est zéro

# Initialisation d'une heap (file de priorité) pour l'algorithme de Dijkstra
Q = []

# On insère le noeud racine avec un coût nul
heappush(Q, Info(root, 0))

# Boucle principale de Dijkstra
while len(Q) > 0:
    info = heappop(Q)  # Extraire l'élément avec le coût minimal
    # Si on a déjà trouvé un meilleur chemin avant, on ignore cet élément
    if info.sum_cost > min_cost[info.node_id]:
        continue
    # Parcourir toutes les arêtes adjacentes au noeud courant
    for edge in G[info.node_id]:
        # Si un chemin plus court est trouvé vers edge.to
        if min_cost[edge.to] > info.sum_cost + edge.cost:
            # Mise à jour du coût minimal
            min_cost[edge.to] = info.sum_cost + edge.cost
            # Ajout dans la heap pour exploration ultérieure
            heappush(Q, Info(edge.to, min_cost[edge.to]))

# Calcul final de la somme pondérée des coûts minimaux par les valeurs associées à chaque noeud
ans = 0
for i in range(1, N + 1):
    ans += min_cost[i] * value[i]

# Affichage de la réponse finale
print("%d" % (ans))