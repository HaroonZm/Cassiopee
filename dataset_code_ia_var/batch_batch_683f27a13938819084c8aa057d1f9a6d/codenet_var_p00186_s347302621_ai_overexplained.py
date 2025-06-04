# Importation du module heapq, pour utiliser des structures de données de file de priorité (tas/min-heap).
import heapq
# Importation de deque depuis collections, pour créer des files de type deque (double-ended queue).
from collections import deque
# Importation de Enum depuis enum, pour pouvoir définir des énumérations (types énumérés).
from enum import Enum
# Importation du module sys, principalement utilisé ici pour changer la limite de récursion.
import sys
# Importation du module math, qui fournit des fonctions mathématiques de base (non utilisé ici).
import math
# Importation spécifique des fonctions heappush et heappop du module _heapq, pour manipuler un tas.
from _heapq import heappush, heappop
# Importation du module copy, qui permet de copier des objets (non utilisé ici).
import copy
# Importation d'une fonction interne _MemoryWatchdog pour surveiller la mémoire (non utilisée ici).
from test.support import _MemoryWatchdog

# Déclaration et initialisation d'une variable entière très grande, servant de constante ou pour initialiser des bornes supérieures.
BIG_NUM = 2000000000
# Déclaration d'une variable avec une valeur énorme, probablement jamais atteinte dans un calcul normal.
HUGE_NUM = 99999999999999999
# Déclaration d'une constante pour un modulo couramment utilisé pour éviter le débordement lors de grands calculs.
MOD = 1000000007
# Déclaration d'une constante utilisée pour gérer les comparaisons de flottants (epsilon, petite valeur).
EPS = 0.000000001
# Modification de la limite par défaut de récursion dans l'interpréteur Python à 100000 pour éviter l'erreur RecursionError dans des cas extrêmes.
sys.setrecursionlimit(100000)

# Boucle infinie. Sert à lire plusieurs jeux de données depuis l'entrée standard jusqu'à l'apparition d'un indicateur de fin.
while True:
    # Lecture d'une ligne depuis l'entrée standard (typiquement depuis le clavier ou un fichier).
    input_str = input()
    # Si la ligne comporte exactement un caractère et qu'il s'agit du chiffre 0, on considère qu'il faut arrêter la boucle.
    if len(input_str) == 1 and input_str[0] == "0":
        break  # On sort de la boucle while.

    # Découpage de la chaîne lue en utilisant les espaces comme séparateurs, puis transformation en entiers.
    need, budget, aizu, normal, limit = map(int, input_str.split())

    # Initialisation de la borne inférieure (left) à 1, et de la borne supérieure (right) à la valeur de 'limit'.
    left = 1
    right = limit
    # Calcul initial de la moyenne des bornes, arrondie à l'entier inférieur (division entière).
    mid = (left + right) // 2
    # Initialisation des variables pour stocker la meilleure combinaison d'objets trouvée.
    num_aizu = 0
    num_normal = 0

    # Début d'une boucle de recherche dichotomique (binaire) : on cherche le maximum de 'mid' sous certaines contraintes.
    while left <= right:
        # Calcul du budget restant après avoir acheté 'mid' objets de type 'aizu'.
        rest = budget - mid * aizu
        # Calcul du nombre d'objets de type 'normal' que l'on peut acheter avec le reste du budget.
        tmp_normal = rest // normal
        # Condition vérifiant si on a un budget suffisant (rest >= 0) ET le nombre total d'objets est suffisant (mid+tmp_normal >= need).
        if rest >= 0 and mid + tmp_normal >= need:
            # Si c'est possible, on enregistre cette combinaison (c'est pour le maximum de 'mid' trouvé jusqu'à présent).
            num_aizu = mid
            num_normal = tmp_normal
            # On essaie d'acheter davantage d'objets 'aizu', donc on remonte la borne gauche.
            left = mid + 1
        else:
            # Sinon, cela veut dire qu'on a dépassé les capacités du budget ou du besoin, donc on baisse la borne droite.
            right = mid - 1
        # Mise à jour de la valeur centrale pour la prochaine itération.
        mid = (left + right) // 2

    # Après la boucle de recherche binaire, on vérifie si une solution acceptable a été trouvée (num_aizu != 0).
    if num_aizu == 0:
        # Si aucune solution n'a été trouvée, on affiche 'NA' pour indiquer l'impossibilité.
        print("NA")
    else:
        # Sinon, on affiche le nombre d'objets 'aizu' et 'normal' choisis, formatés comme des entiers séparés par un espace.
        print("%d %d" % (num_aizu, num_normal))