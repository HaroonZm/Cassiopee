# Importation de modules standards Python qui offrent des fonctions et structures de données communes
from collections import defaultdict, deque, Counter  # defaultdict: dictionnaire avec valeur par défaut; deque: file double; Counter: compteur d'éléments
from heapq import heappush, heappop, heapify        # Fonctions pour la manipulation de files de priorité (tas binaire min)
import math                                         # Module mathématique standard pour les fonctions comme sqrt, log, etc.
import bisect                                       # Permet l'insertion et la recherche efficace dans des listes triées
import random                                       # Fournit des fonctions pour générer des nombres pseudo-aléatoires
from itertools import permutations, accumulate, combinations, product  # Fonctions pour créer/générer des itérateurs complexes
import sys                                          # Accès à certaines variables/fonctions système, comme stdin
import string                                       # Accès à des chaînes de caractères courantes (ascii_letters, digits, etc.)
from bisect import bisect_left, bisect_right         # Fonctions pour trouver la position d'insertion à gauche/droite dans une liste triée
from math import factorial, ceil, floor              # Import direct de certaines fonctions mathématiques : factorielle, plafond, plancher
from operator import mul                            # Fonction pour la multiplication (utilisée dans reduce, par ex)
from functools import reduce                        # Fonction pour appliquer une opération cumulée sur un itérable

# Modification de la limite maximale de récursion, c'est à dire le nombre d'appels imbriqués autorisé avant une erreur
# 2 147 483 647 est la valeur maximale d'un entier signé sur 32 bits (large limite pour ne plus jamais recevoir RecursionError)
sys.setrecursionlimit(2147483647)

# Affectation d'une valeur très grande qui jouera probablement le rôle d'infini (INF = 10^13)
INF = 10 ** 13

# Définition de fonctions utilitaires concises pour lire l'entrée standard (sys.stdin), utiles pour les compétitions
def LI():
    # Lit une ligne depuis l'entrée standard, divise la chaîne en éléments via split() et convertit chaque élément en entier
    return list(map(int, sys.stdin.readline().split()))
def I():
    # Lit une ligne depuis l'entrée standard et la convertit en entier
    return int(sys.stdin.readline())
def LS():
    # Lit une ligne depuis l'entrée standard (au format binaire), supprime les espaces en fin de ligne,
    # décode en UTF-8, et coupe la chaîne en une liste de mots
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S():
    # Lit une ligne depuis l'entrée standard (en binaire), supprime les espaces en fin, et la décode en UTF-8
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n):
    # Lis n entiers (un par ligne) et les retourne sous forme de liste
    return [I() for i in range(n)]
def LIR(n):
    # Lis n lignes d'entiers et retourne une liste de listes d'entiers
    return [LI() for i in range(n)]
def SR(n):
    # Lis n lignes de texte et retourne une liste de chaînes
    return [S() for i in range(n)]
def LSR(n):
    # Lis n lignes, chacune transformée en liste de mots (split) et retourne une liste de telles listes
    return [LS() for i in range(n)]
def SRL(n):
    # Lis n lignes, dont chacune est convertie en liste de caractères (chaque caractère devient un élément)
    return [list(S()) for i in range(n)]
def MSRL(n):
    # Lis n lignes de chiffres sous forme de texte, transforme chaque caractère de chaque ligne en entier,
    # puis retourne la liste de listes résultantes
    return [[int(j) for j in list(S())] for i in range(n)]

# Déclaration du modulo à utiliser pour les calculs (modulo très courant en compétitions, ici 10^9+7 : nombre premier grand)
mod = 10 ** 9 + 7

# Lecture d'un entier n depuis l'entrée standard ; variable correspondant typiquement à la taille des données du problème
n = I()

# Lecture d'une liste d'entiers H depuis l'entrée standard,
# puis ajout de la valeur 1 à la fin de la liste (cela protège souvent contre les débordements de boucle ou simplifie la DP)
H = LI() + [1]

# Initialisation de la liste dp, de taille n+1, dont chaque cellule est remplie avec la valeur 1.
# dp jouera le rôle de tableau de programmation dynamique pour stocker les résultats intermédiaires
dp = [1] * (n + 1)

# Boucle principale qui itère sur chaque indice k de 0 à n-1 inclus (n itérations)
for k in range(n):
    # Création d'un nouveau tableau new_dp de taille n+1 rempli de zéros,
    # qui recevra les nouveaux états de dp à l'étape k+1
    new_dp = [0] * (n + 1)
    # Boucle interne sur l'indice i allant de 0 à n inclus
    for i in range(n + 1):
        # Vérification de la première condition : si H[i] > H[k]
        if H[i] > H[k]:
            # La nouvelle valeur de new_dp[i] est alors dp[k] multiplié par 2
            new_dp[i] = dp[k] * 2
        # Sinon, vérification si H[k - 1] <= H[i] (attention: pour k=0, H[-1] correspond à H[n] car Python autorise les indices négatifs)
        elif H[k - 1] <= H[i]:
            # Ici, on multiplie dp[i] par 2 puis par une puissance de 2 :
            # l'exposant correspond à la différence H[k] - H[i] ; la multiplication se fait modulo mod
            new_dp[i] = dp[i] * 2 * pow(2, H[k] - H[i], mod)
        # Sinon, si H[k - 1] > H[k]
        elif H[k - 1] > H[k]:
            # On ajoute dp[i] et dp[k], résultat stocké dans new_dp[i]
            new_dp[i] = dp[i] + dp[k]
        # Sinon (toutes les autres situations)
        else:
            # On additionne dp[i] et dp[k - 1], puis multiplie par une puissance de 2 :
            # Exposant : différence H[k] - H[k-1] ; calcul modulo mod
            new_dp[i] = (dp[i] + dp[k - 1]) * pow(2, H[k] - H[k - 1], mod)
        # Résultat modulo mod pour rester dans l'intervalle des entiers supportés
        new_dp[i] %= mod
    # Mise à jour de dp par le nouvel état new_dp calculé à cette itération
    dp = new_dp

# Affichage du dernier élément de dp (dp[-1]), qui représente le résultat final recherché après toutes les itérations/prix
print(dp[-1])