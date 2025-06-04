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

# Augmente la limite de récursion définie pour éviter l'erreur de profondeur maximale dans certains cas extrêmes.
sys.setrecursionlimit(10 ** 7)

# Constantes utiles à travers le programme
inf = 10 ** 20                  # Une valeur représentant l'infini, pour les comparaisons ou initialisations
eps = 1.0 / 10 ** 10            # Un epsilon pour comparer des nombres flottants
mod = 10 ** 9 + 7               # Modulo utilisé pour réduire les grands entiers
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]              # Déplacements (haut, droite, bas, gauche)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), 
       (1, 0), (1, -1), (0, -1), (-1, -1)]            # Déplacements pour les 8 directions autour d'un point

def LI():
    """
    Lit une ligne de l'entrée standard, découpe les éléments séparés par des espaces,
    et les convertit en entiers.

    Returns:
        list[int]: Liste d'entiers lus de l'entrée.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Même comportement que LI, mais décrémente chaque entier de 1.
    Utile pour les indices de base 0 dans certaines tâches de programmation.

    Returns:
        list[int]: Liste d'entiers (décalés de -1) de l'entrée.
    """
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne de l'entrée standard et convertit les entrées en flottants.

    Returns:
        list[float]: Liste de flottants issus de l'entrée standard.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne de l'entrée standard et la découpe en liste de chaînes par espaces.

    Returns:
        list[str]: Liste de chaînes de caractères issues de la ligne lue.
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier à partir de l'entrée standard.

    Returns:
        int: L'entier lu depuis l'entrée.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un flottant à partir de l'entrée standard.

    Returns:
        float: Le flottant lu de l'entrée.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une ligne entière de l'entrée standard (en utilisant input pour compatibilité).

    Returns:
        str: La chaîne lue depuis l'entrée standard (ligne complète).
    """
    return input()

def pf(s):
    """
    Affiche un message immédiatement (sans mise en cache) sur la sortie standard.

    Args:
        s (Any): Le message à afficher.
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale du programme. Lit les jeux de données et applique la logique dédiée 
    pour chaque jeu jusqu'à ce qu'une ligne de terminaison soit rencontrée (n == 0).
    Construit les résultats pour chaque jeu de données et les imprime à la fin.

    Returns:
        str: Les résultats pour chaque test, linéaires, séparés par des retours à la ligne.
    """
    rr = []  # Liste pour stocker les résultats de chaque cas

    def f(t, d, l):
        """
        Traite un ensemble d'entrées selon les critères fournis.

        Args:
            t (int): Nombre d'éléments dans la séquence.
            d (int): Portée ou profondeur d'une opération affectant la séquence.
            l (int): Valeur seuil pour activer le marquage d'un élément.

        Returns:
            int: Le total d'éléments marqués, sauf le dernier (r[:-1]).
        """
        # Lecture de t entiers depuis l'entrée standard
        a = [I() for _ in range(t)]
        # Tableau pour marquer les éléments sélectionnés
        r = [0] * t
        # Parcours de droite à gauche
        for i in range(t-1, -1, -1):
            c = a[i]
            # Si la valeur courante dépasse ou égale le seuil l
            if c >= l:
                r[i] = 1  # Marque l'élément courant
                # Marque d'éventuels éléments suivants dans la portée d, sauf si déjà marqué
                for j in range(i+1, min(i+d, t)):
                    if r[j] > 0:
                        break  # On arrête si on retombe sur un déjà marqué
                    r[j] = 1  # On marque aussi cet élément
        return sum(r[:-1])  # Retourne le total, en ignorant le dernier élément

    # Boucle principale de lecture des jeux de données jusqu'à entrée qui commence par 0
    while True:
        n, m, l = LI()
        if n == 0:
            break
        rr.append(f(n, m, l))

    # Concatène chaque résultat sur une ligne différente
    return '\n'.join(map(str, rr))

# Appel principal de la fonction main et affiche le résultat
print(main())