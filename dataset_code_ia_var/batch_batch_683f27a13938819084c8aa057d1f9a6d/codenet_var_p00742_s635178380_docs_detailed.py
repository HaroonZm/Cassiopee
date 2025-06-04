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

# Augmenter la limite de récursion, utile pour certains scénarios de backtracking profonds
sys.setrecursionlimit(10 ** 7)

# Constantes globales utilisées dans des calculs ou comme bornes
inf = 10 ** 20           # Valeur infinie (utile pour des comparaisons de grand nombre)
eps = 1.0 / (10 ** 10)   # Précision pour comparaisons flottantes
mod = 10 ** 9 + 7        # Modulo classique pour les opérations sur les entiers

# Directions usuelles pour parcourir une grille (haut, droite, bas, gauche)
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Directions diagonales et cardinales (pour parcourir les 8 voisins)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Fonctions d'aide pour lire différents types d'entrée rapidement
def LI():
    """Lit une ligne de l'entrée standard et la convertit en une liste d'entiers."""
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """Lit une ligne d'entiers et décrémente chaque valeur de 1 (pour indexation 0-based)."""
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """Lit une ligne de flottants et la convertit en liste de float."""
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """Lit une ligne de chaînes et la convertit en une liste de chaînes."""
    return sys.stdin.readline().split()

def I():
    """Lit et retourne un entier depuis l'entrée standard."""
    return int(sys.stdin.readline())

def F():
    """Lit et retourne un flottant depuis l'entrée standard."""
    return float(sys.stdin.readline())

def S():
    """Lit et retourne une chaîne (stripping newline) depuis l'entrée standard."""
    return input()

def pf(s):
    """Écrit la chaîne s sur la sortie standard avec flush."""
    return print(s, flush=True)

