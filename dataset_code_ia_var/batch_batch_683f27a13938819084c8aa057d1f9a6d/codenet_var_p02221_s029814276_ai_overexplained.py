#!usr/bin/env python3

# Importation des modules nécessaires
from collections import defaultdict, deque           # Collection d'objets utiles : defaultdict pour des dictionnaires avec des valeurs par défaut, deque pour des files double-entrée.
from heapq import heappush, heappop                  # heappush/heappop servent à manipuler des files de priorité (tas).
from itertools import permutations, accumulate       # permutations pour générer toutes les permutations, accumulate pour les sommes cumulées.
import sys                                           # Module donnant accès à des variables et fonctions propres à l'environnement Python, comme les entrées/sorties standard.
import math                                          # Module mathématique pour de nombreuses fonctions mathématiques communes.
import bisect                                        # Module pour manipuler des listes triées (insertion, recherche).

# Définition de fonctions utilitaires permettant de lire les entrées plus facilement depuis stdin (entrée standard).

def LI():
    """
    Lit une ligne depuis l'entrée standard, la découpe sur les espaces,
    convertit chaque élément découpé en entier, et retourne la liste de ces entiers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    """
    Lit une ligne depuis l'entrée standard, retire le caractère de fin de ligne,
    convertit la chaîne en un entier et renvoie cet entier.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne depuis l'entrée, découpe la ligne sur les espaces,
    transforme chaque "mot" de la ligne en une liste de caractères, puis retourne
    une liste contenant chacune de ces listes.
    """
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    """
    Lit une ligne depuis l'entrée standard, la convertit en une liste de caractères,
    puis vérifie si le dernier caractère de la liste est un saut de ligne ("\n").
    Si oui, retire ce caractère et retourne la liste ainsi modifiée.
    Sinon, retourne la liste telle quelle.
    """
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    """
    Lit n entiers (chacun sur une ligne séparée) depuis l'entrée standard et retourne
    la liste de ces entiers.
    """
    return [I() for i in range(n)]

def LIR(n):
    """
    Lit n lignes de l'entrée standard, chacune contenant une séquence d'entiers séparés par
    des espaces, et retourne une liste composée de ces listes.
    """
    return [LI() for i in range(n)]

def SR(n):
    """
    Lit n lignes de l'entrée standard, chacune convertie en une liste de caractères (en faisant appel à S),
    retourne une liste de ces listes.
    """
    return [S() for i in range(n)]

def LSR(n):
    """
    Pour n lignes de l'entrée standard, découpe chaque ligne sur les espaces, convertit chaque
    'mot' en liste de caractères, retourne la liste de ces listes pour chaque ligne.
    """
    return [LS() for i in range(n)]

# On augmente la limite de récursion pour éviter les erreurs de récursion lors
# d'appels récursifs profonds (par exemple dans certains algorithmes sur des arbres).
sys.setrecursionlimit(1000000)

# On définit un modulo souvent utilisé dans les problèmes compétitifs.
mod = 1000000007

def solve():
    """
    Fonction principale résolvant le problème selon l'entrée.
    Elle inclut une sous-fonction f(a, b) qui choisit entre a et b selon les instructions contenues
    dans la liste de caractères 's', puis construit une table dp en utilisant cette règle.
    À la fin, le résultat final est affiché pour chaque configuration.
    """
    def f(a, b):
        """
        Fonction prenant deux valeurs a et b.
        - Calcule la valeur absolue de leur différence (abs(a-b)).
        - Va chercher dans la liste de caractères 's' à l'indice (abs(a-b)-1).
        - Si la valeur à cet indice est le caractère "1", alors retourne la valeur maximale entre a et b ;
        - Sinon, retourne la valeur minimale entre a et b.
        Cela sert à appliquer une règle de sélection conditionnelle selon l'entrée 's'.
        """
        return max(a, b) if s[abs(a-b)-1] == "1" else min(a, b)
    
    n = I()                       # On lit un entier depuis l'entrée (taille du tournoi ou nombre de participants, par exemple).
    s = S()                       # Lecture de la séquence de caractères qui détermine les règles de sélection pour chaque différence.
    p = LI()                      # Lit une liste d'entiers correspondant à des valeurs associées à chaque participant (score, force, etc.).

    # Construction de la table dp.
    # dp est une liste de listes.
    # Pour chaque valeur i de 0 (inclus) à (2^n) (exclus), on crée une sous-liste de n+1 éléments:
    # La première colonne (j=0) reçoit p[i] (la valeur du participant i) ; les autres colonnes sont initialisées à zéro.
    dp = [[0 if j else p[i] for j in range(n+1)] for i in range(1 << n)]  # 1 << n équivaut à 2 puissance n.
    maxn = 1 << n                    # Calcul de 2 puissance n et stockage dans maxn, pour éviter de recalculer.

    # Boucle principale de programmation dynamique.
    # On procède sur toutes les "phases" j de 0 à n-1 (par ex: tours du tournoi).
    for j in range(n):
        j1 = 1 << j                   # j1 vaudra 1, 2, 4, 8, ..., selon la valeur de j. Cela sert de décalage binaire pour grouper les états.
        for i in range(1 << n):       # Pour chaque état ou partition possible (tous les sous-ensembles de taille n).
            if i + j1 >= maxn:
                # On est "hors-limites" du tableau initial, et on utilise alors dp[i+j1-maxn][j], c'est-à-dire on revient circulairement.
                dp[i][j+1] = f(dp[i][j], dp[i+j1-maxn][j])
            else:
                # Sinon, on utilise dp[i+j1][j], c'est-à-dire l'élément aux j1 positions suivantes dans l'état.
                dp[i][j+1] = f(dp[i][j], dp[i+j1][j])

    # À ce stade, dp[i][n] représente la valeur finale pour chaque état i après toutes les itérations/transitions (par exemple, gagnant de chaque configuration).
    for i in range(1 << n):
        print(dp[i][-1])              # Affiche la dernière entrée de chaque sous-liste, c'est-à-dire à la dernière étape.
        # On boucle sur tous les états possibles, donc on affiche le résultat final pour chacun.
    return                             # Facultatif, termine la fonction solve().

# Point d'entrée principal. Si le script est exécuté directement (et non importé), on lance la fonction solve().
if __name__ == "__main__":
    solve()