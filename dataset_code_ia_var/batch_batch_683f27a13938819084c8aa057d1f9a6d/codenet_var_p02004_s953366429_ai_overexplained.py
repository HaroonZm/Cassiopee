#!/usr/bin/env python3

# Importation de modules nécessaires pour différentes structures et opérations

# defaultdict permet de créer des dictionnaires avec des valeurs par défaut
from collections import defaultdict
# deque est une collection optimisée pour ajouter ou supprimer des éléments des deux côtés
from collections import deque
# heappush et heappop permettent de gérer une file de priorité min-heap
from heapq import heappush, heappop
# sys module permet d'interagir avec l'interpréteur Python (ici, entrée standard etc.)
import sys
# math contient des fonctions mathématiques basiques
import math
# bisect permet d'utiliser des fonctions pour manipuler efficacement des listes triées
import bisect
# random permet de générer des nombres aléatoires ou faire des choix aléatoires
import random

# Définition de fonctions utilitaires pour lire différents types et formats de données depuis l'entrée standard

def LI():
    # Lit une ligne de l'entrée standard, la découpe par espaces, convertit chaque élément en entier, et renvoie la liste résultante
    return list(map(int, sys.stdin.readline().split()))

def I():
    # Lit une ligne de l'entrée standard et la convertit en entier
    return int(sys.stdin.readline())

def LS():
    # Lit une ligne de l'entrée standard, sépare par espaces, transforme chaque chaîne en liste de caractères et renvoie la liste de ces listes
    return list(map(list, sys.stdin.readline().split()))

def S():
    # Lit une ligne de l'entrée standard, la transforme en liste de caractères, puis retire le dernier caractère (saut de ligne)
    return list(sys.stdin.readline())[:-1]

def IR(n):
    # Initialise une liste de longueur n contenant None
    l = [None for i in range(n)]
    # Pour chaque valeur de 0 à n-1, lit un entier depuis l'entrée standard et le stocke à l'index correspondant
    for i in range(n):
        l[i] = I()
    # Renvoie la liste d'entiers
    return l

def LIR(n):
    # Semblable à IR, mais chaque élément est une liste d'entiers obtenue en lisant une ligne d'entiers depuis l'entrée
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    # Crée une liste de n éléments chacun obtenu en lisant une ligne et la découpant en caractères (sauf le \n final)
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    # Crée une liste de n éléments, chacun étant une liste de chaînes (chaque ligne lue de l’entrée, séparée par espaces, puis transformée en liste de caractères)
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Change la limite maximale de récursivité afin d'éviter une RecursionError dans le cas d'appels récursifs profonds
sys.setrecursionlimit(1000000)

# Définition d'une constante pour le module d'opérations, généralement utilisée pour éviter les débordements lors des grands nombres (typiquement utilisé dans les problèmes compétitifs)
mod = 1000000007


#Fonction correspondant au problème A
def A():
    # Lit une ligne de l'entrée, la convertit en liste de caractères SANS le saut de ligne
    s = S()
    # Variable pour représenter une sorte de direction/modulo (peut-être une position ou un état cyclique parmi 4)
    d = 0
    # Variable compteur qui stockera la réponse finale à afficher
    ans = 0
    # Variable indicateur booléen (0 ou 1) servant de signal au sein de la logique
    k = 0
    # Parcourt chaque caractère de la liste s (chaque caractère de la chaîne d'entrée)
    for i in s:
        # Si le caractère actuel est "R"
        if i == "R":
            # Si d vaut 0 (état de départ/initial), alors k devient 1 (pour indiquer une condition spéciale)
            if d == 0:
                k = 1
            # On incrémente d de 1 pour indiquer un changement d'état/position
            d += 1
            # Applique le modulo 4 pour que d reste dans la plage [0,3] (c'est-à-dire cyclique)
            d %= 4
            # Si après ce changement d'état, on revient à 0 ET que k est positif, on incrémente la réponse (signe qu'on a complété un tour)
            if d == 0 and k:
                ans += 1
        # Sinon si on lit un caractère autre que "R" (supposé ici être "L" ou autre)
        else:
            # Si d est 0, on met k à 0
            if d == 0:
                k = 0
            # On décrémente d de 1 (changement dans l'autre sens probablement)
            d -= 1
            # Application du modulo 4 pour rester dans la plage cyclique [0,3]
            d %= 4
    # Affiche la réponse à la fin, après avoir parcouru toute la chaîne
    print(ans)
    return

#Fonction B (Vide - aucun traitement ou commentaire à faire ici)
def B():
    return

#Fonction C (Vide - aucun traitement ou commentaire à faire ici)
def C():
    return

#Fonction D (Vide - aucun traitement ou commentaire à faire ici)
def D():
    return

#Fonction E (Vide - aucun traitement ou commentaire à faire ici)
def E():
    return

#Fonction F (Vide - aucun traitement ou commentaire à faire ici)
def F():
    return

#Fonction G (Vide - aucun traitement ou commentaire à faire ici)
def G():
    return

#Fonction H (Vide - aucun traitement ou commentaire à faire ici)
def H():
    return

#Fonction I_ (Vide - aucun traitement ou commentaire à faire ici)
def I_():
    return

#Fonction J (Vide - aucun traitement ou commentaire à faire ici)
def J():
    return

# Point d'entrée principal du programme
# Le bloc __name__ == "__main__" permet de s'assurer que le code contenu ici ne sera exécuté que si ce fichier est lancé en tant que programme principal et non importé comme module dans un autre script
if __name__ == "__main__":
    # Appelle la fonction A définie plus haut
    A()