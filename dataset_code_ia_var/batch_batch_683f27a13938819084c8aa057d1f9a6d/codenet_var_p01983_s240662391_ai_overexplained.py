#!/usr/bin/env python3

# Importation du module collections et importation de defaultdict
# defaultdict agit comme un dictionnaire Python standard mais avec une valeur par défaut pour les clés manquantes
from collections import defaultdict

# Importation de deque depuis le module collections
# deque permet de créer une liste doublement chaînée, efficace pour les opérations en début/fin
from collections import deque

# On importe deux fonctions du module heapq : heappush et heappop
# Elles servent à manipuler facilement les files de priorité (min-heaps)
from heapq import heappush, heappop

# Importation du module sys, qui donne accès aux objets utilisés/interprétés par l'interpréteur Python
import sys

# importation du module math, qui inclut des fonctions mathématiques standards comme sqrt, ceil, floor, etc.
import math

# On importe le module bisect, qui fournit des fonctions permettant de manipuler des listes triées par bissection
import bisect

# Importation du module random, pour générer des nombres ou choisir des éléments aléatoirement
import random

# Définition d’une fonction LI() : renvoie une liste d’entiers lus depuis une ligne de l’entrée standard
def LI():
    # sys.stdin.readline() lit une ligne de l'entrée standard, qui est ensuite découpée (split())
    # chaque morceau est converti en int avec map, et la map est convertie en liste
    return list(map(int, sys.stdin.readline().split()))

# Définition d'une fonction I() : lit une ligne de l'entrée standard et la convertit en int
def I():
    # sys.stdin.readline() lit une ligne, et int(...) convertit cette chaîne en entier
    return int(sys.stdin.readline())

# Définition d'une fonction LS() : lit une ligne et retourne une liste de listes de caractères
def LS():
    # On lit une ligne, on la coupe par les espaces, et chaque élément est converti en liste (donc chaque mot est transformé en liste de lettres)
    return list(map(list, sys.stdin.readline().split()))

# Définition d'une fonction S() : lit une ligne et retourne une liste de ses caractères sauf le dernier (en général '\n')
def S():
    # On lit une ligne puis on la transforme en liste de caractères, et on enlève le dernier caractère
    return list(sys.stdin.readline())[:-1]

# Définition d'une fonction IR(n) : retourne une liste de n entiers, chaque entier est lu sur une nouvelle ligne
def IR(n):
    # On crée une liste de longueur n, initialisée avec None
    l = [None for i in range(n)]
    # Pour chaque indice dans cette liste, on lit un entier à insérer
    for i in range(n):
        l[i] = I()
    return l

# Définition d'une fonction LIR(n) : retourne une liste de n listes, chaque liste contient des entiers lus sur une ligne
def LIR(n):
    # On crée une liste de longueur n, initialisée avec None
    l = [None for i in range(n)]
    # Pour chaque case, on remplit avec la liste d'entiers lue
    for i in range(n):
        l[i] = LI()
    return l

# Définition d'une fonction SR(n) : retourne une liste de n listes, chaque liste est obtenue en lisant une ligne puis en enlevant le caractère de retour à la ligne
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

# Définition d'une fonction LSR(n) : retourne une liste de n listes de listes de caractères
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Définition de la profondeur maximale de la pile d'appels récursifs à 1.000.000.
# Cela permet d'éviter les erreurs de récursion trop profonde dans certains algorithmes
sys.setrecursionlimit(1000000)

# Définition d'une constante mod, utilisée généralement comme modulo pour éviter les grands nombres dans des problèmes de programmation compétitive
mod = 1000000007

