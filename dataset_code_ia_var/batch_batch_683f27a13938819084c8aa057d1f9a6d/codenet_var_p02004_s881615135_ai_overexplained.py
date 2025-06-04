#!usr/bin/env python3

# La ligne ci-dessus informe au système d'exploitation d'utiliser l'interpréteur Python 3 pour exécuter ce script.

# Importation de modules de la bibliothèque standard

# Importe defaultdict depuis le module collections. defaultdict est un dictionnaire qui fournit une valeur par défaut pour les clés non existantes.
from collections import defaultdict

# Importe deque depuis le module collections. La classe deque (double-ended queue) permet d'ajouter et de supprimer des éléments efficacement des deux côtés de la deque.
from collections import deque

# Importe les fonctions heappush et heappop depuis le module heapq. Ces fonctions sont utilisées pour la manipulation de tas binaires (min-heaps), qui servent à accéder facilement à l'élément minimum.
from heapq import heappush, heappop

# Importe le module sys, qui donne accès à des variables et fonctions qui interagissent fortement avec l'interpréteur Python.
import sys

# Importe le module math, qui comporte de nombreuses fonctions mathématiques usuelles comme sqrt, sin, cos, etc.
import math

# Importe le module bisect, qui contient des fonctions de recherche et d'insertion dans des listes triées.
import bisect

# Importe le module random, qui permet de générer des nombres aléatoires et de faire du tirage au hasard.
import random

# Importe le module itertools, qui fournit des fonctions permettant de créer et d'utiliser des itérateurs efficaces.
import itertools

# Modifie la limite maximale de récursion pour éviter d'atteindre cette limite dans les cas où l'on utilise beaucoup de récursivité (par défaut, la limite est 1000).
sys.setrecursionlimit(10**5)

# Assigne la variable stdin au flux d'entrée standard, c'est-à-dire là où le script lit ses entrées (utilisé avec input ou readline).
stdin = sys.stdin

# Attribue des alias locaux aux fonctions bisect_left et bisect_right pour faciliter leur utilisation. bisect_left donne l'indice d'insertion à gauche dans une liste triée, bisect_right le fait à droite.
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right

# Définitions de fonctions utilitaires pour différentes entrées courantes

# Fonction qui lit une ligne depuis l'entrée standard, divise la ligne en morceaux séparés par des espaces, convertit chaque morceau en int et retourne la liste résultante.
def LI(): 
    return list(map(int, stdin.readline().split()))

# Fonction similaire à LI, mais convertit les valeurs en float au lieu de int.
def LF(): 
    return list(map(float, stdin.readline().split()))

# Fonction qui lit une ligne, découpe en mots, convertit chaque mot en entier, puis soustrait 1 à chacun (utile pour convertir des indices 1-based en 0-based), retourne la liste résultante.
def LI_(): 
    return list(map(lambda x: int(x)-1, stdin.readline().split()))

# Fonction qui lit une ligne depuis stdin et la convertit en int.
def II(): 
    return int(stdin.readline())

# Fonction qui lit une ligne et la convertit en float.
def IF(): 
    return float(stdin.readline())

# Fonction qui lit une ligne depuis stdin, la divise en mots, et transforme chaque mot en liste de caractères (retourne donc une liste de listes de caractères).
def LS(): 
    return list(map(list, stdin.readline().split()))

# Fonction qui lit une ligne depuis stdin, enlève le saut de ligne en fin de ligne, puis retourne la ligne sous forme de liste de caractères.
def S(): 
    return list(stdin.readline().rstrip())

# Fonction qui exécute II() n fois et retourne la liste des n entiers lus.
def IR(n): 
    return [II() for _ in range(n)]

# Fonction qui exécute LI() n fois et retourne la liste des n listes d'entiers lues.
def LIR(n): 
    return [LI() for _ in range(n)]

# Fonction qui exécute IF() n fois et retourne la liste des n flottants lus.
def FR(n): 
    return [IF() for _ in range(n)]

# Fonction qui exécute LI() n fois et retourne la liste des n listes d'entiers lues. Redondant avec LIR.
def LFR(n): 
    return [LI() for _ in range(n)]

