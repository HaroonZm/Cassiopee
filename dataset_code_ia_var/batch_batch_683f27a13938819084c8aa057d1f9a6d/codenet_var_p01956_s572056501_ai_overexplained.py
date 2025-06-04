#!usr/bin/env python3

# Importation du module 'defaultdict' depuis 'collections'.
# Cela permet de créer des dictionnaires avec des valeurs par défaut.
from collections import defaultdict

# Importation du module 'deque' depuis 'collections'.
# 'deque' est une liste optimisée pour ajouter/supprimer des éléments aux extrémités.
from collections import deque

# Importation des fonctions 'heappush' et 'heappop' depuis le module 'heapq'.
# Ces fonctions permettent de manipuler des files de priorité (heap).
from heapq import heappush, heappop

# Importation du module 'sys'.
# Ce module donne accès à des fonctionnalités liées au système d'exécution, comme la lecture des entrées standard.
import sys

# Importation du module 'math'.
# Ce module fournit des fonctions mathématiques standard comme sqrt, ceil, etc.
import math

# Importation du module 'bisect'.
# Ce module contient des fonctions pour la recherche dichotomique sur des listes triées.
import bisect

# Importation du module 'random'.
# Ce module contient des fonctions pour générer des nombres aléatoires.
import random

# Définition d'une fonction LI()
# Cette fonction lit une ligne de l'entrée standard, la découpe en nombres entiers et retourne la liste de ceux-ci.
def LI():
    # sys.stdin.readline() lit une ligne depuis l'entrée standard.
    # split() découpe la ligne en une liste de chaînes selon les espaces.
    # map(int, ...) convertit chaque chaîne en entier.
    # list(...) transforme le résultat en liste.
    return list(map(int, sys.stdin.readline().split()))

# Définition d'une fonction I()
# Cette fonction lit une ligne de l'entrée standard et la convertit en nombre entier.
def I():
    # sys.stdin.readline() lit une ligne complète; int(...) convertit la chaîne en entier.
    return int(sys.stdin.readline())

# Définition d'une fonction LS()
# Cette fonction lit une ligne, la découpe en morceaux et retourne une liste de listes, chaque sous-liste comportant un caractère.
def LS():
    # map(list, ...) convertit chaque mot en une liste de caractères.
    # sys.stdin.readline().split() découpe selon les espaces.
    # list(...) emballe le tout dans une liste.
    return list(map(list, sys.stdin.readline().split()))

# Définition d'une fonction S()
# Cette fonction lit une ligne de l'entrée standard et retourne la liste de ses caractères, sans le dernier caractère (habituellement le saut de ligne '\n').
def S():
    # sys.stdin.readline() lit toute la ligne y compris '\n'
    # list(...) transforme la chaîne en liste de caractères
    # [:-1] enlève le dernier caractère (saut de ligne)
    return list(sys.stdin.readline())[:-1]

# Définition d'une fonction IR(n)
# Permet de lire 'n' entiers consécutivement, un par ligne.
def IR(n):
    # Création d'une liste de taille n, initialisée avec None
    l = [None for i in range(n)]
    # Boucle pour lire et stocker chaque entier
    for i in range(n):
        l[i] = I()
    return l

# Définition d'une fonction LIR(n)
# Permet de lire 'n' lignes, chaque ligne étant convertie en une liste d'entiers.
def LIR(n):
    # Création d'une liste de taille n, initialisée avec None
    l = [None for i in range(n)]
    # Boucle pour lire chaque ligne et la convertir
    for i in range(n):
        l[i] = LI()
    return l

# Définition d'une fonction SR(n)
# Lit 'n' lignes, chaque ligne étant convertie en liste de caractères, sans le saut de ligne.
def SR(n):
    # Création d'une liste de taille n, initialisée avec None
    l = [None for i in range(n)]
    # Boucle pour lire chaque ligne et la convertir
    for i in range(n):
        l[i] = S()
    return l

# Définition d'une fonction LSR(n)
# Lit 'n' lignes, chaque ligne étant découpée en mots puis chaque mot en liste de caractères.
def LSR(n):
    # Création d'une liste de taille n, initialisée avec None
    l = [None for i in range(n)]
    # Boucle pour lire chaque ligne, puis conversion
    for i in range(n):
        l[i] = LS()
    return l

# Permet d'augmenter la limite de récursion (profondeur d'appels de fonctions récursives)
# La valeur 1000000 permet d'éviter des erreurs en cas de récursion profonde.
sys.setrecursionlimit(1000000)

# Déclaration de la variable 'mod', contenant la valeur du modulo souvent utilisée dans les calculs mathématiques pour éviter les dépassements d'entier.
mod = 1000000007

# 
# Définition de la fonction A
# Cette fonction lit des valeurs depuis l'entrée standard et effectue un traitement pour calculer la valeur attendue selon une logique spécifique.
def A():
    # Lecture de trois entiers depuis l'entrée standard et affectation aux variables n, h et w
    # n : nombre de colonnes ou étapes (selon le contexte du problème)
    # h : une hauteur
    # w : une largeur
    n, h, w = LI()
    # Lecture de n entiers, à stocker dans la liste x
    x = LI()
    # Création de la liste t, initialisée à 0, de taille (w*n+1)
    # Cette liste servira à gérer des incréments/décréments selon une technique de différence de tableaux.
    t = [0 for i in range(w*n+1)]
    # Pour chaque index i de 0 à n-1 (inclus)
    for i in range(n):
        # Test si i est pair (i%2 == 0)
        if not i % 2:
            # Si i est pair :
            # On incrémente t à la position (i*w + x[i]) de 1
            t[i*w + x[i]] += 1
            # On décrémente t à la position ((i+1)*w + x[i]) de 1
            t[(i+1)*w + x[i]] -= 1
        else:
            # Si i est impair :
            # On incrémente t à la position (i*w - x[i]) de 1
            t[i*w - x[i]] += 1
            # On décrémente t à la position ((i+1)*w - x[i]) de 1
            t[(i+1)*w - x[i]] -= 1
    # Parcours de la liste t depuis l'indice 0 jusqu'à w*n-1
    # Cette étape calcule les valeurs cumulées dans t
    for i in range(w*n):
        # Ajoute la valeur précédente à la suivante (ajout cumulatif)
        t[i+1] += t[i]
    # Initialisation de la variable 'ans' à 0. Cette variable va contenir le résultat final.
    ans = 0
    # Parcours de tous les éléments de t sauf le dernier
    for i in t[:-1]:
        # Si la valeur de i est 0
        if i == 0:
            # Ajoute la valeur de h à la variable ans
            ans += h
    # Affiche la valeur finale de ans sur la sortie standard.
    print(ans)
    # Retourne None explicitement (même si ce n'est pas nécessaire en Python)
    return

# Définition de la fonction B, laissée volontairement vide
def B():
    return

# Définition de la fonction C, laissée vide
def C():
    return

# Définition de la fonction D, laissée vide
def D():
    return

# Définition de la fonction E, laissée vide
def E():
    return

# Définition de la fonction F, laissée vide
def F():
    return

# Définition de la fonction G, laissée vide
def G():
    return

# Définition de la fonction H, laissée vide
def H():
    return

# Définition de la fonction I_, laissée vide
def I_():
    return

# Définition de la fonction J, laissée vide
def J():
    return

# Bloc conditionnel permettant d'exécuter le code qui suit SEULEMENT
# si ce fichier est exécuté directement (et non importé comme un module)
if __name__ == "__main__":
    # Appel de la fonction A pour lancer sa logique principale.
    A()