# Fonction principale associée à l’énoncé "A"
def A():
    # Définition d'une fonction interne permettant de parser une expression/hash
    # Elle prend en arguments s (la chaîne à traiter) et i (l’indice courant)
    def parse_hash(s, i):
        # Si le caractère courant est "[", alors on a une opération à traiter
        if s[i] == "[":
            # On avance d'un caractère après "["
            i += 1
            # On lit l'opération (op) à effectuer, en avançant l'indice
            op, i = parse_op(s, i)
            # On lit le premier opérande (h1), en avançant l'indice
            h1, i = parse_hash(s, i)
            # On lit le second opérande (h2), en avançant l'indice
            h2, i = parse_hash(s, i)
            # On saute le caractère "]"
            i += 1
            # On applique l'opération op à h1 et h2 puis on retourne le résultat et la nouvelle position dans la chaîne
            return calc(op, h1, h2), i
        else:
            # Sinon, il s'agit d'une feuille, donc c'est une lettre/valeur à analyser
            return parse_letter(s, i)

    # Fonction interne qui lit un opérateur op à l'indice i dans la chaîne s
    # Elle retourne l'opérateur et l'indice suivant
    def parse_op(s, i):
        return s[i], i + 1

    # Fonction interne qui lit une lettre ou valeur à l’indice i dans la chaîne s
    # Retourne la valeur (ici une lettre ou une variable devenue un nombre) et l'indice suivant
    def parse_letter(s, i):
        return s[i], i + 1

    # Fonction qui exécute l’opération op entre les deux valeurs h1 et h2
    # Les opérations définies sont :
    # "+" : bitwise OR (|), "*" : bitwise AND (&), "^" : bitwise XOR (^)
    def calc(op, h1, h2):
        if op == "+":
            # op == "+" : opération OU binaire entre h1 et h2
            return h1 | h2
        elif op == "*":
            # op == "*" : opération ET binaire entre h1 et h2
            return h1 & h2
        else:
            # Sinon (par défaut "^") : opération XOR binaire entre h1 et h2
            return h1 ^ h2

    # Boucle principale d'exécution
    # On répète ce bloc jusqu'à interruption (break)
    while 1:
        # On lit la première expression, sous forme de liste de caractères, en supprimant le saut de ligne
        s = S()
        # Si la première lettre du mot est '.', on interrompt la boucle (cas d'arrêt)
        if s[0] == ".":
            break
        # On lit la deuxième ligne, qui contient les valeurs à associer aux variables
        t = S()
        # On utilise la longueur de s pour traiter tous les caractères
        n = len(s)
        # On copie la chaîne s, caractère par caractère, dans une liste s0
        s0 = [s[i] for i in range(n)]
        # On remplace dans cette liste chaque lettre par la valeur correspondante de t (selon a, b, c ou d)
        for i in range(n):
            if s0[i] == "a":
                # Remplacement de "a" par la valeur correspondante (premier caractère de t converti en entier)
                s0[i] = int(t[0])
            elif s0[i] == "b":
                # Remplacement de "b" par la valeur correspondante (deuxième caractère)
                s0[i] = int(t[1])
            elif s0[i] == "c":
                # Remplacement de "c" par la (troisième) valeur entière
                s0[i] = int(t[2])
            elif s0[i] == "d":
                # Remplacement de "d" par la (quatrième) valeur entière
                s0[i] = int(t[3])
        # On appelle la fonction de parsing, en démarrant à l’indice 0, et on retient le premier élément de la sortie (la valeur calculée)
        p = parse_hash(s0, 0)[0]
        # Initialisation du compteur de solutions
        ans = 0
        # On parcourt toutes les combinaisons possibles de a, b, c, d dans l’intervalle [0, 9]
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        # On recrée une copie de la liste originale s
                        s0 = [s[i] for i in range(n)]
                        # Pour chaque caractère, on remplace la variable 'a', 'b', 'c', ou 'd' par la valeur correspondante dans la boucle courante
                        for i in range(n):
                            if s0[i] == "a":
                                s0[i] = a
                            elif s0[i] == "b":
                                s0[i] = b
                            elif s0[i] == "c":
                                s0[i] = c
                            elif s0[i] == "d":
                                s0[i] = d
                        # On évalue cette version de s0 pour obtenir la valeur p0
                        p0 = parse_hash(s0, 0)[0]
                        # Si la valeur initiale (p) est égale à p0, on incrémente le compteur
                        if p == p0:
                            ans += 1
        # On affiche, pour l'expression courante, la valeur obtenue p avec les valeurs initiales et ans, le nombre de combinaisons de valeurs qui donnent ce résultat
        print(p, ans)

    # Fin de la fonction
    return

# Les fonctions suivantes sont vides, mais sont prévues pour accueillir d'autres problèmes (B à J)
def B():
    return

def C():
    return

def D():
    return

def E():
    return

def F():
    return

def G():
    return

def H():
    return

def I_():
    return

def J():
    return

# Bloc pour lancer la bonne fonction lorsque le programme est exécuté en tant que script principal
if __name__ == "__main__":
    # On exécute la fonction A() définie ci-dessus
    A()