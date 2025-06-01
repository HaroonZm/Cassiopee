import heapq  # Importation du module heapq qui permet de gérer des files de priorité (tas min) en Python.
from collections import deque  # Importation de deque, une structure de données optimisée pour l'ajout/retrait aux deux extrémités.
from enum import Enum  # Importation d'Enum, qui permet de créer des enumerations (listes de constantes nommées).
import sys  # Importation du module sys donnant accès à des variables et fonctions liées à l'interpréteur Python.
import math  # Importation du module math, qui permet d'accéder à des fonctions mathématiques avancées.
from _heapq import heappush, heappop  # Importation directe des fonctions heappush et heappop depuis le module _heapq (pour manipuler un tas).
import copy  # Importation du module copy pour pouvoir effectuer des copies profondes d'objets complexes.
from test.support import _MemoryWatchdog  # Importation d'un outil interne de support de tests pour surveiller la mémoire (non utilisé ici).

# Définition de constantes numériques très grandes utilisées ultérieurement pour des comparaisons ou modulo
BIG_NUM = 2000000000  # Une grande valeur entière arbitraire.
HUGE_NUM = 99999999999999999  # Une très grande valeur entière arbitraire.
MOD = 1000000007  # Un grand nombre premier souvent utilisé comme modulo pour éviter les dépassements d'entiers.
EPS = 0.000000001  # Une très petite valeur epsilon pour des comparaisons flottantes.

# Modification de la limite maximale de récursion de Python à 100000
# sys.setrecursionlimit définit la profondeur maximale de la pile d'appels récursifs
sys.setrecursionlimit(100000)  

# Attribution d'indices entiers à des variables correspondant aux lettres J, O, I et combinaisons de ces lettres
J = 0  # Représente l'indice pour 'J'
O = 1  # Représente l'indice pour 'O'
I = 2  # Représente l'indice pour 'I'
JO = 3  # Représente l'indice pour la séquence "JO"
OI = 4  # Représente l'indice pour la séquence "OI"

num_JOI = 0  # Initialisation du compteur du nombre total de séquences "JOI"

# Lecture de la longueur N de la chaîne de caractères depuis l'entrée standard (entrée utilisateur)
N = int(input())

# Lecture de la chaîne de caractères input_str contenant les lettres 'J', 'O' et 'I'
input_str = input()

# Création d'une matrice dp (programmation dynamique) de taille (N+1) x 5 initialisée à 0
# dp[i][k] représente un cumul ou un comptage spécifique jusqu'à l'indice i (exclusif ou inclusif selon contexte)
dp = [[0]*(5) for _ in range(N+1)]  # Chaque sous-liste correspond à un état/statistique pour chaque position i

# Boucle sur chaque position i allant de 1 à N inclus (indices 1-based pour faciliter le calcul des sous-séquences)
for i in range(1,(N+1)):
    # Lecture du caractère à la position i-1 de la chaîne (car la chaîne est 0-indexée)
    if input_str[i-1] == "J":  # Si le caractère courant est 'J'
        dp[i][J] += 1  # On compte 1 occurrence de 'J' à cette position
    elif input_str[i-1] == "O":  # Si le caractère courant est 'O'
        dp[i][O] += 1  # On compte 1 occurrence de 'O'
        dp[i][JO] += dp[i-1][J]  # Le nombre de "JO" se met à jour en ajoutant le nombre de 'J' précédents (pour finir la séquence "JO")
    else: # input_str[i-1] == "I"  # Sinon, le caractère est 'I' par défaut
        dp[i][I] += 1  # On compte 1 occurrence de 'I'
        dp[i][OI] += dp[i-1][O]  # Le nombre de "OI" se met à jour en ajoutant le nombre de 'O' précédents (pour finir la séquence "OI")
        num_JOI += dp[i-1][JO]  # On increment le nombre total de séquences "JOI" par le nombre de "JO" déjà présentes avant

    # Mise à jour des sommes cumulées dans dp[i] en ajoutant les compteurs cumulés à la position précédente
    # Ceci permet d'avoir des compteurs cumulative afin d'accélérer les calculs futurs évitant de recalculer depuis le début
    for k in range(5):
        dp[i][k] += dp[i-1][k]  # Ajout de la somme cumulée précédente pour chaque type de compteur

# Calcul du maximum entre le nombre de séquences "JO" et "OI" à la dernière position (N)
# Ceci représente la meilleure contribution de séquences partielles proches des extrémités
maximum = max(dp[N][JO],dp[N][OI])  # On prend la plus grande valeur entre JO et OI pour commencer

# Boucle pour tester chaque caractère dans la chaîne afin d'identifier le maximum d'amélioration possible
# Cela consiste à essayer d'ajouter des séquences liées à O en diverses positions
for i in range(1,(N+1)):
    if input_str[i-1] == "J":  # Si le caractère est 'J'
        # On calcule un produit entre le nombre de 'J' jusqu'à i et le nombre d'I après i, et on compare avec maximum
        maximum = max(maximum,dp[i][J]*(dp[N][I]-dp[i][I]))
    elif input_str[i-1] == "O":  # Si le caractère est 'O'
        # Calcul similaire mais au décalage précédent pour 'J'
        maximum = max(maximum,dp[i-1][J]*(dp[N][I]-dp[i][I]))
    else:  # Si le caractère est 'I'
        # Prise en compte d'une unité supplémentaire pour l'extension de la séquence
        maximum = max(maximum,dp[i-1][J]*(dp[N][I]-dp[i][I]+1))

# Affichage final : somme du nombre total de séquences "JOI" déjà comptées plus la valeur maximale calculée
print("%d"%(num_JOI+maximum))  # On affiche ce résultat en format entier sans espace ni saut de ligne superflu.