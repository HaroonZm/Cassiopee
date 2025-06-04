import math  # Importation du module math, fournit des fonctions mathématiques de base comme sqrt, sin, etc.
import string  # Importation du module string, offre des constantes et des classes utiles pour les chaînes de caractères.
import itertools  # Module pour créer et manipuler des itérateurs efficaces, par exemple cycle, permutations, etc.
import fractions  # Permet de manipuler des fractions (nombres rationnels) précisément.
import heapq  # Fournit une implémentation du tas, une structure de données efficace pour les files de priorité.
import collections  # Fournit des structures de conteneur alternatives comme deque, Counter, etc.
import re  # Module pour les expressions régulières (recherche de motifs dans les chaînes).
import array  # Donne accès à la structure de données tableau efficace (plus compact que list pour des types homogènes).
import bisect  # Fournit un ensemble d’outils pour le tri et la recherche dans les listes triées.
import sys  # Donne accès à des variables et fonctions système comme stdin, stdout, argv, etc.
import random  # Fournit des outils pour générer des nombres aléatoires, mélanger des listes, etc.
import time  # Permet de manipuler le temps (obtenir l'heure, mesurer des durées, faire des pauses, etc).
import copy  # Facilite la copie superficielle et profonde d'objets complexes.
import functools  # Offre des fonctions utilitaires pour les fonctions (comme reduce, lru_cache, etc).

# Modifie la profondeur maximale de récursion du programme
# Par défaut elle est d'environ 1000, ici on la pousse à 10 millions pour éviter d'atteindre la limite lors de récursions profondes
sys.setrecursionlimit(10**7)

# Définition d'une constante pour représenter un nombre très grand (par exemple l'infini dans ce contexte)
inf = 10**20

# Définition d'une petite valeur epsilon, utile pour comparer des nombres flottants en évitant les problèmes d'arrondi
eps = 1.0 / 10**10

# Valeur d'un grand nombre premier fréquemment utilisé dans les problèmes de programmation modulaire (notamment en compétition)
mod = 998244353

# Définition de la direction pour se déplacer sur une grille de 4 manières : haut, droite, bas, gauche (dx, dy)
dd = [(0,-1), (1,0), (0,1), (-1,0)]

# Définition de la direction pour se déplacer sur une grille de 8 manières : inclut les diagonales
ddn = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,-1), (-1,0), (-1,1)]

# Fonction utilitaire : lit une ligne de l'entrée standard, sépare selon les espaces, convertit chaque partie en int et retourne sous forme de liste
def LI(): 
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction similaire à LI, mais soustrait 1 à chaque élément (utile pour la conversion index 1-based <-> 0-based)
def LI_(): 
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction utilitaire : lit une ligne, la découpe selon les espaces et convertit chaque élément en float
def LF(): 
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction utilitaire : lit une ligne, la découpe selon les espaces et retourne une liste de chaînes
def LS(): 
    return sys.stdin.readline().split()

# Fonction utilitaire : lit une ligne et la convertit en entier, retourne ce nombre
def I(): 
    return int(sys.stdin.readline())

# Fonction utilitaire : lit une ligne et la convertit en flottant
def F(): 
    return float(sys.stdin.readline())

# Fonction utilitaire : lit une ligne venant de l'entrée utilisateur (sans suppression du \n), retourne la chaîne
def S(): 
    return input()

# Fonction utilitaire : effectue un print avec flush=True (vide le tampon immédiatement)
def pf(s): 
    return print(s, flush=True)

