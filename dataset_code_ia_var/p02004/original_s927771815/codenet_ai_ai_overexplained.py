# Importation de nombreux modules standards de la bibliothèque Python.
# Certains de ces modules sont utilisés dans divers scénarios, pour le traitement mathématique,
# la manipulation de texte, la gestion de listes, les files de priorité, les collections, les expressions régulières, etc.
import math  # Module mathématique : fonctions math (par ex., sqrt, sin, cos, …)
import string  # Module de chaînes : fonctions utiles pour manipuler des chaînes de caractères.
import itertools  # Module pour la manipulation d’itérateurs efficaces.
import fractions  # Pour travailler avec des fractions (nombres rationnels).
import heapq  # Fournit une file de priorité basée sur le tas binaire (heap).
import collections  # Fournit des structures de données optimisées (deque, Counter, etc.)
import re  # Module expressions régulières.
import array  # Pour manipuler des tableaux typés.
import bisect  # Algorithmes pour insérer dans des listes ordonnées.
import sys  # Interaction avec l'environnement système (par exemple, stdin, stdout, arguments).
import random  # Génération de nombres pseudo-aléatoires.
import time  # Fournit des fonctions liées au temps.
import copy  # Pour faire des copies superficielles ou profondes d’objets.
import functools  # Fournit des fonctions utilitaires comme reduce, lru_cache, etc.

# Modifie la limite maximale de récursion autorisée dans le programme.
# Par défaut, elle est environ à 1000; ici, elle est fixée à 10 millions (10 puissance 7).
sys.setrecursionlimit(10**7)

# Définit la valeur de infini comme 10 puissance 20.
# Peut être utilisée dans les algorithmes où une valeur initiale très grande est requise,
# par exemple dans la programmation dynamique ou les plus courts chemins.
inf = 10**20

# Définit une très petite valeur epsilon pour comparer des nombres flottants avec tolérance.
eps = 1.0 / 10**10

# Définition de la constante pour le modulo, couramment utilisée pour éviter le dépassement de capacité
# ou pour respecter les contraintes des problèmes de compétitions de programmation.
mod = 10**9+7  # 1000000007 est un nombre premier souvent utilisé.

# Définit les directions pour les déplacements dans une grille (haut, droite, bas, gauche).
# Chaque tuple (dx, dy) définit un déplacement sur l'axe x et y respectivement.
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Définit les directions pour les déplacements dans une grille 8 directions (haut, haut-droite, droite, ..., haut-gauche).
# Utile lors des recherches dans toutes les directions autour d'une cellule dans une matrice.
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Définition de fonctions utilitaires pour la lecture de l’entrée standard.
# Chacune lit une ligne depuis sys.stdin et retourne les valeurs dans le type approprié.

# Lit une ligne, sépare par espaces, convertit chaque élément en int et retourne la liste.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Pareil que LI, mais décrémente chaque int de 1 (utile pour transformer des indices 1-based en 0-based).
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Lit une ligne, sépare par espaces, convertit chaque élément en float, retourne la liste.
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne, sépare par espaces, retourne la liste de chaînes résultantes.
def LS():
    return sys.stdin.readline().split()

# Lit une ligne, convertit en int, retourne la valeur.
def I():
    return int(sys.stdin.readline())

# Lit une ligne, convertit en float, retourne la valeur.
def F():
    return float(sys.stdin.readline())

# Lit une ligne depuis l’entrée standard, retourne la valeur telle quelle (sous forme de chaîne).
def S():
    return input()

# Fonction utilitaire : affiche un message à l’écran (print) et force l’écriture immédiate sur la sortie standard.
def pf(s):
    return print(s, flush=True)

# Définition de la fonction principale du programme
def main():
    # Création d'une liste vide pour stocker les résultats calculés.
    rr = []

    # Définition d'une fonction interne "f" qui compte le nombre de motifs "RRRR"
    # dans la chaîne d'entrée n, en respectant aussi le motif inverse (4 autres caractères).
    def f(n):
        # Déclaration et initialisation de variables locales.
        r = 0  # Compteur pour le nombre total de motifs "RRRR" trouvés.
        t = 0  # Compteur intermédiaire pour compter le nombre de "R" consécutifs ; peut aussi être négatif.

        # Parcours de chaque caractère de la chaîne n, un par un.
        for c in n:
            # Vérifie si le caractère courant est 'R'.
            if c == 'R':
                t += 1  # Incrémente t de 1 pour chaque 'R' trouvée consécutivement.
                # Quand t atteint 4, cela signifie qu'on a trouvé 4 'R' consécutifs.
                if t == 4:
                    r += 1  # Incrémente le compteur de motifs "RRRR".
                    t = 0  # Réinitialise t à 0 pour recommencer un nouveau comptage.
            else:
                # Si le caractère n'est pas 'R' (autre caractère), décrémente t de 1.
                t -= 1
                # Quand t atteint -4 (par exemple 4 fois un caractère différent de 'R'),
                # on réinitialise t à 0 (remise à zéro du compteur).
                if t == -4:
                    t = 0
        # Retourne le nombre total de motifs "RRRR" trouvés dans la chaîne.
        return r

    # Boucle infinie qui sera brisée manuellement (fonctionne comme "do while True" en d'autres langages).
    while 1:
        # Lit une chaîne à partir de l'entrée standard.
        n = S()
        # Vérifie si la chaîne entrée correspond à "0" (fin d'entrée).
        if n == 0:
            break  # Sort de la boucle si condition remplie.
        # Calcule le résultat pour cette chaîne, ajoute à la liste des résultats.
        rr.append(f(n))
        # Sort immédiatement de la boucle, donc ne traite qu'une seule entrée (peut refléter une modification temporaire/test).
        break

    # Transforme tous les éléments de la liste de résultats rr en chaînes de caractères
    # et les joint à l'aide d'un retour à la ligne, puis retourne la chaîne résultante.
    return '\n'.join(map(str, rr))

# Appelle la fonction principale et affiche le résultat sur la sortie standard.
print(main())