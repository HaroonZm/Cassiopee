import math  # Ce module fournit des fonctions mathématiques de base, comme sqrt, sin, pi, etc.
import string  # Permet de manipuler des chaînes de caractères, notamment les constantes comme ascii_letters.
import itertools  # Fournit des outils pour créer des itérateurs complexes (combinations, permutations...)
import fractions  # Permet de manipuler des fractions rationnelles.
import heapq  # Fournit une implémentation efficace de la structure de données heap (file de priorité).
import collections  # Contient des types de données spécialisés comme deque, Counter, defaultdict, etc.
import re  # Sert à travailler avec les expressions régulières.
import array  # Fournit un type tableau efficace pour stocker des données numériques.
import bisect  # Aide à manipuler des listes triées, ajoute ou cherche efficacement.
import sys  # Fournit des variables et fonctions propres à l'interpréteur (comme stdin, exit...).
import copy  # Permet de copier des objets (profondément ou non).
import functools  # Fournit des outils pour programmer avec des fonctions de haut niveau.
import time  # Permet de manipuler le temps et les délais.
import random  # Génère des nombres pseudo-aléatoires.

# Modifie la limite maximale de récursion autorisée par Python
sys.setrecursionlimit(10**7)  # Cela permet d'éviter que le programme ne plante lorsqu'il effectue une grande récursion

inf = 10**20  # Une valeur représentant un "infini" pour les comparaisons ou bornes supérieures.
eps = 1.0 / 10**10  # Une petite valeur, utile pour comparer des nombres à virgule flottante.
mod = 10**9+7  # Un modulo couramment utilisé dans de nombreux problèmes de programmation compétitive.
mod2 = 998244353  # Un autre modulo très utilisé en algorithmie compétitive.

# Définition d'une liste de couples représentant les 4 directions cardinales (-1 pour haut, puis droite, bas, gauche).
dd = [(-1,0),(0,1),(1,0),(0,-1)]
# Définition d'une liste de couples représentant les 8 directions d'une matrice (toutes les directions autour d'un point).
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Fonction qui lit une ligne depuis l'entrée standard, coupe la chaîne en morceaux par espace,
# transforme chaque morceau en un entier, et construit une liste.
def LI():
    return list(map(int, sys.stdin.readline().split()))

# Fonction qui lit chaque ligne restante de l'entrée standard, coupe les morceaux par espace,
# transforme chaque morceau en un entier, retourne une liste de listes.
def LLI():
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

# Semblable à LI, mais retourne des entiers décrémentés (pour compter à partir de zéro).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne depuis l'entrée standard, la coupe en morceaux, 
# et transforme chaque morceau en flottant.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne depuis l'entrée standard et la coupe en morceaux (sur les espaces).
def LS():
    return sys.stdin.readline().split()

# Avant d'utiliser "I", on lit une ligne, puis on la convertit en entier.
def I():
    return int(sys.stdin.readline())

# Pareil, mais pour un nombre flottant
def F():
    return float(sys.stdin.readline())

# Retourne simplement l'entrée de l'utilisateur (ligne lue), sous forme de chaîne.
def S():
    return input()

# Affiche la valeur "s" en forçant le flush du buffer d'affichage. Utile pour interagir avec des juges automatiques.
def pf(s):
    return print(s, flush=True)

# Affiche la valeur "s" mais dans le flux d’erreur standard (stderr).
def pe(s):
    return print(str(s), file=sys.stderr)

# Prend une séquence "a" et une chaîne "sep" (séparateur). Convertit chaque élément de "a" en chaîne,
# puis les concatène avec le séparateur.
def JA(a, sep):
    return sep.join(map(str, a))

# Pour une liste de listes "a", entrelace les valeurs de chaque sous-liste avec "t", puis chaque bloc avec "s".
def JAA(a, s, t):
    return s.join(t.join(map(str, b)) for b in a)

# Fonction principale du programme
def main():
    # Lecture de deux entiers à partir de l'entrée standard :
    n, m = LI()  # n est typiquement la taille d'un intervalle général, m le nombre d'intervalles à considérer

    # Lecture des m intervalles, chaque intervalle étant un triplet [l, r, c].
    # On les trie par trois critères : 'l' croissant, puis 'c' croissant, puis 'r' décroissant.
    lrc = sorted([LI() for _ in range(m)], key=lambda x: (x[0], x[2], -x[1]))

    # On ajoute à la fin un intervalle factice contenant des valeurs de "l", "r", "c" très grandes (pour bloquer les boucles plus loin).
    lrc.append([inf, inf, inf])

    # Initialisation d'un indice pour parcourir la liste lrc
    i = 0

    # On crée une liste q de tuples : chaque tuple a la forme (position, coût minimal pour atteindre cette position)
    # On part avec (1,0), indiquant qu'on est à la position 1 avec un coût 0. (inf, inf) est un "garde-fou".
    q = [(1,0), (inf, inf)]

    # Parcours chaque position "l" de 1 (compris) à n-1 (exclu)
    for l in range(1, n):
        # Tant que lrc[i][0] < l, on saute les intervalles qui commencent avant "l"
        while lrc[i][0] < l:
            i += 1
        # Pour chaque intervalle qui commence exactement à "l"
        while lrc[i][0] == l:
            # On extrait "r" et "c" de cet intervalle
            _, r, c = lrc[i]
            i += 1  # On passe à l'intervalle suivant pour la prochaine itération

            # On cherche l'indice dans q où se trouve un intervalle couvrant "l" 
            # bisect.bisect_left cherche le premier élément >= (l, -1) (le -1 n'est là que pour l'ordre lexicographique)
            qi = bisect.bisect_left(q, (l, -1))
            _, cc = q[qi]  # cc : le coût minimal pour atteindre l

            # On prépare une nouvelle transition vers la position "r" avec le nouveau coût
            t = (r, cc + c)

            # On recherche où insérer ce nouveau tuple (r, nouveau coût total obtenu) dans q
            ti = bisect.bisect_left(q, t)

            # Si à l'endroit où on veut insérer, le coût existant est plus élevé, 
            # et si la plage précédente couvre le point de départ de notre nouvel intervalle
            if q[ti][1] > t[1] and q[ti-1][0] < r:
                # Si l'intervalle arriverait exactement en r, on le met à jour
                if q[ti][0] == r:
                    q[ti] = t
                else:
                    # Sinon, on insère le nouvel intervalle à la bonne place
                    q.insert(ti, t)
                # On retire tous les intervalles dont le coût qui précède celui-ci est pire,
                # pour conserver la structure de la liste q ordonnée avec les meilleurs coûts uniquement
                while q[ti-1][1] > t[1]:
                    del q[ti-1]
                    ti -= 1  # On recule pour continuer la vérification si besoin

    # À la fin, on cherche parmi les entrées de q la dernière position atteinte
    t = q[-2]  # On regarde l'avant dernier car le dernier est (inf, inf)
    # Si la position atteinte est strictement avant n, c'est qu'on ne peut pas construire une solution complète
    if t[0] < n:
        return -1  # Cas d'impossibilité

    # Sinon, on retourne le coût minimal pour atteindre la fin
    return t[1]

# On exécute la fonction principale et on affiche le résultat
print(main())