import math  # Importe le module 'math' qui fournit des fonctions mathématiques de base comme sqrt, sin, cos, etc.
import time  # Importe le module 'time' qui permet de manipuler le temps, mesurer la durée, faire des pauses, etc.
from collections import defaultdict, deque  # Importe 'defaultdict' (dictionnaire avec valeur par défaut) et 'deque' (double-ended queue pour gérer efficacement les files et piles).
from sys import stdin, stdout  # Importe 'stdin' (entrée standard, généralement le clavier) et 'stdout' (sortie standard, généralement l'écran).
from bisect import bisect_left, bisect_right  # Importe les fonctions 'bisect_left' et 'bisect_right' du module 'bisect' permettant de rechercher des indices d'insertion dans une liste triée.

# Les lignes suivantes, commençant par '#', sont des commentaires et ne sont pas exécutées.
# Elles contiennent un exemple de boucle pour gérer plusieurs cas de test, souvent utilisé en programmation compétitive.
# t=int(input())  # Demande à l'utilisateur d'entrer le nombre de cas de test et convertit la chaîne en entier.
# for _ in range(t):  # Boucle pour traiter chaque cas de test.
#     n,m=map(int,stdin.readline().split())  # Lit une ligne, la découpe selon les espaces, convertit chaque élément en entier et les assigne à n et m.

k = int(stdin.readline())  # Lit une ligne depuis l'entrée standard (généralement via le clavier), la convertit en entier, et stocke cette valeur dans la variable 'k'.
s = input()  # Demande à l'utilisateur de saisir une chaîne de caractères et la stocke dans la variable 's'.

# La condition suivante vérifie si la longueur de la chaîne 's' est inférieure ou égale à la valeur 'k'.
if len(s) <= k:
    print(s)  # Si c'est le cas, affiche simplement la chaîne 's' sans modification.
else:
    # Sinon, affiche les 'k' premiers caractères de 's',
    # ce qui est fait grâce à l'opérateur de découpage (slice) s[:k].
    # Ajoute ensuite trois points à la suite grâce à l'opérateur '+' pour indiquer que la chaîne a été tronquée.
    print(s[:k] + '...')  # Affiche la version raccourcie suivie de '...'.