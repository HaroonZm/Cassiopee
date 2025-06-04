import math  # Importe le module math pour les fonctions mathématiques de base
import string  # Importe le module string pour le traitement des chaînes de caractères
import itertools  # Importe itertools pour travailler avec des itérateurs et générer des combinaisons
import fractions  # Importe le module fractions pour les nombres rationnels
import heapq  # Importe le module heapq pour manipuler des files de priorité (heaps)
import collections  # Importe le module collections qui fournit des structures de données avancées comme defaultdict
import re  # Importe le module re pour les expressions régulières
import array  # Importe le module array pour les structures de tableaux efficaces
import bisect  # Importe bisect pour rechercher et insérer de façon efficace dans une liste triée
import sys  # Importe sys qui fournit des fonctions interactant étroitement avec l’interpréteur Python
import random  # Importe random pour générer des nombres pseudo-aléatoires
import time  # Importe le module time pour gérer les opérations liées au temps
import copy  # Importe copy pour gérer la copie des objets (copie superficielle et profonde)
import functools  # Importe functools pour travailler avec des fonctions d'ordre supérieur (ex: réduire)

# Définit la limite de récursion maximale pour le programme afin d’éviter RecursionError dans les algorithmes profonds
sys.setrecursionlimit(10 ** 7)

# Définit une valeur représentative de l’infini (utilisé pour les comparaisons numériques de grande taille)
inf = 10 ** 20

# Définit une petite valeur epsilon pour la comparaison des flottants (approche de zéro)
eps = 1.0 / 10 ** 10

# Définit le mod pour les calculs modulo (utilisé pour éviter les débordements dans certains algorithmes)
mod = 998244353

# Définit une fonction qui lit une ligne de l'entrée standard, la découpe par espaces et convertit chaque élément en entier
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Définit une fonction qui lit une ligne, convertit chaque valeur en entier et décrémente de 1 (pour l’indexage à partir de zéro)
def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne, découpe chaque élément et convertit en nombre flottant
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne et découpe en liste de chaînes par espace
def LS():
    return sys.stdin.readline().split()

# Fonction qui lit une ligne et la convertit en entier
def I():
    return int(sys.stdin.readline())

# Fonction qui lit une ligne et la convertit en flottant
def F():
    return float(sys.stdin.readline())

# Fonction qui lit une ligne de l'utilisateur via 'input'
def S():
    return input()

# Fonction qui affiche une chaîne (s) et force le flush du buffer de sortie
def pf(s):
    return print(s, flush=True)