# Déclaration de la fonction principale qui va contenir la logique principale du programme
def main():
    rr = []  # Création d'une liste vide pour stocker les résultats pour chaque jeu traité
    mk = {}  # Dictionnaire pour faire la correspondance entre la représentation des cartes (T, J, Q, ...) et leur valeur numérique

    # On attribue les valeurs numériques pour les figures dans un jeu de cartes (T, J, Q, K, A)
    mk['T'] = 10  # T pour Ten
    mk['J'] = 11  # J pour Jack
    mk['Q'] = 12  # Q pour Queen
    mk['K'] = 13  # K pour King
    mk['A'] = 14  # A pour Ace

    # Pour les cartes numérotées 1 à 9, on fait la correspondance "str" vers int
    for i in range(1, 10):  # Boucle de 1 à 9 inclus
        mk[str(i)] = i

    # On boucle pour traiter chacun des cas de test ; s'arrête lorsque l'utilisateur entre une ligne contenant uniquement "#"
    while True:
        t = S()  # On lit la prochaine ligne depuis l'entrée standard ; ceci représente l'atout (couleur qui coupe)
        if t == '#':  # Si la ligne vaut "#", c'est un signal de fin de données d'entrée, on quitte la boucle
            break

        # a va contenir les données des 4 joueurs pour cette partie
        # Pour chaque joueur (4 au total), on lit une ligne avec 13 cartes
        # Pour chaque carte, on l'associe à un tuple (valeur numérique de la carte, couleur)
        a = [
            list(
                map(  # On applique une fonction à chaque élément d'une liste
                    lambda x: (mk[x[0]], x[1]),  # x[0] est le caractère de valeur, x[1] celui de couleur
                    LS()  # On lit une ligne pour ce joueur et on découpe par espaces pour obtenir les cartes
                )
            )
            for _ in range(4)  # Il y a 4 joueurs, donc on répète 4 fois
        ]

        d = 0  # Variable indiquant qui commence à jouer (0 pour le premier joueur)
        ns = 0  # Compteur de plis remportés par l'équipe NS (Nord-Sud) ; joueurs 0 et 2
        ew = 0  # Compteur de plis remportés par l'équipe EW (Est-Ouest) ; joueurs 1 et 3

        # On va maintenant simuler les 13 plis de la partie (car chaque joueur a 13 cartes)
        for i in range(13):
            m = -1  # Initialisation de la valeur maximale rencontrée pour le pli courant
            mi = -1  # Index du joueur qui a joué la meilleure carte jusqu'à présent pour le pli courant
            it = a[d][i][1]  # Couleur demandée pour ce pli (c'est la couleur de la carte jouée par le premier joueur de ce pli)

            # On vérifie chaque joueur pour voir s’il peut surcouper, suivre, ou surenchérir
            for j in range(4):  # 4 joueurs à chaque pli
                k = a[j][i][0]  # On prend la valeur de la carte pour ce joueur et ce pli

                # Si le joueur joue une carte de la couleur d'atout (couleur pour "couper"), on lui attribue 100 points fictifs supplémentaires
                if a[j][i][1] == t:
                    k += 100  # Cela va faire gagner la priorité à une carte d'atout

                # Si le joueur joue une carte de la couleur demandée, on lui attribue 50 points fictifs supplémentaires (sauf si c'était déjà l'atout)
                if a[j][i][1] == it:
                    k += 50

                # On conserve l'index du joueur ayant pour l'instant la carte la plus forte du pli
                if m < k:
                    m = k  # Nouvelle meilleure valeur
                    mi = j  # Index du joueur

            d = mi  # Le joueur gagnant devient le premier à jouer au prochain pli

            # Attribution du pli au camp NS ou EW selon si le gagnant a un index pair (NS) ou impair (EW)
            if mi % 2 == 0:  # Joueurs 0 et 2 sont l'équipe NS (indices pairs)
                ns += 1
            else:  # Joueurs 1 et 3 sont l'équipe EW (indices impairs)
                ew += 1

        # Après les 13 plis, on détermine le résultat
        # L'équipe ayant plus de 6 plis remporte la manche ; le score est le nombre de plis au-delà de 6
        if ns > 6:
            rr.append('NS {}'.format(ns - 6))  # Equipe NS a gagné, on stock le résultat
        else:
            rr.append('EW {}'.format(ew - 6))  # Sinon c'est EW qui a gagné

    # On retourne les résultats pour tous les jeux comme une seule chaîne, avec une ligne par résultat
    return '\n'.join(map(str, rr))

# Appel de la fonction principale et affichage du résultat final dans la console
print(main())