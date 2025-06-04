#!usr/bin/env python3

# Importation de modules standards de la bibliothèque Python
from collections import defaultdict, deque  # defaultdict : dictionnaire avec valeur par défaut, deque : file doublement chaînée (file d'attente/défilement efficace)
from heapq import heappush, heappop         # Fonctions pour manipuler des tas (heap) min (pour files de priorité)
import sys                                  # Module pour interagir avec l'interpréteur Python (utilisé ici pour lire les entrées standard)
import math                                 # Module fournissant des fonctions mathématiques de base
import bisect                               # Module pour rechercher/injecter efficacement dans des listes triées
import random                               # Module pour générer des nombres aléatoires

# Fonction pour lire une ligne de l'entrée standard et la convertir en liste d'entiers
def LI():
    # sys.stdin.readline() lit une ligne de l'entrée standard sous forme de chaîne avec éventuellement un '\n' final.
    # split() divise la chaîne sur les espaces pour obtenir une liste de sous-chaînes (morceaux séparés par des blancs)
    # La liste par compréhension [int(x) for x in ...] convertit chaque morceau en entier
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction pour lire un seul entier depuis une ligne de l'entrée standard
def I():
    # Récupération d'une ligne et conversion en int (suppose que la ligne n'a qu'un nombre)
    return int(sys.stdin.readline())

# Fonction pour lire une ligne de l'entrée standard et retourner une liste de listes de caractères
def LS():
    # sys.stdin.readline().split() sépare la ligne en mots, puis on transforme chaque mot en liste de caractères
    # Ceci donne une liste dont chaque élément est une liste de caractères du mot correspondant
    return [list(x) for x in sys.stdin.readline().split()]

# Fonction pour lire une ligne en tant que liste de caractères
def S():
    # Convertit la chaîne obtenue en liste de caractères individuels
    # Enlève le caractère '\n' final si présent (sinon toute la liste est renvoyée telle quelle)
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

# Fonction pour lire n entiers, un par ligne, et les retourner sous forme de liste
def IR(n):
    # Utilise une compréhension de liste sur n itérations, appelant I() à chaque fois
    return [I() for i in range(n)]

# Fonction pour lire n lignes, chaque ligne représentant une liste d'entiers
def LIR(n):
    # Utilise une compréhension de liste sur n itérations, appelant LI() à chaque fois
    return [LI() for i in range(n)]

# Fonction pour lire n lignes, chaque ligne étant transformée en liste de caractères
def SR(n):
    # Utilise une compréhension de liste sur n itérations, appelant S() à chaque fois
    return [S() for i in range(n)]

# Fonction pour lire n lignes, chaque ligne découpée en "mots" transformés en listes de caractères
def LSR(n):
    # Utilise une compréhension de liste sur n itérations, appelant LS() à chaque fois
    return [LS() for i in range(n)]

# Configuration de la limite de récursion Python à un million pour permettre des appels récursifs profonds
sys.setrecursionlimit(1000000)

# Définition d'une constante souvent utilisée pour le modulo dans les problèmes d'arithmétique
mod = 1000000007

# Fonction pour le problème A (pas exécutée ici)
def A():
    n = I()  # Lecture du nombre d'éléments
    a = LI()  # Lecture de la liste d'entiers
    # On calcule le nombre d'éléments impairs dans la liste a.
    s = sum([i % 2 for i in a])  # i % 2 vaut 1 si i est impair, 0 sinon
    # Si tous les nombres sont pairs (s == 0) ou tous impairs (s == n), réponse = 0
    # Sinon, on calcule n-2+(s%2) (c'est probablement lié à la parité et la transformation des éléments)
    if s in (0, n):
        print(0)
    else:
        print(n - 2 + (s % 2))
    return

# Fonction pour le problème B qui va être exécutée à la fin du script
def B():
    # Lecture de la ligne d'entrée comportant n, Q, L, R
    # n : taille du tableau 'a'
    # Q : nombre de requêtes
    # L et R : bornes pour le filtrage
    n, Q, L, R = LI()
    # Lecture d'une liste d'entiers de longueur n
    a = LI()
    # Tri croissant de la liste 'a'
    a.sort()
    # Lecture des Q requêtes (chaque requête est une liste d'entiers)
    query = LIR(Q)
    # On initialise deux bornes pour une recherche dichotomique (binaire) sur les indices de la liste triée
    l = -1           # Borne gauche (initialement -1, c.à.d. "avant le début" de la liste)
    r = n            # Borne droite (initialement après la fin de la liste)

    # Première recherche binaire pour trouver la limite gauche telle que après transformation, a[m] >= L
    while r - l > 1:          # Boucle tant que l'intervalle n'est pas réduit à un unique élément
        m = (l + r) >> 1      # Milieu de l'intervalle actuel (division entière par 2 via décalage binaire)
        am = a[m]             # On prend la valeur à l'indice médian de la version triée de 'a'
        # On applique chaque requête de la liste 'query' en séquence à 'am'
        for q, x, s, t in query:
            if q == 1:
                # Si q==1, on applique am += s puis am *= t mais seulement si am >= x
                if am < x:
                    continue  # On passe à la requête suivante si la condition n'est pas satisfaite
                am += s
                am *= t
            else:
                # Si q==2, on applique am -= s puis division entière par t, mais seulement si am <= x
                if am > x:
                    continue  # On passe à la requête suivante si la condition n'est pas satisfaite
                am -= s
                # Gestion de la division entière : si am est négatif, division arrondie vers le haut
                if am < 0:
                    am = -((-am) // t)
                else:
                    am //= t
        # Après avoir appliqué toutes les requêtes en séquence, on vérifie si la valeur finale est < L
        if am < L:
            l = m            # Recherche à droite si la valeur finale est trop petite
        else:
            r = m            # Recherche à gauche sinon
    left = r                 # left contiendra le premier indice où am >= L

    # On recommence un dichotomie pour la borne supérieure (pour <= R)
    l = 0       # Nouvelle borne gauche
    r = n       # Nouvelle borne droite
    while r - l > 1:
        m = (l + r) >> 1
        am = a[m]
        # Même suite de transformation sur 'am' que précédemment
        for q, x, s, t in query:
            if q == 1:
                if am < x:
                    continue
                am += s
                am *= t
            else:
                if am > x:
                    continue
                am -= s
                if am < 0:
                    am = -((-am) // t)
                else:
                    am //= t
        # Après les requêtes, on vérifie si la valeur obtenue est <= R
        if am <= R:
            l = m      # Recherche à droite si am est dans la plage ou trop petit
        else:
            r = m      # Recherche à gauche sinon
    # Le nombre d'éléments transformés tombant dans [L,R] est r - left
    print(r - left)
    return

# Fonctions vides pour les autres problèmes, le code principal n'appelle que B
def C():
    n = I()
    return

def D():
    n = I()
    return

def E():
    n = I()
    return

def F():
    n = I()
    return

def G():
    n = I()
    return

def H():
    n = I()
    return

def I_():
    n = I()
    return

def J():
    n = I()
    return

# Bloc principal : ce code ne sera exécuté que si ce script est lancé comme programme principal
if __name__ == "__main__":
    # Appel de la fonction B (c'est-à-dire résolution du problème B avec tous les commentaires ci-dessus)
    B()