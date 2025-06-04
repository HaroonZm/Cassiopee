import sys  # Le module sys permet d'utiliser des fonctionnalités système, comme la modification de la récursion maximale autorisée.
sys.setrecursionlimit(10**7)  # Modifie la limite de récursion maximale autorisée à 10 millions, utile pour éviter les erreurs de récursion maximale dans certains algorithmes récursifs.
import math  # Le module math fournit des fonctions mathématiques de base comme sqrt, ceil, etc. (bien que non utilisé explicitement ici).
from collections import defaultdict  # defaultdict est une sous-classe de dict qui fournit une valeur par défaut pour les clés absentes.

# Définition d'une constante. Généralement utilisée comme valeur de modulo dans les problèmes de programmation compétitive.
mod = 10**9 + 7  # Un nombre premier souvent pris pour effectuer des opérations de modulo afin d'éviter les débordements d'entiers et pour ses propriétés mathématiques.

# Définition de fonctions de lecture d'entrée pour faciliter la récupération et le formatage des données depuis l'entrée standard.
def I(): 
    # La fonction input() lit une ligne au format texte (str),
    # int() convertit ce texte en entier. 
    return int(input())

def II(): 
    # input().split() sépare la ligne en morceaux (str), map(int, ...) convertit chaque morceau en entier,
    # retourne un itérable d'entiers correspondants aux valeurs de l'entrée séparées par des espaces.
    return map(int, input().split())

def III(): 
    # Comme II() mais renvoie la liste directement au lieu d'un itérateur.
    return list(map(int, input().split()))

def Line(N):
    # Lit N lignes depuis l'entrée utilisateur.
    # Pour chaque ligne, on split et on convertit chaque valeur en int, puis on en fait un tuple.
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    # zip(*read_all) transpose la liste de tuples pour obtenir des listes composées de la i-ème valeur de chaque ligne.
    # map(list, ...) convertit chaque groupe transposé en une liste.
    return map(list, zip(*read_all))

# Lecture de l'entrée du problème pour la donnée principale.
N = I()  # Lit un entier N (représentant généralement une taille ou un nombre d'éléments).

# Lecture de la liste principale d'entiers ; la première position (index 0) est mise à zéro par convention pour simplifier l'indexation à partir de 1.
a = [0] + III()

# Importation des fonctions utiles de la bibliothèque heapq.
from heapq import heapify, heappush, heappop  # Permettent d'utiliser des files de priorité, c'est-à-dire des tas (min-heap ou max-heap).

# Initialisation des tableaux red et blue pour les scores cumulés.
# On les dimensionne à 3*N+1 pour que les indices utilisés soient toujours valides. Chaque case est initialisée à 0.
red = [0] * (3 * N + 1)
blue = [0] * (3 * N + 1)

# Préparation du premier tas (heap) pour les éléments "rouges".
# q1 contiendra les N premiers éléments de la liste a (hors l'élément fictif d'index 0).
q1 = a[1:N + 1]  # Sélection des N premiers éléments de a, indices 1 à N inclus.

# Calcul initial du score rouge pour l'indice N.
red[N] = sum(q1)  # La valeur initiale de red[N] est la somme des N premiers éléments.

# Convertir la liste q1 en un tas (heap).
heapify(q1)  # Transforme la liste q1 en min-heap, ce qui permet d'extraire toujours la plus petite valeur rapidement.

# Remplissage des scores rouges pour tous les indices de N+1 à 2N inclus.
for k in range(N + 1, 2 * N + 1):
    heappush(q1, a[k])  # Ajoute l'élément à la position k dans le min-heap.
    # On ajoute le nouvel élément au score, puis on retire la plus petite valeur (q1[0]) pour ne garder que N éléments maximum, et on ajuste le score.
    red[k] = red[k - 1] + a[k] - q1[0]  
    heappop(q1)  # On retire la plus petite valeur afin de conserver seulement les N plus grandes valeurs.

# Préparation du second tas, pour les éléments "bleus".
# q2 contiendra les N derniers éléments de la liste a.
q2 = a[2 * N + 1:3 * N + 1]  # Sélection des N éléments entre les indices 2N+1 et 3N (inclus).

blue[2 * N] = sum(q2)  # Initialisation du score bleu à l'indice 2N avec la somme de ces éléments.

# On crée un max-heap en stockant des couples (-x, x) pour chaque élément x (puisque heapq ne fournit qu'un min-heap).
q2 = [(-x, x) for x in q2]  # On associe à chaque x son opposé -x, en vue de créer un tas basé sur -x.
heapify(q2)  # Transforme la liste q2 en un heap basé sur les -x (max-heap simulé).

# Remplissage des scores bleus pour tous les indices allant de N à 2N-1 (inclus), en ordre décroissant.
for k in range(N, 2 * N)[::-1]:  # On parcourt les indices de 2N-1 jusqu'à N en descendant.
    # Ajoute à q2 le couple (-a[k+1], a[k+1]) pour, lors du prochain pop, potentiellement supprimer la valeur maximale actuelle.
    heappush(q2, (-a[k + 1], a[k + 1]))
    # On met à jour le score bleu à l'indice k : on prend le score au prochain indice, on ajoute a[k+1], puis on retire la plus grande valeur du heap (q2[0][1]).
    blue[k] = blue[k + 1] + a[k + 1] - q2[0][1]
    heappop(q2)  # On retire la plus grande valeur actuelle pour ne conserver à chaque fois que les N éléments les plus petits (en quelque sorte).

# Initialisation de la variable de réponse avec la plus petite valeur possible (ici, l'opposé de l'infini flottant).
ans = -float('inf')

# Recherche du maximum de la différence entre le score rouge et le score bleu sur l'intervalle demandé.
for i in range(N, 2 * N + 1):  # On parcourt tous les indices de N à 2N inclus.
    temp = red[i] - blue[i]  # Calcule la différence de score pour l'indice courant.
    if temp > ans:  # Si cette différence dépasse la valeur actuelle de ans,
        ans = temp  # on la met à jour.

# Affichage du résultat final. 
print(ans)  # Affiche la meilleure valeur trouvée pour la différence entre le score rouge et le score bleu.