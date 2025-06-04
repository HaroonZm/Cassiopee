import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import copy
import functools
import time
import random

# Augmentation du niveau de récursion maximal pour certains algorithmes récursifs lourds
sys.setrecursionlimit(10**7)

# Constantes utiles pour les calculs
inf = 10**20           # Représente un nombre très grand (l'infini)
eps = 1.0 / 10**10     # Petite valeur pour la comparaison de flottants
mod = 10**9+7          # Modulo courant pour certains problèmes
mod2 = 998244353       # Autre modulo fréquemment utilisé

# Déplacements voisins (haut, droite, bas, gauche)
dd = [(-1,0), (0,1), (1,0), (0,-1)]
# Déplacements voisins en 8 directions (haut, haut-droit, droite, bas-droit, bas, bas-gauche, gauche, haut-gauche)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def LI():
    """
    Lit une ligne d'entrée standard, la découpe en entiers, et les retourne sous forme de liste.
    Returns:
        list[int]: Liste d'entiers lus depuis stdin.
    """
    return list(map(int, sys.stdin.readline().split()))

def LLI():
    """
    Lit toutes les lignes restantes sur l'entrée standard et les retourne
    comme une liste de listes d'entiers.
    Returns:
        list[list[int]]: Liste de listes d'entiers.
    """
    return [list(map(int, l.split())) for l in sys.stdin.readlines()]

def LI_():
    """
    Lit une ligne d'entrée standard, la découpe en entiers,
    décrémente chaque entier de 1 (typiquement pour l'indexation 0-based), et retourne la liste.
    Returns:
        list[int]: Liste d'entiers (décalés de -1) depuis stdin.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne d'entrée standard, la découpe en flottants, et les retourne sous forme de liste.
    Returns:
        list[float]: Liste de flottants lus depuis stdin.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne d'entrée standard et la découpe en liste de chaînes de caractères (mots).
    Returns:
        list[str]: Liste de chaînes séparées par espace.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne d'entrée standard contenant un entier et le retourne.
    Returns:
        int: L'entier lu depuis stdin.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne d'entrée standard contenant un flottant et le retourne.
    Returns:
        float: Le flottant lu depuis stdin.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne d'entrée standard via input() (inclut éventuellement des espaces).
    Returns:
        str: La chaîne lue.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne sur la sortie standard et force le flush (pratique pour les problèmes interactifs).
    Args:
        s (str): Chaîne à afficher.
    """
    return print(s, flush=True)

def pe(s):
    """
    Affiche une chaîne sur la sortie d'erreur standard, pour la journalisation.
    Args:
        s (str): Chaîne à afficher sur stderr.
    """
    return print(str(s), file=sys.stderr)

def JA(a, sep):
    """
    Convertit une liste en une chaîne de caractères où chaque élément est séparé par `sep`.

    Args:
        a (list): Liste d'éléments à concaténer.
        sep (str): Séparateur entre les éléments.

    Returns:
        str: Chaîne résultante concaténée.
    """
    return sep.join(map(str, a))

def JAA(a, s, t):
    """
    Convertit une liste de listes en une chaîne de caractères, 
    utilisant « t » comme séparateur entre éléments internes, puis « s » entre les sous-listes.

    Args:
        a (list[list]): Liste de listes à concaténer.
        s (str): Séparateur entre sous-listes.
        t (str): Séparateur entre éléments d'une sous-liste.

    Returns:
        str: Chaîne finale formatée.
    """
    return s.join(t.join(map(str, b)) for b in a)

