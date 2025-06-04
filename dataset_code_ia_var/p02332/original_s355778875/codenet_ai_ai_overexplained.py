import bisect  # Module pour la recherche dichotomique dans des listes triées (non utilisé ici, importé pour référence)
import collections  # Module fournissant des structures de données alternatives comme deque, Counter, etc. (non utilisé ici)
import copy  # Module permettant de copier des objets (non utilisé ici)
import heapq  # Module pour utiliser des tas/min-heaps (non utilisé ici)
import itertools  # Module permettant de travailler avec des itérateurs efficaces (non utilisé ici)
import math  # Module pour des fonctions mathématiques avancées (non utilisé ici)
import string  # Module pour des opérations sur les chaînes de caractères (non utilisé ici)
import sys  # Module utilisé pour interagir avec l'interpréteur Python (ici, pour la lecture rapide de l'entrée)

# Définition d'une fonction lambda pour lire une ligne de l'entrée standard, retirer le caractère de retour à la ligne à la fin
input = lambda: sys.stdin.readline().rstrip()

# Permet d'augmenter la profondeur maximale de récursion autorisée par Python
# Cela peut être utile si vous utilisez la récursion profonde dans vos fonctions
sys.setrecursionlimit(10**7)  # Définit la limite de récursion à 10 000 000

# Définition de la constante représentant l'infini, souvent utilisée dans les algorithmes de graphes ou d'optimisation
INF = float('inf')  # Crée un nombre en virgule flottante qui représente l'infini

# Définition de la constante du module, souvent utilisée pour faire des opérations modulaires afin d'éviter les débordements d'entiers
MOD = 10**9 + 7  # 1 000 000 007, un nombre premier utilisé fréquemment dans les problèmes d'algorithmique

# Définition de fonctions utilitaires pour faciliter la lecture d'entrée et la conversion de types

# Fonction pour lire un entier de l'entrée standard
def I():
    return int(input())

# Fonction pour lire un nombre flottant de l'entrée standard
def F():
    return float(input())

# Fonction pour lire une chaîne de caractères de l'entrée standard
def SS():
    return input()

# Fonction pour lire une ligne de l'entrée standard, diviser la chaîne en sous-chaînes (mots séparés par des espaces), 
# et convertir chaque sous-chaîne en entier, puis retourner la liste des entiers.
def LI():
    return [int(x) for x in input().split()]

# Fonction pour lire une ligne de l'entrée standard, diviser la chaîne en sous-chaînes, convertir chaque sous-chaîne en entier,
# puis soustraire 1 à chaque entier. Ceci est communément utilisé pour convertir les indices 1-based en 0-based.
def LI_():
    return [int(x)-1 for x in input().split()]

# Fonction pour lire une ligne de l'entrée standard, diviser la chaîne en sous-chaînes, convertir chaque sous-chaîne en flottant,
# puis retourner la liste des flottants.
def LF():
    return [float(x) for x in input().split()]

# Fonction pour lire une ligne de l'entrée standard et la diviser en sous-chaînes (mots), en retournant la liste des chaînes.
def LSS():
    return input().split()

# Définition de la fonction principale qui résout le problème
def resolve():
    # Lecture de deux entiers depuis l'entrée, en utilisant la fonction LI définie ci-dessus
    # Par exemple, si l'utilisateur saisit "4 3", n vaudra 4, k vaudra 3
    n, k = LI()  # n et k sont deux entiers lus de l'entrée

    # Condition pour déterminer lequel des deux cas appliquer
    if n <= k:
        # Si n est inférieur ou égal à k, alors nous pouvons sélectionner n éléments distincts parmi k dans un certain ordre
        # Nous allons calculer le nombre de façons de faire cela : k * (k-1) * (k-2) ... * (k-n+1), ce qui est une "permutation"
        ans = 1  # Initialisation du nombre de façons à 1 (car multiplier par 1 ne change pas la valeur)
        for i in range(n):  # Pour chaque entier i de 0 à n-1 (nous faisons n itérations)
            # À chaque étape, on multiplie la réponse courante par (k - i),
            # ce qui correspond à réduire le nombre d'éléments disponibles à choisir à chaque itération
            ans *= (k - i)  # Multiplie le résultat courant par le nombre d'éléments restants disponibles
            ans %= MOD  # Prend le reste de la division euclidienne de ans par MOD
            # Cela permet d'éviter que ans ne devienne trop grand et déborde
    else:
        # Si n est strictement supérieur à k, il est impossible de choisir n éléments distincts parmi k,
        # donc il n'y a aucune façon de faire cela
        ans = 0  # On fixe ans à 0 car aucune combinaison n'est possible

    # On affiche la réponse finale à l'utilisateur en utilisant la fonction print intégrée à Python
    print(ans)

# Ceci vérifie si le script est exécuté en tant que programme principal
# Si c'est le cas, alors on appelle la fonction resolve()
if __name__ == '__main__':
    resolve()