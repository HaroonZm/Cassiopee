import sys  # Le module sys permet d'accéder à certaines fonctions système de Python, ici pour lire les entrées.
def input():
    # Redéfinition de la fonction input pour lire une ligne sur stdin (entrée standard), sous forme binaire,
    # en excluant le dernier caractère (le saut de ligne '\n').
    # sys.stdin.buffer.readline() lit une ligne en bytes ; [:-1] enlève le dernier byte (qui est généralement \n).
    return sys.stdin.buffer.readline()[:-1]

from heapq import heappush, heappop  # Importation des fonctions pour utiliser une file de priorité (heap).

# Lire trois entiers x, y et z de la première ligne de l'entrée.
# input() lit la ligne, split() la divise en éléments, map(int, ...) convertit chaque élément en entier.
x, y, z = map(int, input().split())

# Lecture du tableau c de x + y + z lignes suivantes.
# Chaque ligne contient trois entiers, qui sont regroupés dans une liste [a, b, c] grâce à map(int, ...).
# La compréhension de liste répète cette opération x + y + z fois.
c = [list(map(int, input().split())) for _ in range(x + y + z)]

# Tri du tableau c selon la différence entre son 2e et 1er élément, c'est-à-dire c[i][1] - c[i][0].
# Le tri est effectué in-place.
c.sort(key=lambda x: x[1] - x[0])

# Initialisation de deux listes ans_l et ans_r pour stocker des résultats intermédiaires.
# Elles contiendront, respectivement, des sommes maximales lors de sélections à gauche et à droite.
# Chaque position est initialisée à -1.
ans_l = [-1 for _ in range(x + y + z)]
ans_r = [-1 for _ in range(x + y + z)]

# SECTION : Calcul des sélections à gauche (grouper les x + z premiers selon la valeur du 1er élément)
tmp = 0        # Initialisation d'une variable temporaire pour la somme courante.
l = []         # Initialisation d'un min-heap vide (pour suivre les éléments à potentiellement échanger plus tard).

# Pour les x premiers éléments, ajouter la 1ère valeur de chaque ligne à tmp.
for i in range(x):
    tmp += c[i][0]  # Ajout de c[i][0], c’est-à-dire la "valeur de la sélection gauche" à la somme temporaire.
    # On place dans le tas un couple (différence entre la sélection gauche et la valeur d'échange, index).
    heappush(l, (c[i][0] - c[i][2], i))

# On stocke dans ans_l[x] la somme obtenue après avoir choisi les x premiers, sans échanges.
ans_l[x] = tmp

# Ensuite, pour chaque élément parmi les z suivants (jusqu'à x+z non inclus), on ajoute la nouvelle sélection et gère les échanges.
for i in range(x, x + z):
    tmp += c[i][0]  # On ajoute le nouvel élément dans la sélection de gauche.
    heappush(l, (c[i][0] - c[i][2], i))  # Ajout dans le tas pour potentiellement le retirer ensuite.
    p = heappop(l)  # On enlève l'élément le moins intéressant (le min selon la différence stockée).
    tmp -= c[p[1]][0]  # On retire la valeur précédente de gauche pour l'élément échangé.
    tmp += c[p[1]][2]  # On ajoute sa valeur "d'échange" (côté neutre).
    ans_l[i + 1] = tmp  # On sauvegarde la somme obtenue après chaque opération.

# SECTION : Calcul des sélections à droite (grouper les y + z derniers selon la valeur du 2e élément)
tmp = 0         # Réinitialisation de la variable temporaire pour la somme courante.
r = []          # Nouveau min-heap vide pour gérer la sélection de droite.

# Pour les y derniers éléments (après x+z-1 jusqu'à la fin), on calcule la somme des valeurs de droite.
for i in range(x + z, x + y + z):
    tmp += c[i][1]  # Ajout de c[i][1] : valeur de la sélection droite.
    heappush(r, (c[i][1] - c[i][2], i))  # On conserve l'élément avec sa différence pour les échanges.

# On mémorise, en ans_r[x+z], la somme initiale obtenue à droite sans échanges.
ans_r[x + z] = tmp

# On étend la sélection à droite, en parcourant à rebours les z éléments précédant la sélection.
for i in range(x + z - 1, x - 1, -1):
    tmp += c[i][1]  # On ajoute la prochaine valeur de droite à la somme.
    heappush(r, (c[i][1] - c[i][2], i))  # Ajout dans le tas.
    p = heappop(r)  # On retire l'élément le moins intéressant de la sélection.
    tmp -= c[p[1]][1]  # On retire la valeur droite correspondante.
    tmp += c[p[1]][2]  # On ajoute sa valeur "d'échange".
    ans_r[i] = tmp  # On sauvegarde cette nouvelle somme.

# SECTION : Calcul du score maximal en combinant gauche et droite.
ans = 0  # Initialisation du résultat final à 0.
# On parcourt tous les indices où une division entre gauche et droite est possible (délimités par x et x+z inclus).
for i in range(x, x + z + 1):
    # On additionne la somme de gauche et de droite, et garde le maximum.
    ans = max(ans, ans_l[i] + ans_r[i])

# Affichage du résultat final.
print(ans)