#!/usr/bin/env python3

# Importation des modules nécessaires

# 'defaultdict' permet de créer des dictionnaires avec des valeurs par défaut automatiquement.
from collections import defaultdict

# 'deque' est une structure de données de type file doublement chaînée, utile pour des opérations de file d'attente performantes.
from collections import deque

# Importation de 'heappush' et 'heappop' qui servent à gérer des files de priorité (tas binaire).
from heapq import heappush, heappop

# Le module 'sys' donne accès à des fonctionnalités système, notamment pour lire les entrées standard.
import sys

# Le module 'math' fournit des fonctions mathématiques standards.
import math

# Le module 'bisect' permet de rechercher et d'insérer efficacement dans des listes triées.
import bisect

# Le module 'random' permet de générer des nombres aléatoires.
import random

# Définition de fonctions utilitaires pour faciliter la lecture et la conversion des entrées

# Lit une ligne de l'entrée, la découpe en morceaux séparés par des espaces, puis convertit chaque morceau en entier ; retourne une liste d'entiers.
def LI():
    return list(map(int, sys.stdin.readline().split()))

# Lit une ligne de l'entrée et la convertit en un entier.
def I():
    return int(sys.stdin.readline())

# Lit une ligne, sépare par espaces, chaque sous-élément devient une liste (pour chaque mot/entier/etc.).
def LS():
    return list(map(list, sys.stdin.readline().split()))

# Lit une ligne et la convertit en une liste de caractères, en supprimant le dernier caractère (généralement '\n').
def S():
    return list(sys.stdin.readline())[:-1]

# Lit 'n' lignes, chacune étant convertie en entier, et les stocke dans une liste ; retourne la liste d'entiers.
def IR(n):
    l = [None for i in range(n)]  # Création d'une liste de taille n, remplie de None pour initialisation.
    for i in range(n):
        l[i] = I()  # Remplace l'élément None par l'entrée entière à l'indice i.
    return l

# Lit 'n' lignes, chacune coupée/convertie en liste d'entiers, et empile dans une liste de listes.
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

# Lit 'n' lignes, chaque ligne convertie en liste de caractères, retire le '\n', et construit une liste de listes.
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

# Lit 'n' lignes, chaque ligne transformée en liste de listes de caractères, stockées dans une autre liste.
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Augmente la profondeur maximale de la récursion Python, ici à 1 000 000, utile pour la récursivité profonde (ex : arbres profonds).
sys.setrecursionlimit(1000000)

# Définition d'un modulo pour les calculs de grandes valeurs numériques pour éviter le dépassement de capacité.
mod = 1000000007

###########################################################################
# Fonction D - Analyse détaillée
###########################################################################

def D():
    # Lecture de la première entrée, attendue comme un seul entier : le nombre de paires (n).
    n = I()
    
    # Initialisation d'une liste de taille 100001 remplie de zéros, nommée 's'.
    # Cette liste peut être utilisée pour compter des événements sur un intervalle de 0 à 100000.
    s = [0 for i in range(100001)]
    
    # Lecture de n lignes, chaque ligne étant une paire (liste de deux entiers), stockées dans la liste 'l'.
    l = LIR(n)
    
    # Trie la liste 'l' en utilisant le deuxième élément de chaque sous-liste comme clé de tri (ordre croissant).
    l.sort(key = lambda x: x[1])
    
    # Création d'une nouvelle liste 'r' qui contient seulement le premier élément de chaque sous-liste de 'l'.
    r = [l[i][0] for i in range(n)]
    
    # Trie la liste 'r' en ordre croissant.
    r.sort()
    
    # Crée une nouvelle liste 'f' de taille 100001, remplie de zéros.
    # Cette liste permettra de réaliser des pré-calculs ou des accumulations rapides.
    f = [0 for i in range(100001)]
    
    # Pour chaque paire (a, b) de la liste 'l' :
    for a, b in l:
        # Incrémente l'élément d'indice 'a' dans 's' de 1 (débute une plage/intervalles).
        s[a] += 1
        
        # Décrémente l'élément d'indice 'b' dans 's' de 1 (terme une plage/intervalles à b).
        s[b] -= 1
        
        # Incrémente f[b] de 1 (utilisé pour compter les fins d'intervalles à b).
        f[b] += 1
    
    # Cette boucle réalise la somme de préfixe sur 's' et 'f' pour permettre des accès rapides par position.
    for i in range(100000):
        # Additionne la valeur précédente à l'indice suivant (somme cumulative sur 's').
        s[i+1] += s[i]
        
        # Idem pour 'f'.
        f[i+1] += f[i]
    
    # Initialise la variable 'ans' à zéro. Servira à garder la meilleure réponse trouvée.
    ans = 0
    
    # Pour chaque paire (a, b) de la liste 'l' :
    for a, b in l:
        # Utilisation de bisect.bisect_left pour trouver la première position où 'b' peut être inséré dans la liste triée 'r'
        # de façon à garder 'r' trié. Renvoie donc une position (indice).
        ri = bisect.bisect_left(r, b)
        
        # Calcule le nombre d'éléments strictement supérieurs à 'b' dans la liste 'r'.
        # 'n' est la longueur totale de la liste donc n - ri donne ce nombre.
        ri = n - ri
        
        # 'le' représente le nombre de fins d'intervalles à la position 'a'.
        le = f[a]
        
        # Mise à jour de la réponse avec la valeur maximale entre l'ancienne et la nouvelle calculée.
        ans = max(ans, n - (ri + le))
    
    # Affichage du résultat : la valeur maximale trouvée parmi les essais et la plus grande valeur dans la liste 's'.
    print(ans, max(s))
    return

###########################################################################
# Point d'entrée du script : appelle la fonction D lorsqu'exécuté directement
###########################################################################

if __name__ == "__main__":
    D()