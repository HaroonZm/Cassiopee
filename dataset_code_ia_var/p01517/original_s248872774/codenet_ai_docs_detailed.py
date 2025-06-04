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
import random
import time
import copy
import functools

# Augmente la limite de récursion pour permettre des appels récursifs profonds si nécessaire
sys.setrecursionlimit(10**7)

# Définit une grande valeur représentant l'infini dans le contexte de l'algorithme
inf = 10**20

# Petite valeur epsilon, utilisée lors des comparaisons de nombres à virgule flottante
eps = 1.0 / 10**13

# Constante utilisée pour effectuer des opérations modulo sur de grands entiers
mod = 10**9+7

# Déplacements dans les 4 directions cardinales (haut, droite, bas, gauche)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Déplacements dans les 8 directions (incluant diagonales)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def LI():
    """
    Lit une ligne de l'entrée standard et la convertit en liste d'entiers.

    Returns:
        list: Liste d'entiers lus depuis l'entrée.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne d'entrée standard et la convertit en liste d'entiers, chacun décrémenté de un.

    Returns:
        list: Liste d'entiers (décalés de -1) lus depuis l'entrée.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et la convertit en liste de flottants.

    Returns:
        list: Liste de nombres à virgule flottante lus depuis l'entrée.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et la convertit en liste de chaînes de caractères séparées par espace.

    Returns:
        list: Liste de chaînes (str) lues depuis l'entrée.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier de l'entrée standard.

    Returns:
        int: Entier lu depuis l'entrée.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un nombre flottant de l'entrée standard.

    Returns:
        float: Nombre à virgule flottante lu depuis l'entrée.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de texte depuis l'entrée standard (retire le caractère de fin de ligne).

    Returns:
        str: Ligne lue depuis l'entrée.
    """
    return input()

def pf(s):
    """
    Affiche le texte s, puis vide explicitement le buffer de sortie.

    Args:
        s (str): Texte à afficher.
    """
    print(s, flush=True)

def main():
    """
    Fonction principale. Traite des cas d'entrée selon une logique spécifique (problème d'optimisation avec contraintes sur des ensembles et dépendances).
    
    Lit plusieurs cas (tant que n != 0), traite chaque cas via la fonction interne f(n), puis affiche tous les résultats.

    Returns:
        str: Chaîne résultante des résultats de chaque cas, séparés par des retours à la ligne.
    """
    rr = []  # Liste de résultats pour chaque cas

    def f(n):
        """
        Traite un seul cas selon la logique problématique :
        Chaque entrée représente une "action" ou "tâche" avec potentiellement des dépendances, et l'on cherche à maximiser un score sous certaines contraintes.

        Args:
            n (int): Nombre de lignes/éléments pour ce cas.

        Returns:
            int: Résultat calculé.
        """
        a = [LS() for _ in range(n)]  # Lis toutes les lignes du cas, chacune étant une liste de champs (str)
        sn = {}  # Associe un nom à un indice pour chaque élément

        # Indexation : associe chaque nom à son indice d'apparition
        for i in range(n):
            sn[a[i][0]] = i

        b = []   # Stocke des actions filtrées avec leur bitmask, valeur et dépendances encodées en bitmask
        bs = {}  # Pour chaque bitmask-id, stocke les dépendances encodées
        bb = {}  # Pour chaque bitmask-id, stocke la valeur associée
        kr = int(a[0][1])  # Initialisation de la "réponse" avec la première donnée numérique du premier élément

        # Parcours des lignes à partir de la deuxième (index 1)
        for i in range(1, n):
            ai = a[i]
            # Ignore si le premier nom (racine) est une dépendance de cette "tâche"
            if a[0][0] in ai[3:]:
                continue
            # Si la colonne 2 est '0', ajoute sa valeur à kr, et saute la suite
            if ai[2] == '0':
                kr += int(ai[1])
                continue

            # Sinon, encode la tâche comme : [bitmask_id, valeur, dependances_bitmask]
            b.append([2**sn[ai[0]], int(ai[1]), sum(map(lambda x: 2**sn[x], ai[3:]))])
            bs[b[-1][0]] = b[-1][-1]
            bb[b[-1][0]] = b[-1][1]

        fm = {}  # Mémoïsation de _f : bitmask d'état -> résultat maximal
        def _f(i):
            """
            Fonction récursive avec mémoïsation, calcule la meilleure somme de valeurs sur un ensemble de tâches (bitmask i)
            en tenant compte des dépendances (encodées dans bs) et des valeurs (bb).

            Args:
                i (int): Bitmask représentant l'ensemble courant de tâches disponibles.

            Returns:
                int: Score maximal atteignable avec cet ensemble de tâches.
            """
            if i == 0:
                return 0
            if i in fm:
                return fm[i]

            r = 0     # Score maximal courant
            si = 0    # Indique la progression sur les bits à traiter
            kr = 0    # Stocke la somme des valeurs réalisables sans dépendances
            nsi = 0   # Ensemble de tâches traitées simplement

            # Première boucle : ajoute directement les tâches réalisables sans dépendances actives
            while i > si:
                ti = i - si
                # Ni isole le bit de poids le plus faible encore à traiter
                ni = ti - (ti & (ti-1))
                si += ni
                # Si la dépendance n'est PAS satisfaite (ie, bs[ni] n'est pas inclus dans i)
                if (bs[ni] & i) == 0:
                    nsi += ni
                    kr += bb[ni]

            si = nsi
            # Deuxième boucle : pour le reste des tâches, tente de les sélectionner récursivement
            while i > si:
                ti = i - si
                ni = ti - (ti & (ti-1))
                nr = bb[ni]
                si += ni
                nr += _f(i - nsi - ni - (i & bs[ni]))
                if r < nr:
                    r = nr

            fm[i] = r + kr
            return r + kr

        r = 0  # Résultat maximal global
        l = len(b)
        l2 = l // 2  # Pour équilibrer le nombre de combinaisons à tester (meet-in-the-middle classique)
        ii = [b[i][0] for i in range(l2)]  # Prend l'identifiant de bitmask pour la moitié des tâches
        ab = sum(x[0] for x in b)
        anb = sum(x[0] for x in b[l2:])  # Bitmask des tâches dans la seconde moitié

        # Boucle : évalue toutes les combinaisons de la première moitié ; pour chaque, combine avec le résultat optimal de la deuxième moitié
        for i in range(l2+1):
            for ia in itertools.combinations(ii, i):
                ti = sum(ia)
                tf = False     # Indicateur de conflit de dépendance
                tr = 0         # Score partiel pour cette combinaison
                ts = 0         # Bitmask des dépendances générées par cette combinaison

                # Vérifie que toutes les tâches de la combinaison sont compatibles entre elles (pas de conflit de dépendance)
                for j in ia:
                    if bs[j] & ti:
                        tf = True
                        break
                    tr += bb[j]
                    ts |= bs[j]
                if tf:
                    continue

                # Combine avec le résultat optimal de la deuxième moitié (récursif)
                tr += _f(anb - (anb & ts))
                if r < tr:
                    r = tr

        return r + kr  # Combine le score optimal agrégé avec la valeur accumulée "kr"

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(map(str, rr))

# Exécute la fonction main et affiche le résultat
print(main())