# Fonction qui exécute LI_() n fois et retourne la liste des n listes d'entiers moins un.
def LIR_(n): 
    return [LI_() for _ in range(n)]

# Fonction qui exécute S() n fois et retourne la liste des n listes de caractères.
def SR(n): 
    return [S() for _ in range(n)]

# Fonction qui exécute LS() n fois, retournant n listes de listes de caractères.
def LSR(n): 
    return [LS() for _ in range(n)]

# Déclaration d'une variable mod contenant un nombre premier utilisé souvent pour faire des opérations modulo (surtout dans les problèmes d'arithmétique modulaire ou de dénombrement).
mod = 1000000007

# Déclaration d'une variable inf assignée à la chaîne de caractères 'INF' convertie en float (ce qui donne l'infini positif en Python).
inf = float('INF')

# ---------------------------------------------------------------------------
# Définition de la fonction A, qui réalise un traitement sur une chaîne de caractères.

def A():
    # Appelle la fonction S() pour lire une chaîne de caractères depuis l'entrée standard, sous forme de liste de caractères.
    s = S()
    # Initialise un compteur i à 0, qui servira d'indice pour parcourir la liste s.
    i = 0
    # Initialise la variable now à 0. Elle semble contenir un état courant qui sera incrémenté ou décrémenté selon le caractère lu.
    now = 0
    # Initialise la variable ans à 0, qui comptera le nombre de fois où une certaine condition est satisfaite.
    ans = 0

    # Début de la boucle principale, qui parcourt chaque caractère de la liste s à l'aide de i.
    while i < len(s):
        # Si le caractère courant est un 'R'
        if s[i] == "R":
            # Si now vaut 0 (état initial ou revenu à l'état initial)
            if now == 0:
                # Incrémente de 1 la variable now.
                now += 1
                # Passe au caractère suivant en incrémentant i.
                i += 1
                # Débute une boucle intérieure pour continuer à parcourir s depuis la nouvelle position de i.
                while i < len(s):
                    # Si le caractère est encore un 'R'
                    if s[i] == "R":
                        # Incrémente now de 1.
                        now += 1
                    else:
                        # Sinon, décrémente now de 1.
                        now -= 1
                    # Modulo 4 sur now pour qu'il soit toujours dans l'intervalle [0,3] (cycle sur 4 états).
                    now = now % 4
                    # Passe au caractère suivant.
                    i += 1
                    # Si now revient à 0 (état de départ), c'est une séquence complète.
                    if now == 0:
                        # Si le dernier caractère traité est 'R'
                        if s[i-1] == "R":
                            # Incrémente ans de 1, car une séquence appropriée a été trouvée.
                            ans += 1
                        # Quitte la boucle intérieure, car le cycle est complet.
                        break
            else:
                # Si now n'est pas 0, on incrémente now de 1 pour tenir compte du nouveau 'R'.
                now += 1
                # On garde now dans l'intervalle [0,3] (avec modulo).
                now = now % 4
                # Passe au caractère suivant.
                i += 1
        else:
            # Si le caractère lu n'est pas 'R' (ici tout autre caractère), on décrémente now.
            now -= 1
            # Modulo pour rester dans l'intervalle [0,3].
            now = now % 4
            # Passe au caractère suivant.
            i += 1

    # Affiche la valeur finale de ans à la sortie standard (normalement l'utilisateur attend une réponse).
    print(ans)

    # La fonction ne retourne rien de spécial, juste une instruction return vide.
    return

# ---------------------------------------------------------------------------
# Fonctions B à H sont présentes comme gabarits pour d'autres parties du code, mais elles sont vides et ne font rien pour l'instant.

def B():
    return

def C():
    return

def D():
    return

def E():
    return

def F():
    return

def G():
    return

def H():
    return

# ---------------------------------------------------------------------------
# Bloc principal, exécute le script si ce fichier est exécuté directement (et non importé comme module).
if __name__ == '__main__':
    A()  # Appelle la fonction A définie précédemment.