#!usr/bin/env python3  # Indique à l'OS d'utiliser l'interpréteur Python 3 pour exécuter ce script

# Importations de bibliothèques standards Python utilisées dans le code

from collections import defaultdict, deque  # defaultdict permet de créer des dictionnaires avec une valeur par défaut. deque est une file doublement terminée efficace.
from heapq import heappush, heappop  # Fonctions pour manipuler des tas binaires min-heap (file de priorité)
import sys  # Fournit l'accès à certains objets utilisés ou maintenus par l'interpréteur : ici pour lire l'entrée standard, changer la limite de récursion, etc.
import math  # Fournit des fonctions mathématiques standard (pas utilisé explicitement dans ce code)
import bisect  # Implémente des fonctions pour manipuler des listes triées (pas utilisé ici)
import random  # Fournit des fonctions pour générer des nombres aléatoires (pas utilisé ici)

# Définition de fonctions utilitaires pour faciliter la récupération et le traitement d'entrées standard

def LI():
    # Cette fonction lit une ligne depuis l'entrée standard, la divise en morceaux avec split()
    # et convertit chacun de ces éléments en int, puis retourne la liste de ces entiers.
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    # Cette fonction lit une ligne depuis l'entrée standard et la convertit directement en un entier.
    return int(sys.stdin.readline())

def LS():
    # Cette fonction lit une ligne de l'entrée standard, la découpe sur les espaces,
    # puis pour chacun de ces morceaux, crée une liste de caractères.
    # Elle retourne donc une liste de listes de caractères.
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    # Cette fonction lit une ligne depuis l'entrée standard et la convertit en une liste de caractères.
    # Si le dernier caractère (l'élément final de la liste) est un saut de ligne, il est retiré (slice jusqu'à l'avant-dernier).
    res = list(sys.stdin.readline())  # Convertit la ligne lue en liste de caractères
    if res[-1] == "\n":  # Vérifie si le dernier caractère est un saut de ligne
        return res[:-1]  # Retourne la liste sans le dernier caractère
    return res  # Sinon, retourne la liste entière lue

def IR(n):
    # Fonction qui lit n entiers depuis l'entrée standard (un entier par ligne)
    # et retourne ces n entiers sous forme de liste
    return [I() for i in range(n)]

def LIR(n):
    # Fonction qui lit n lignes, chaque ligne étant traitée par LI(), c'est-à-dire convertie en liste d'entiers.
    # Retourne donc une liste de n listes d'entiers.
    return [LI() for i in range(n)]

def SR(n):
    # Fonction qui lit n lignes depuis l'entrée standard, chacune traitée avec S(), renvoie une liste de listes de caractères
    return [S() for i in range(n)]

def LSR(n):
    # Fonction qui lit n lignes, chaque ligne est traitée avec LS(), retournant donc une liste de listes de listes de caractères
    return [LS() for i in range(n)]

# On augmente la limite de récursion maximale de Python pour autoriser jusqu'à 1 000 000 appels récursifs imbriqués.
# Utile pour des algorithmes utilisant la récursion profonde, mais pas utilisé explicitement dans ce script.

sys.setrecursionlimit(1000000)

# Déclaration d'une variable entière "mod" valant 10^9+7, un nombre premier
# Utilisé traditionnellement pour réduire des résultats mathématiques trop grands par un modulo, mais il n'est pas utilisé dans ce code.
mod = 1000000007

# Définition de la fonction principale "solve", qui est appelée pour résoudre le problème.

def solve():
    n = I()  # Lit un entier représentant le nombre d'opérations que le programme doit gérer
    a, b = 0, 1  # Initialise deux variables entières a à 0 et b à 1.
                 # Ces variables vont servir de base pour les manipulations demandées dans la boucle suivante.

    for i in range(n):  # Boucle for qui itère n fois, i servant d'index de boucle (mais non utilisé explicitement)
        q, x = LI()  # Pour chaque itération : lit deux entiers de la même ligne.
                     # q : indique le type d'opération à effectuer
                     # x : la valeur utilisée pour cette opération

        if q == 1:
            # Si q vaut 1 : on multiplie "a" par "x" et on multiplie "b" par "x"
            a *= x
            b *= x
        elif q == 2:
            # Si q vaut 2 : on ajoute "x" à "a" ainsi qu'à "b"
            a += x
            b += x
        else:
            # Pour tout autre cas (donc q == 3, selon la logique du code),
            # on soustrait "x" à "a" et à "b"
            a -= x
            b -= x

    B = b - a  # À la fin de la boucle, on calcule la différence B entre "b" et "a"

    # On affiche deux nombres séparés par un espace :
    # Le premier nombre est "B-b", soit la différence entre "B" et "b"
    # Le deuxième nombre est "B" (la différence entre "b" et "a")
    # print affiche ces valeurs sur une ligne
    print(B - b, B)

    return  # Fait sortir de la fonction solve. (Ici, return explicite mais non obligatoire)

# Ce bloc spécial permet d'exécuter la fonction solve uniquement si ce fichier
# est exécuté en tant que script principal (et non importé comme module par un autre fichier)
if __name__ == "__main__":
    solve()  # Appel de la fonction principale du programme