# Fonction principale du programme. Elle réalise le traitement sur les données lues.
def main():
    rr = []  # Initialise une liste vide qui va stocker les résultats finaux

    while True:  # Boucle infinie, permet d’enchaîner plusieurs traitements si besoin (ici interrompue par break)
        # Lit 10 lignes d’entrées, chaque ligne étant une liste de 10 entiers (10x10 matrice)
        a = [LI() for _ in range(10)]

        sm = {}  # Initialise un dictionnaire vide pour associer à chaque nombre à 4 chiffres un résultat de transition

        # Boucle sur tous les entiers de 0 à 9999 (inclus), donc tous les nombres à 4 chiffres (pouvant commencer par zéro)
        for i in range(10 ** 4):
            c = 0  # Variable compteur, utilisée ici comme point de départ (état initial)
            t = 10 ** 3  # Place du chiffre la plus à gauche (milliers). On va la diviser à chaque itération.
            # Décompose le nombre 'i' en ses 4 chiffres. Ex: 1234 => 1, 2, 3, 4
            while t > 0:
                k = (i // t) % 10  # Extraire le chiffre à la position t (millier, centaine, dizaine, unité respectivement)
                c = a[c][k]  # On « transite » d’un état à l’autre en utilisant la matrice a
                t //= 10  # Passe à la position suivante (ex: de millier à centaine)
            sm[i] = c  # Le résultat final pour le nombre i est stocké dans sm avec la clé i

        # Crée un graphe des transitions possibles entre nombres à 4 chiffres par des changements de chiffres ou d’ordres
        e = collections.defaultdict(set)  # Crée un dictionnaire avec des ensembles comme valeurs pour y ajouter rapidement des voisins

        # Boucle imbriquée sur tous les chiffres des quatre positions (i: millier, j: centaine, k: dizaine, l: unité)
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        t = i * 1000 + j * 100 + k * 10 + l  # Calcule la valeur du nombre à 4 chiffres formé par i, j, k, l

                        # Pour chaque position, teste tous les remplacements possibles de chaque chiffre par un autre (m)
                        for m in range(10):

                            # Si le chiffre des milliers i est différent de m, remplace-le par m
                            if i != m:
                                u = m * 1000 + j * 100 + k * 10 + l  # Forme le nouveau nombre en remplaçant i par m
                                e[t].add(u)  # Ajoute la nouvelle valeur comme « voisin » accessible depuis t

                            # Même principe pour la centaine (j)
                            if j != m:
                                u = i * 1000 + m * 100 + k * 10 + l
                                e[t].add(u)

                            # Dizaine (k)
                            if k != m:
                                u = i * 1000 + j * 100 + m * 10 + l
                                e[t].add(u)

                            # Unité (l)
                            if l != m:
                                u = i * 1000 + j * 100 + k * 10 + m
                                e[t].add(u)

                            # On permute deux chiffres s'ils sont différents (millier <-> centaine)
                            if i != j:
                                u = j * 1000 + i * 100 + k * 10 + l
                                e[t].add(u)

                            # Permutation (centaine <-> dizaine)
                            if j != k:
                                u = i * 1000 + k * 100 + j * 10 + l
                                e[t].add(u)

                            # Permutation (dizaine <-> unité)
                            if k != l:
                                u = i * 1000 + j * 100 + l * 10 + k
                                e[t].add(u)

        r = 0  # Compteur du nombre de configurations vérifiant certaines conditions

        # Parcours tous les nombres à 4 chiffres possibles
        for i in range(10 ** 4):
            t = sm[i]  # Récupère le résultat (état) pour ce nombre à partir de « sm »

            # Teste une première condition sur la relation entre i, t et la matrice a
            # i % 10 donne le chiffre des unités du nombre i
            # sm[i - i % 10 + t] donne le résultat pour le nombre dont le chiffre d'unité est t
            # a[...][][] teste la case correspondante de la matrice
            if i % 10 != t and a[sm[i - i % 10 + t]][i % 10] == 0:
                r += 1  # Incrémente le compteur si la condition est remplie
                continue  # Passe à l’itération suivante

            f = False  # Drapeau pour vérifier une autre condition, initialement faux

            # Boucle sur tous les chiffres de 0 à 9 pour tester si depuis l’état t on peut aller vers un autre état m via a
            for m in range(10):
                if m == t:
                    continue  # On ne traite pas le cas où m == t, passer à l'itération suivante
                if a[t][m] == 0:  # Si la transition de t vers m n’est pas permise (matrice a), le drapeau est mis à Vrai
                    f = True
                    r += 1  # Compte ce cas comme vérifié
                    break  # On sort de la boucle m car la condition suffit

            if f:  # Si la condition précédente était valide, on n’a pas besoin de vérifier la suite
                continue

            # Pour chaque voisin k accessible à un pas de t (càd à une modification ou permutation près), on teste une propriété sur a
            for k in e[i]:
                if a[sm[k]][t] == 0:  # Si la transition n’est pas permise dans la matrice, on compte ce cas
                    r += 1
                    break  # On peut arrêter la recherche pour ce i dès que la condition est vérifiée

        rr.append(r)  # Ajoute le résultat pour cette matrice a (cas courant)

        break  # On sort de la boucle principale (puisqu’on ne lit qu’une seule matrice d’entrée)

    # Génère une chaîne représentant tous les résultats ligne par ligne (comme demandé dans certains problèmes de juges en ligne)
    return '\n'.join(map(str, rr))

# Appelle la fonction principale et affiche son résultat (entrée-sortie standard, typique des problèmes de concours programmés)
print(main())