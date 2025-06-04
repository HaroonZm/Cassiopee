#!/usr/bin/env python3

# Importation du module 'collections' pour utiliser le dictionnaire avec valeur par défaut (defaultdict)
from collections import defaultdict

# Importation du module 'collections' pour utiliser la file double (deque), non utilisée ici mais incluse pour référence
from collections import deque

# Importation des fonctions 'heappush' et 'heappop' du module 'heapq' pour manipuler des files de priorité (min-heap)
from heapq import heappush, heappop

# Importation du module 'sys' pour manipuler l'entrée et la sortie standard et autres utilitaires système
import sys

# Importation du module 'math' pour accéder à des fonctions mathématiques
import math

# Importation du module 'bisect' pour accéder à la recherche dichotomique dans des listes triées
import bisect

# Importation du module 'random' pour générer des nombres pseudo-aléatoires
import random

# Définition d'une fonction LI qui lit une ligne standard de l'entrée, la sépare par les espaces, applique int dessus,
# puis en fait une liste
def LI():
    # sys.stdin.readline() lit une ligne (string) de l'entrée standard ; split() découpe la string en morceaux selon les espaces,
    # map(int, ...) convertit chaque morceau en entier, list(...) crée une liste des entiers.
    return list(map(int, sys.stdin.readline().split()))

# Définition d'une fonction I qui lit une ligne, supprime la fin de ligne, et convertit toute la ligne en entier
def I():
    return int(sys.stdin.readline())

# Définition d'une fonction LS qui lit une ligne, la découpe et retourne une liste de listes de caractères
def LS():
    # sys.stdin.readline() lit une ligne, split() coupe par espace, puis map(list, ...) transforme chaque morceau en liste de caractères
    return list(map(list, sys.stdin.readline().split()))

# Définition d'une fonction S qui lit une ligne comme une liste de caractères et enlève le dernier caractère (habituellement '\n')
def S():
    # list(...) crée une liste de chaque caractère de la string lue ; [:-1] enlève le dernier caractère
    return list(sys.stdin.readline())[:-1]

# Définition de IR qui lit n lignes de nombres entiers (une par ligne)
def IR(n):
    l = [None for i in range(n)]  # Création d'une liste de n éléments à None pour réserver l'espace
    for i in range(n):
        l[i] = I()  # Remplace chaque élément par un entier lu depuis entrée
    return l  # Retourne la liste d'entiers

# Définition de LIR qui lit n listes d'entiers (format 'n' lignes à multi-entiers par ligne)
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()  # Remplace chaque ligne par la liste d'entiers lue
    return l

# Définition de SR qui lit n chaînes en mode liste de caractères (une chaîne par ligne lue)
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

# Définition de LSR qui lit n lignes et retourne la liste de listes de listes de caractères par ligne
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Définition de la limite maximale de récursion pour éviter RecursionError lors d'appels récursifs profonds
sys.setrecursionlimit(1000000)

# Définition d'une constante pour le modulo à utiliser dans certains calculs (souvent utile dans les compétitions pour gérer de gros entiers)
mod = 1000000007

# ------------------------------------------------------
# Solution pour le problème C, encapsulée dans une fonction
def C():
    # Définition d'une fonction interne pour calculer le PGCD (Plus Grand Commun Diviseur) de deux entiers
    def gcd(a, b):
        # Si le premier nombre est égal à 0, le PGCD est le second nombre.
        if a == 0:
            return b
        # Sinon, appel récursif du PGCD, en utilisant modulo pour réduire le second nombre.
        return gcd(b % a, a)

    # Lecture d'une ligne utilisateur depuis l'entrée, en attente d'une chaîne représentant un nombre rationnel (éventuellement périodique)
    s = input()
    # Calcul de la longueur de la chaîne saisie
    n = len(s)

    # On vérifie si le nombre contient une partie périodique (détectée par la présence du caractère '(' )
    if s.count("(") == 0:
        # Aucun périodique ; conversion directe en float
        s = float(s)
        # Calcul de la puissance de 10 correspondante au nombre de chiffres après la virgule
        b = 10 ** (n - 2)
        # Multiplie le nombre lu par cette puissance puis arrondit pour avoir un entier au numérateur
        a = round(s * b)
        # Calcul du PGCD de a et b, permet de réduire la fraction ensuite
        g = gcd(a, b)
        # Réduction du numérateur
        a //= g
        # Réduction du dénominateur
        b //= g
    else:
        # Il y a une partie périodique
        n = s.find("(")  # Trouve l'index du début de la parenthèse ouvrante
        t = float(s[:n])  # Transforme la partie non périodique avant le ( en float
        b = 10 ** (n - 2)  # Calcul de la puissance de 10 correspondant au nombre de chiffres après la virgule AVANT le (
        a = round(t * b)  # Numérateur correspondant à la partie non périodique
        g = gcd(a, b)  # Calcul du PGCD pour réduire
        a //= g
        b //= g
        # Calcul du nombre de chiffres entre le point '.' et le '(' (longueur de la partie décimale non périodique)
        l = (s.find("(") - s.find(".") - 1)
        # Extraction de la partie périodique sous forme de chaîne
        s = s[n+1:-1]  # Prend les caractères après le '(' jusqu'au ')'
        m = len(s)  # La longueur de la partie périodique
        c = round(float(s))  # La partie périodique convertie en entier
        d = (10 ** m - 1) * 10 ** l  # Calcul du dénominateur pour la partie périodique : facteur pour faire apparaître le motif périodique uniquement
        g = gcd(c, d)  # Réduction fraction périodique
        c //= g
        d //= g
        # Modification du numérateur et du dénominateur pour additionner la partie non périodique à la périodique
        a = a * d + b * c
        b = b * d
        # Dernière simplification de la fraction obtenue
        g = gcd(a, b)
        a //= g
        b //= g
    # Construction de la chaîne représentant la fraction finale sous forme 'a/b'
    print(str(a) + "/" + str(b))
    return  # Fin de la fonction

# ------------------------------------------------------
# Si ce script est lancé comme le programme principal (et non importé comme module)
if __name__ == "__main__":
    # Exécution de la fonction C (problème C)
    C()