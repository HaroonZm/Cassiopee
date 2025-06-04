#!usr/bin/env python3

# Importation des modules nécessaires

# 'defaultdict' permet de créer un dictionnaire avec une valeur par défaut pour les clés inexistantes.
# 'deque' est une file doublement terminée pour des ajouts et retraits efficaces par les deux bouts.
from collections import defaultdict, deque

# 'heappush' et 'heappop' servent à manipuler des files de priorité (heap/priority queue).
from heapq import heappush, heappop

# 'sys' donne accès à certaines fonctions du système comme la lecture des entrées standard.
import sys

# 'math' donne accès à des fonctions mathématiques comme sqrt, factorial, etc.
import math

# 'bisect' permet de rechercher ou d’insérer dans des listes triées rapidement.
import bisect

# 'random' permet de générer des nombres pseudo-aléatoires.
import random

# Définition de fonctions d’utilité pour faciliter la lecture des entrées

def LI():
    # Lit une ligne de l'entrée standard, coupe en morceaux par espaces et convertit chaque morceau en entier.
    # Retourne une liste d'entiers.
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    # Lit une ligne de l'entrée standard, supprime le retour à la ligne, et convertit le texte obtenu en entier.
    # Retourne cet entier.
    return int(sys.stdin.readline())

def LS():
    # Lit une ligne de l'entrée standard, la divise par espaces et convertit chaque élément (string) en liste de caractères.
    # Retourne une liste de listes de caractères.
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    # Lit une ligne de l’entrée standard et la transforme en liste de caractères.
    res = list(sys.stdin.readline())
    # Vérifie si le dernier caractère est un retour à la ligne '\n'.
    if res[-1] == "\n":
        # Si oui, retourne la liste sans ce dernier caractère.
        return res[:-1]
    # Sinon retourne la liste dans son intégralité.
    return res

def IR(n):
    # Pour 'n' lignes, lit un entier par ligne et retourne la liste des entiers lus.
    return [I() for i in range(n)]

def LIR(n):
    # Pour 'n' lignes, lit chaque fois une liste d'entiers et retourne une liste de ces listes.
    return [LI() for i in range(n)]

def SR(n):
    # Pour 'n' lignes, lit chaque fois une liste de caractères (ligne) et retourne une liste de ces listes.
    return [S() for i in range(n)]

def LSR(n):
    # Pour 'n' lignes, lit chaque fois une ligne, la découpe par mots et transforme chaque mot en liste de caractères.
    # Retourne une liste de ces listes de listes.
    return [LS() for i in range(n)]

# Définit la profondeur maximale de récursion autorisée par Python à 1 000 000.
# C'est utile dans les problèmes d'arbre/profondeur profonde pour éviter une erreur de récursion maximale atteinte.
sys.setrecursionlimit(1000000)

# Définition d'une constante. 'mod' est utilisé pour effectuer des opérations modulo (souvent dans les problèmes de combinatoire)
mod = 1000000007

def solve():
    # Fonction principale qui résout le problème.
    
    # Sous-fonction permettant d'ajouter 1 à toutes les cases du tableau 'bit' qui couvrent l'index i dans le Fenwick Tree.
    def add(i):
        # 'i' est la position dans le BIT/Fenwick Tree à incrémenter.
        # Tant que 'i' est inférieur ou égal à la taille totale 'n'
        while i <= n:
            # Incrémente la valeur à la position 'i' du tableau 'bit' de 1
            bit[i] += 1
            # Isole le bit de poids faible de 'i' et l'ajoute à 'i' pour aller à l'indice parent.
            i += i & -i

    # Sous-fonction permettant de calculer la somme des valeurs dans le BIT jusqu'à l'indice i inclus.
    def sum(i):
        # Initialise la variable de résultat à 0
        res = 0
        # Tant que 'i' est strictement positif
        while i > 0:
            # Ajoute la valeur à la position 'i' du tableau 'bit' à 'res'
            res += bit[i]
            # Isole le bit de poids faible de 'i' et le soustrait de 'i' pour remonter l'arbre.
            i -= i & -i
        # Retourne la somme totale.
        return res

    # Lit deux entiers 'n' et 'k' depuis l'entrée (par exemple: "5 2")
    n, k = LI()
    # Lit une liste de 'n' entiers (par exemple: "2 3 5 4 1")
    p = LI()
    
    # Premier cas : si le nombre d'éléments 'n' est strictement supérieur à 'k'
    if n > k:
        # Si 'k' est pair (le reste de la division par 2 est 0)
        if k % 2 == 0:
            print("Yes") # Affiche "Yes"
        else:
            # 'a' est une variable qui sert à accumuler le résultat d'un XOR sur des bits.
            a = 0
            # On crée un tableau 'bit' d'entiers à n+1 cases (indices 0 à n), initialisé à 0.
            bit = [0] * (n + 1)
            # Boucle sur tous les indices de 0 à n-1
            for i in range(n):
                # Calcule (i - sum(p[i])) & 1 :
                # - 'sum(p[i])' donne le nombre d'éléments < p[i] déjà rencontrés
                # - Le résultat donne la parité (pair/impair) de la différence
                # - Le XOR ^ ajoute à 'a' cette parité au bit de poids faible
                a ^= (i - sum(p[i])) & 1
                # On met à jour le Fenwick Tree en ajoutant 1 à la case p[i]
                add(p[i])
            # Si 'a' est non nul (pas un multiple de 2), c'est "No"
            if a:
                print("No")
            # Sinon, c'est "Yes"
            else:
                print("Yes")
        # On quitte la fonction une fois la réponse trouvée pour ce cas.
        return

    else:
        # Sinon, c'est le cas où n <= k
        # Cherche l'indice 'i' du premier élément de p qui vaut 1 (on cherche la position de '1' dans la liste)
        for i in range(n):
            if p[i] == 1:
                break
        # On vérifie ensuite si la liste p, en commençant à cette position 'i', forme un cycle ordonné croissant
        for j in range(n):
            # On regarde la valeur à la position (j + i) % n de la liste p, et la compare à (j + 1)
            if p[(j + i) % n] != j + 1:
                # Si l'un des éléments ne correspond pas à la suite attendue, on affiche "No" et on sort.
                print("No")
                return
        # Si la vérification passe pour toutes les positions, on affiche "Yes"
        print("Yes")
    return

# Ce bloc permet de lancer la fonction 'solve' seulement si ce fichier est exécuté directement
# et non importé comme un module dans un autre script.
if __name__ == "__main__":
    solve()