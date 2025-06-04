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

# Augmente la limite de récursion pour permettre des appels profonds si nécessaire
sys.setrecursionlimit(10**7)

# Définition de constantes souvent utilisées
inf = 10**20  # Une valeur représentant l'infini
eps = 1.0 / 10**10  # Petite valeur epsilon pour la comparaison de flottants
mod = 998244353  # Module pour la réduction de grands entiers

def LI():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste d'entiers.
    Returns:
        list[int]: Liste d'entiers lus sur la ligne.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste d'entiers décrémentés de 1.
    Returns:
        list[int]: Liste d'entiers (décalés de -1) lus sur la ligne.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste de flottants.
    Returns:
        list[float]: Liste de flottants lus sur la ligne.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et la convertit en une liste de chaînes.
    Returns:
        list[str]: Liste de mots lus sur la ligne.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit une ligne de l'entrée standard et la convertit en entier.
    Returns:
        int: Entier lu sur la ligne.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit une ligne de l'entrée standard et la convertit en flottant.
    Returns:
        float: Flottant lu sur la ligne.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne de l'entrée standard.
    Returns:
        str: Chaîne de caractères lue.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne de caractères et force l'affichage immédiat (flush).
    Args:
        s (str): La chaîne de caractères à afficher.
    Returns:
        None
    """
    return print(s, flush=True)

def main():
    """
    Résout le problème principal en lisant des séquences de longueurs diverses depuis l'entrée standard et
    détermine pour chaque séquence l'une des valeurs : 'none', 'ambiguous' ou un entier, et les affiche ligne par ligne.
    Les instructions pour les séquences sont les suivantes :
        - Chaque élément peut être un entier ou le caractère 'x'.
        - Les contraintes et règles sont imposées sur les valeurs et leur position par rapport aux éléments adjacents.
    Returns:
        str: Une chaîne contenant toutes les réponses, une par ligne, jointe par '\n'.
    """
    rr = []  # Liste de résultats pour chaque séquence traitée

    while True:
        n = I()  # Lit le nombre d'éléments de la séquence
        if n == 0:
            break  # Fin de l'entrée, on arrête

        a = LS()  # Lit la séquence sous forme de liste de chaînes ('x' ou entiers)
        r = None  # Initialisation du résultat pour la séquence courante

        # Phase 1 : Vérification de la structure et validation primaire
        for i in range(n):
            if a[i] == 'x':
                # Deux 'x' consécutifs ne sont pas permis
                if i > 0 and a[i-1] == 'x':
                    r = 'none'
                    break
            else:
                a[i] = int(a[i])  # Conversion en entier pour les éléments connus
                if i > 0 and a[i-1] != 'x':
                    # Vérifie si la séquence respecte les contraintes des positions paires/impaires
                    if i % 2 == 0:
                        if a[i-1] <= a[i]:
                            r = 'none'
                            break
                    elif a[i-1] >= a[i]:
                        r = 'none'
                        break

        if r:
            # Si une irrégularité a été détectée ci-dessus, on ajoute le résultat et on passe à la séquence suivante
            rr.append(r)
            continue

        ma = -inf  # valeur maximale possible pour remplacer les 'x' aux positions impaires
        mi = inf   # valeur minimale possible pour remplacer les 'x' aux positions paires

        # Phase 2 : Détermination des bornes pour les 'x'
        for i in range(n):
            if a[i] != 'x':
                continue  # Ignore les éléments qui ne sont pas 'x'

            if i % 2 == 0:
                # 'x' à une position paire, cherche la plus petite borne supérieure
                if i > 0:
                    mi = min(mi, a[i-1]-1)
                if i < n-1:
                    mi = min(mi, a[i+1]-1)
            else:
                # 'x' à une position impaire, cherche la plus grande borne inférieure
                if i > 0:
                    ma = max(ma, a[i-1]+1)
                if i < n-1:
                    ma = max(ma, a[i+1]+1)

        # Phase 3 : Détermination du résultat final
        if ma == mi:
            # Il existe une unique valeur possible pour les 'x'
            rr.append(ma)
        elif ma == -inf or mi == inf:
            # Impossible de déterminer une valeur (trop ambigu)
            rr.append('ambiguous')
        elif ma > mi:
            # Pas de valeur possible qui satisfait toutes les contraintes
            rr.append('none')
        else:
            # Plusieurs valeurs possibles (ambigüité)
            rr.append('ambiguous')

    # Retourne tous les résultats séparés par une nouvelle ligne
    return '\n'.join(map(str, rr))

# Exécute la fonction principale et affiche son résultat
print(main())