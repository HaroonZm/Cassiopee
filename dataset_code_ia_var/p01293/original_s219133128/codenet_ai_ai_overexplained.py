#!/usr/bin/env python3

# Importation de modules de la bibliothèque standard Python

from collections import defaultdict, deque      # defaultdict : dictionnaire avec valeur par défaut ; deque : structure de file (double-ended queue)
from heapq import heappush, heappop            # heappush et heappop : gestion de files à priorité (min-heaps)
from bisect import bisect_left, bisect_right   # bisect_left, bisect_right : recherche d'insertion binaire dans des listes triées
import sys, random, itertools, math            # sys : outils système (stdin, etc.), random : hasard, itertools : outils itératifs, math : fonctions mathématiques

# Augmentation de la limite de récursion maximale (le nombre d'appels récursifs permis avant interruption)
sys.setrecursionlimit(10**5)

# Redéfinition de la fonction input pour lire une ligne depuis l'entrée standard
input = sys.stdin.readline

# Association locale de la fonction math.sqrt pour un accès plus rapide à la racine carrée
sqrt = math.sqrt

# Définition de fonctions d'entrée de données utiles, pour faciliter la lecture et l'écriture du code :

def LI(): 
    # Lit une ligne, découpe en morceaux par espace, transforme chaque morceau en int, retourne sous forme de liste d'entiers
    return list(map(int, input().split()))

def LF(): 
    # Lit une ligne, découpe en morceaux par espace, transforme chaque morceau en float, retourne sous forme de liste de flottants
    return list(map(float, input().split()))

def LI_(): 
    # Comme LI(), mais retire 1 à chaque élément (pour passage en indices 0-based utiles en programmation)
    return list(map(lambda x: int(x)-1, input().split()))

def II(): 
    # Lit une ligne, supprime l'espace en fin de ligne, transforme en int et retourne la valeur (utile pour un seul entier)
    return int(input())

def IF(): 
    # Lit une ligne, supprime l'espace en fin de ligne, transforme en flottant
    return float(input())

def LS(): 
    # Lit une ligne, découpe par espace, chaque morceau devient une liste contenant les caractères du mot
    return list(map(list, input().split()))

def S(): 
    # Lit une ligne, supprime l'espace en fin de ligne, retourne la liste des caractères (chaîne en liste de caractères)
    return list(input().rstrip())

def IR(n): 
    # Pour n lignes, lit un entier à chaque fois, retourne la liste des entiers lus
    return [II() for _ in range(n)]

def LIR(n): 
    # Pour n lignes, lit chaque ligne comme une liste d'entiers, retourne une liste de listes d'entiers
    return [LI() for _ in range(n)]

def FR(n): 
    # Pour n lignes, lit un flottant par ligne, retourne une liste de flottants
    return [IF() for _ in range(n)]

def LFR(n): 
    # Pour n lignes, lit toute la ligne comme liste d'entiers, retourne liste de listes
    return [LI() for _ in range(n)]

def LIR_(n): 
    # Pour n lignes, lit chaque ligne comme liste d'entiers en enlevant 1 à chaque entier (0-based), retourne liste de listes
    return [LI_() for _ in range(n)]

def SR(n): 
    # Pour n lignes, lit chaque ligne, transforme en liste de caractères, retourne liste de listes de caractères
    return [S() for _ in range(n)]

def LSR(n): 
    # Pour n lignes, lit chaque ligne avec LS(), retourne liste de listes
    return [LS() for _ in range(n)]

# Déclaration de deux constantes utiles
mod = 1000000007           # Modulo typique pour éviter les débordements dans les problèmes de nombre (notamment en compétitions)
inf = 1e10                 # Grande valeur représentant l'infini (ici 10^10)

