import heapq  # Importation du module heapq pour travailler avec les files de priorité (tas binaire)
from collections import deque  # Importation de deque (double-ended queue), non utilisé ici mais souvent pour les files
from enum import Enum  # Importation de Enum, non utilisé ici, permettrait de définir des énumérations
import sys  # Importation du module système (pour l'entrée/sortie ou configuration d'encodage, mais non utilisé)
import math  # Importation du module mathématique, non utilisé ici, pour accès à des fonctions math de base
from _heapq import heappush, heappop  # Importation des fonctions heappush et heappop pour manipuler les tas
import copy  # Importation de copy permettant de faire des copies d'objet (non utilisé ici)

# Définition d'une valeur très grande, utilisée comme l'infini pour initialiser des coûts minimaux (BIG_NUM)
BIG_NUM = 2000000000

# Définition d'une constante de module, souvent utilisée pour les opérations modulo, non utilisée ici (MOD)
MOD = 1000000007

# Définition d'une petite constante EPSILON, non utilisée ici (EPS)
EPS = 0.000000001

# Définition d'une classe représentant une arête dans un graphe
class Edge:
    def __init__(self, arg_to, arg_cost):
        # Attribut représentant le sommet de destination de l'arête
        self.to = arg_to
        # Attribut représentant le coût pour suivre cette arête
        self.cost = arg_cost

# Définition d'une classe Info utilisée pour stocker des informations sur un nœud pour l'algorithme de Dijkstra
class Info:
    def __init__(self, arg_node_id, arg_sum_cost):
        # Attribut stockant l'identifiant du nœud (entier)
        self.node_id = arg_node_id
        # Attribut stockant le coût cumulé pour atteindre ce nœud depuis la source
        self.sum_cost = arg_sum_cost

    # Définition d'une méthode qui permet de comparer deux objets Info selon leur sum_cost
    # Cette méthode permet d'utiliser les objets Info dans un tas binaire (min-heap)
    def __lt__(self, another):
        # On retourne True si le coût de self est inférieur à celui de another
        return self.sum_cost < another.sum_cost

# Lecture de l'entrée standard: le nombre de nœuds N et le nombre d'arêtes additionnelles R
N, R = map(int, input().split())

# Création du graphe sous forme de liste d'adjacence, G est une liste de listes d'arêtes.
# On met N+1 car les nœuds sont indexés de 1 à N, mais aussi on ajoute la racine 0.
G = [[] for _ in range(N + 1)]

# Création d'une liste pour stocker la 'valeur' associée à chaque nœud
# On met N+1 pour les mêmes raisons
value = [None] * (N + 1)

# Définition d'une variable root pour représenter la racine (identifiant 0)
root = 0

# Lecture des coûts pour aller de la racine vers chaque nœud et la valeur associée à chaque nœud
for i in range(1, N + 1):
    # Lecture de deux entiers : cost (coût de l'arête depuis root) et tmp (valeur du nœud)
    cost, tmp = map(int, input().split())
    # On ajoute une arête partant de root vers i de coût 'cost'
    G[root].append(Edge(i, cost))
    # On garde en mémoire la valeur associée au nœud i
    value[i] = tmp

# Pour chaque arête additionnelle à ajouter dans le graphe
for _ in range(R):
    # Lecture de trois entiers : destination, source, coût de l'arête
    to_, from_, cost = map(int, input().split())
    # Ajout d'une arête partant de 'from_' vers 'to_' avec coût 'cost - 1'
    # Le coût est décrémenté de 1 conformément à la logique du problème
    G[from_].append(Edge(to_, cost - 1))

# Initialisation d'une liste min_cost pour stocker le coût minimal pour atteindre chaque nœud depuis la racine
# Chaque nœud est initialisé avec un coût infiniment grand (BIG_NUM)
min_cost = [BIG_NUM] * (N + 1)

# Le coût pour atteindre la racine est 0 car on y est déjà
min_cost[root] = 0

# Initialisation de la file de priorité pour Dijkstra (ici une liste qui sera utilisée comme un tas)
Q = []

# On place dans le tas binaire une information indiquant que pour atteindre la racine il faut un coût 0
heappush(Q, Info(root, 0))

# Début de la boucle principale de l'algorithme de Dijkstra
# Tant qu'il y a au moins un élément dans la file de priorité
while len(Q) > 0:
    # Retire l'élément avec le plus petit coût cumulatif de la file de priorité (min-heap)
    info = heappop(Q)
    # Si on a déjà trouvé un chemin moins coûteux pour atteindre ce nœud, on passe
    if info.sum_cost > min_cost[info.node_id]:
        continue  # Passe à l'itération suivante de la boucle

    # Pour chaque arête accessible à partir du nœud courant
    for edge in G[info.node_id]:
        # Si on trouve un chemin vers le sommet d'arrivée 'edge.to' avec un coût inférieur à celui mémorisé
        if min_cost[edge.to] > info.sum_cost + edge.cost:
            # On met à jour le coût minimal pour atteindre ce sommet
            min_cost[edge.to] = info.sum_cost + edge.cost
            # On ajoute cette nouvelle situation à la file de priorité
            heappush(Q, Info(edge.to, min_cost[edge.to]))

# Initialisation d'une variable qui stockera la réponse finale
ans = 0

# Pour chaque nœud (hors la racine), on multiplie le coût minimal pour l'atteindre par la valeur de ce nœud
for i in range(1, N + 1):
    ans += min_cost[i] * value[i]  # Ajout au total

# On affiche le résultat final mis en forme comme un entier
print("%d" % (ans))