class RangeAddSum:
    """
    Implémente un Segment Tree pour gérer rapidement les opérations 'range add' (ajout sur segment)
    et 'range sum' (somme sur segment). Permet d'effectuer des ajouts sur des intervalles d'indices
    et de calculer la somme de sous-intervalles efficacement.
    """

    def __init__(self, n):
        """
        Initialise l'arbre de segment interne de capacité supérieure égale à la puissance de 2 la plus proche de n.

        Args:
            n (int): Taille effective du tableau/manché sur lequel effectuer les opérations.
        """
        i = 1
        while 2**i <= n:
            i += 1
        self.N = 2**i  # Taille tronquée à la prochaine puissance de 2
        self.A = [0] * (self.N*2)  # Tableau pour stocker les incréments d'intervalles entiers couverts
        self.B = [0] * (self.N*2)  # Tableau pour stocker les incréments partiels ou restants

    def add(self, a, b, x, k, l, r):
        """
        Ajoute la valeur x à tous les éléments de l'intervalle [a, b) (a inclus, b exclus).

        Args:
            a (int): Début de l'intervalle cible (inclus).
            b (int): Fin de l'intervalle (exclu).
            x (int/float): Valeur à ajouter.
            k (int): Index du nœud courant dans le segment tree (0 pour la racine).
            l (int): Limite gauche de la plage couverte par le nœud courant.
            r (int): Limite droite de la plage couverte par le nœud courant.
        """
        def ina(k, l, r):
            # Si [a, b) couvre entièrement [l, r), on stocke l'ajout dans le nœud en entier
            if a <= l and r <= b:
                self.A[k] += x
            # Si [a, b) intersecte [l, r), gestion récursive sur les enfants
            elif l < b and a < r:
                self.B[k] += (min(b, r) - max(a, l)) * x
                m = (l + r) // 2
                ina(k*2+1, l, m)
                ina(k*2+2, m, r)

        ina(k, l, r)

    def query(self, a, b, k, l, r):
        """
        Calcule la somme des éléments dans l'intervalle [a, b) du tableau cible.

        Args:
            a (int): Début de l'intervalle recherché (inclus).
            b (int): Fin de l'intervalle recherché (exclu).
            k (int): Index du nœud courant dans le segment tree (0 pour la racine).
            l (int): Limite gauche du nœud courant.
            r (int): Limite droite du nœud courant.

        Returns:
            int/float: Valeur de la somme dans [a, b).
        """
        def inq(k, l, r):
            # Aucun recouvrement
            if b <= l or r <= a:
                return 0

            # Si [a, b) couvre entièrement [l, r), retourne la somme stockée
            if a <= l and r <= b:
                return self.A[k] * (r - l) + self.B[k]

            # Recouvrement partiel : ajoute la somme des incréments, puis convertit récursivement
            res = (min(b, r) - max(a, l)) * self.A[k]
            m = (l + r) // 2
            res += inq(k*2+1, l, m)
            res += inq(k*2+2, m, r)
            return res

        return inq(k, l, r)

def main():
    """
    Fonction principale :
      - Lit les entiers n (taille), q (nombre de requêtes), et la liste des requêtes.
      - Gère deux types de requêtes :
        * (0, s, t, x): ajoute x à l'intervalle [s, t)
        * (1, s, t): calcule la somme sur l'intervalle [s, t)
      - Affiche les résultats des requêtes de type 1, un par ligne.

    Returns:
        str: Les résultats concaténés par retour à la ligne.
    """
    n, q = LI()                            # Lecture taille tableau et nombre de requêtes
    qa = [LI() for _ in range(q)]          # Lecture des q requêtes

    ras = RangeAddSum(n)                   # Initialisation du segment tree
    rr = []                                # Liste des résultats pour les requêtes de type somme

    for qi in qa:
        s = qi[1] - 1                      # Conversion en index 0-based
        t = qi[2]                          # Fin (non incluse)
        if qi[0] == 0:                     # Ajout sur segment
            x = qi[3]
            ras.add(s, t, x, 0, 0, n)
        else:                              # Somme sur segment
            rr.append(ras.query(s, t, 0, 0, n))

    return JA(rr, "\n")                    # Résultats formatés

# Si exécuté directement, lance la fonction principale et affiche ses résultats.
print(main())
# Pour afficher le temps d'exécution : décommenter les lignes liées à time.time(), pf et pe.