def main():
    """
    Fonction principale du programme. Lit l'entrée, traite les cas, et imprime les résultats.
    
    Pour chaque cas, lit un ensemble de chaînes représentant des nombres en lettres, et
    compte le nombre d'affectations de chiffres possibles (1-9, pas de zéro initial sauf 
    autorisé) aux lettres de façon à ce que la somme des (n-1) premiers égale la dernière.
    
    Retourne :
        Une chaîne contenant les résultats pour tous les cas testés, séparés par des retours ligne.
    """
    rr = []  # Liste des résultats pour chaque cas

    def f(n):
        """
        Compte le nombre d'affectations valides de chiffres aux lettres pour un système 
        d'équations basé sur l'entrée des mots.
        
        Args:
            n (int): Le nombre de mots (chaînes) dans le cas courant.
        
        Returns:
            int: Le nombre de solutions valides possibles pour l'affectation de chiffres aux lettres.
        """
        # Lire tous les mots en entrée
        ss = [S() for _ in range(n)]
        
        cs = set()  # Ensemble de tous les caractères présents
        nz = set()  # Lettres qui ne doivent pas être assignées à 0 (en tête d'un mot avec longueur > 1)
        
        # Identifier l'ensemble total des lettres et celles qui ne peuvent être 0
        for s in ss:
            cs |= set([c for c in s])
            if len(s) > 1:
                nz.add(s[0])
        
        l = len(cs)  # Nombre de lettres différentes
        ci = {}      # Dictionnaire lettre -> indice
        cw = [0] * l # Poids de chaque lettre (selon sa position dans chaque mot)
        
        # Attribuer à chaque lettre un index. Lettres non nulles en premier pour éviter de leur assigner 0
        for c, i in zip(sorted(list(cs), key=lambda x: 0 if x in nz else 1), range(l)):
            if c in nz:
                nz.add(i)  # On note aussi l'indice correspondant dans 'nz'
            ci[c] = i     # Mappe la lettre à son indice

        # Calculer les coefficients de chaque lettre pour la somme du problème
        for s in ss[:-1]:
            w = 1
            for c in s[::-1]:  # De droite à gauche, poids 1, 10, 100, etc.
                cw[ci[c]] += w
                w *= 10
        w = 1
        for c in ss[-1][::-1]:
            cw[ci[c]] -= w
            w *= 10

        r = 0  # Résultat pour ce cas

        # Séparation en deux groupes pour l'optimisation via meet-in-the-middle
        al = l // 2
        bl = l - al
        cwa = cw[:al]
        cwb = cw[al:]

        # Générer toutes les combinaisons possibles pour les affectations de chiffres
        for _a in itertools.combinations(range(1, 10), al):
            ad = collections.defaultdict(int)
            bd = collections.defaultdict(int)

            # Tester toutes les permutations des chiffres choisis pour la 1re moitié
            for a in itertools.permutations(_a, al):
                tw = 0
                for i in range(al):
                    tw += cwa[i] * a[i]
                ad[tw] += 1

            # Chiffres restants pour la 2de moitié
            _b = [_ for _ in range(1, 10) if _ not in _a]

            # Tester toutes les permutations pour la 2de moitié
            for b in itertools.permutations(_b, bl):
                tw = 0
                for i in range(bl):
                    tw += cwb[i] * b[i]
                bd[tw] += 1

            # Fusion des résultats pour trouver les solutions qui s'annulent
            aa = sorted(ad.items())
            ba = sorted(bd.items(), reverse=True)
            aal = len(aa)
            bal = len(ba)
            ai = bi = 0
            while ai < aal and bi < bal:
                t = aa[ai][0] + ba[bi][0]
                if t == 0:
                    r += aa[ai][1] * ba[bi][1]
                    ai += 1
                    bi += 1
                elif t < 0:
                    ai += 1
                else:
                    bi += 1

        # Calcul des indices des lettres autorisées à être 0, en inversant pour permutations
        zl = [_ for _ in range(l) if _ not in nz][::-1]
        al = l - len(zl)
        bl = l - al

        # Cas particuliers quand il y a peu de lettres qui peuvent être à 0 ou si une seule partie possible
        if al == 0 or bl < 2:
            # On construit la liste des différences de coefficients pour les lettres candidates à 0
            cws = [cw[i + 1] - cw[i] for i in range(l - 1)]
            for a in itertools.permutations(range(1, 10), l - 1):  # permutations sans le chiffre 0
                tw = 0
                for i in range(l - 1):
                    tw += cw[i] * a[i]
                zz = l - 1
                for zi in zl:
                    while zz > zi:
                        zz -= 1
                        tw += cws[zz] * a[zz]
                    if tw == 0:
                        r += 1
        else:
            cwa = cw[:al]
            cwb = cw[al:]
            zl = [_ - al for _ in zl]  # Ajuster les indices pour la partie b

            for _a in itertools.combinations(range(1, 10), al):
                ad = collections.defaultdict(int)
                bd = collections.defaultdict(int)

                for a in itertools.permutations(_a):
                    tw = 0
                    for i in range(al):
                        tw += cwa[i] * a[i]
                    ad[tw] += 1

                _b = [_ for _ in range(1, 10) if _ not in _a]
                cws = [cwb[i + 1] - cwb[i] for i in range(bl - 1)]

                for b in itertools.permutations(_b, bl - 1):
                    tw = 0
                    for i in range(bl - 1):
                        tw += cwb[i] * b[i]
                    zz = bl - 1
                    for zi in zl:
                        while zz > zi:
                            zz -= 1
                            tw += cws[zz] * b[zz]
                        bd[tw] += 1

                aa = sorted(ad.items())
                ba = sorted(bd.items(), reverse=True)
                aal = len(aa)
                bal = len(ba)
                ai = bi = 0
                while ai < aal and bi < bal:
                    t = aa[ai][0] + ba[bi][0]
                    if t == 0:
                        r += aa[ai][1] * ba[bi][1]
                        ai += 1
                        bi += 1
                    elif t < 0:
                        ai += 1
                    else:
                        bi += 1

        return r

    # Lecture des cas tant qu'ils ne valent pas 0
    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    # Retourner les résultats pour chaque cas, séparés par des retours à la ligne
    return '\n'.join(map(str, rr))

# Exécuter la fonction principale et afficher le résultat final
print(main())