# Fonction principale de résolution par lot
def solve():
    # Lecture de la première ligne (le nom de la couleur atout dans une partie de bridge, ou "#" pour arrêter) ;
    n = input().rstrip()   # .rstrip() permet de supprimer les retours à la ligne en fin d'entrée

    # Condition d'arrêt : si la valeur entrée est un dièse ("#"), on doit mettre fin à la boucle d'exécution principale
    if n == "#":
        return False   # On retourne False pour indiquer à la boucle principale qu'on doit s'arrêter

    # Lecture des 4 lignes suivantes, chacune décrivant la "main" (les cartes détenues) d'un joueur
    lis = [LS() for i in range(4)]  # Chaque lis[i] sera une liste de 13 éléments (représentant les 13 cartes de ce joueur, chaque carte étant une chaîne de 2 caractères)

    # Liste de toutes les valeurs possibles de cartes dans l'ordre croissant, du 2 à l'as (A)
    num = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    ans = [0] * 4   # Initialisation du score pour chaque joueur : ans[0]=Nord, ans[1]=Est, ans[2]=Sud, ans[3]=Ouest
    master = 0      # La variable 'master' repère l'indice du joueur qui mène le prochain pli (au départ, joueur 0, c'est à dire Nord)

    # Boucle sur les 13 plis (chaque joueur joue une carte à chaque tour donc il y a 13 tours/plis)
    for i in range(13):

        # Extraction de la carte jouée par chaque joueur pour ce pli
        north, east, south, west = lis[0][i], lis[1][i], lis[2][i], lis[3][i]
        
        # Liste des couleurs jouées par chaque joueur pour ce pli (la couleur est le 2e caractère de la chaîne de 2 caractères)
        suit = [north[1], east[1], south[1], west[1]]

        # tmp sera la paire (indice de la valeur de la carte du "master", indice du joueur du "master")
        # On suppose par défaut que le maître du pli sera celui qui a joué la plus forte carte dans la couleur demandée par le "master"
        tmp = [num.index(lis[master][i][0]), master]

        # Si un atout (couleur demandée par l'utilisateur/n) est présent dans le pli
        if n in suit:
            # tmp cherche à déterminer pour ce pli, le joueur ayant la plus forte carte d'atout dans ce pli
            tmp = [-1, -1]
            for k in range(4):   # On parcourt les 4 joueurs
                if suit[k] == n:   # Si la couleur jouée par le joueur k est la couleur d'atout
                    if tmp[0] < num.index(lis[k][i][0]):  # On compare la valeur de la carte avec la meilleure trouvée jusqu'à présent
                        tmp = [num.index(lis[k][i][0]), k]  # On retient l'indice de la carte et le numéro du joueur
        else:
            # Si aucun atout n'a été joué, la main reviendra à celui qui a joué la carte la plus forte dans la couleur demandée
            for k in range(4):
                # Vérifie si la couleur jouée vaut la couleur demandée, et si la valeur de la carte est plus forte que celle précédemment retenue
                if suit[tmp[1]] == suit[k] and tmp[0] < num.index(lis[k][i][0]):
                    tmp = [num.index(lis[k][i][0]), k]

        # Incrémente le nombre de plis remportés par le gagnant de ce pli
        ans[tmp[1]] += 1

        # Le joueur gagnant ce pli commence le pli suivant
        master = tmp[1]

    # Calcul du score de l'équipe Nord-Sud (sont joueurs 0 et 2), soustraction de 6 (par convention, seuls les plis au-dessus de 6 sont scorisés)
    a = ans[0] + ans[2] - 6

    # Calcul du score de l'équipe Est-Ouest (joueurs 1 et 3)
    b = ans[1] + ans[3] - 6

    # Affichage du résultat : on affiche 'NS' si Nord-Sud ont gagné, sinon on affiche 'EW' pour Est-Ouest, suivi du score
    if a > b:
        print("NS {}".format(a))
    else:
        print("EW {}".format(b))

    # Retourner True pour poursuivre la boucle principale des parties
    return True

# Partie principale du programme (point d'entrée)
if __name__ == '__main__':
    # Boucle principale : tant que solve() retourne True (c'est-à-dire qu'on n'a pas lu "#"), on traite une nouvelle partie
    while solve():
        pass   # pass indique ici qu'aucune opération supplémentaire n'est requise dans la boucle (le traitement est dans solve())