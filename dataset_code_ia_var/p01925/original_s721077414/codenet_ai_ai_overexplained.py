# Importation du module 'defaultdict' qui fournit un dictionnaire avec une valeur par défaut pour les clés manquantes
from collections import defaultdict, deque  # 'deque' fournit une structure de file d'attente rapide

# Importation de plusieurs modules standards
import sys  # Le module 'sys' permet l'accès à des fonctionnalités spécifiques à l'interpréteur Python
import heapq  # 'heapq' fournit une implémentation du tas (heap), utile pour les files de priorité
import bisect  # 'bisect' permet la recherche et l'insertion efficace dans des séquences ordonnées
import math  # 'math' fournit des fonctions mathématiques standard
import itertools  # 'itertools' fournit des outils pour créer et utiliser des itérateurs efficaces
import string  # 'string' fournit des fonctions pour manipuler des chaînes de caractères
import queue  # 'queue' fournit des files d'attente synchronisées
import copy  # 'copy' fournit des fonctions pour dupliquer des objets (copie superficielle ou profonde)
import time  # 'time' fournit des fonctions pour mesurer le temps

# Modification de la limite de récursion de l'interpréteur Python
sys.setrecursionlimit(10**8)  # Définit la profondeur maximale de la pile d'appels récursifs à un nombre très élevé

# Définition de constantes globales
INF = float('inf')  # Représente l'infini en virgule flottante, utile comme valeur sentinelle
mod = 10**9 + 7  # Un grand nombre premier, souvent utilisé pour les calculs modulo
eps = 10**-7  # Petite valeur epsilon, utile pour la comparaison de flottants

# Définition de fonctions utilitaires pour l'entrée standard

def inp():
    # Fonction pour lire un entier depuis l'entrée standard
    # input() prend une ligne saisie par l'utilisateur sous forme de chaîne de caractères
    # int() convertit cette chaîne en entier
    return int(input())

def inpl():
    # Fonction pour lire une liste d'entiers saisie sur une seule ligne
    # input() lit une ligne, split() la découpe en liste par espaces
    # map(int, ...) convertit chaque élément en entier
    # list() transforme l'itérateur en liste réelle
    return list(map(int, input().split()))

def inpl_str():
    # Fonction pour lire une liste de chaînes de caractères saisie sur une seule ligne
    # input().split() découpe la ligne en une liste de mots (str)
    return list(input().split())

# Boucle principale qui traite plusieurs cas de test
while True:
    # Lecture de deux entiers N et M à partir de l'entrée standard
    N, M = inpl()  # N est le nombre d'éléments, M est le nombre de requêtes ou d'opérations

    # Vérifie si les deux valeurs sont 0, ce qui marque la fin des entrées
    if N == 0 and M == 0:
        break  # Sort de la boucle principale lorsque la condition d'arrêt est satisfaite
    else:
        # Création de deux listes pour garder les totaux minimaux et maximaux, ainsi que les indices
        # Chaque élément de MINlist sera une liste [valeur_totale_minimale, indice_elements]
        MINlist = [[0, i] for i in range(N)]
        # Chaque élément de MAXlist sera une liste [valeur_totale_maximale, indice_elements]
        MAXlist = [[0, i] for i in range(N)]

        # Boucle sur chacune des M opérations lignes à traiter
        for _ in range(M):
            # Lecture d'une liste d'entiers de la ligne suivante
            arg = inpl()  # Par exemple [s, k, c1, c2, ..., ci]
            s = arg[0]  # Première valeur : 's', qui semble être une sorte de score ou point à distribuer
            k = arg[1]  # Deuxième valeur : 'k', qui semble être un drapeau (utilisé comme condition)
            cc = arg[2:]  # Toutes les valeurs restantes : 'cc', une liste d'indices d'éléments (indexés à partir de 1)

            # Boucle sur chaque indice dans la liste cc pour mise à jour du score maximal
            for c in cc:
                MAXlist[c - 1][0] += s  # Ajoute 's' à la valeur maximale pour l'élément d'indice c-1

            # Si le drapeau 'k' vaut 1, alors c'est aussi une contrainte pour le minimum
            if k == 1:
                MINlist[c - 1][0] += s  # Ajoute également 's' à la valeur minimale de l'élément d'indice c-1

        # Trie les MINlist croissante (par défaut sur le 1er élément [0])
        MINlist.sort()
        # Trie les MAXlist décroissante, car on veut comparer les plus grands scores d'abord
        MAXlist.sort(reverse=True)

        # Récupération des deux premiers éléments (avec leurs indices) de chaque liste :
        # MINlist : les plus petits totaux de contributions (candidats au minimum)
        MinVal1, MinId1 = MINlist[0]  # Plus petit total et son indice
        MinVal2, MinId2 = MINlist[1]  # Deuxième plus petit total et son indice

        # MAXlist : les plus grands totaux de contributions (candidats au maximum)
        MaxVal1, MaxId1 = MAXlist[0]  # Plus grand total et son indice
        MaxVal2, MaxId2 = MAXlist[1]  # Deuxième plus grand total et son indice

        # Si l'indice du max et du min principal sont différents,
        # on peut tous deux améliorer le score optimal
        if MinId1 != MaxId1:
            # Le score maximum réalisable est la différence entre le max et le min les plus extrêmes + 1
            print(MaxVal1 - MinVal1 + 1)
        else:
            # Si l'indice du max et du min sont identiques, il faut regarder les deuxièmes meilleurs
            # On prend le meilleur résultat obtenu en changeant soit le min, soit le max
            print(max(MaxVal2 - MinVal1, MaxVal1 - MinVal2) + 1)