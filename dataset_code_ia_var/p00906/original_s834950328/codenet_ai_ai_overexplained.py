#!usr/bin/env python3

# Importations de modules standards nécessaires pour le code :
from collections import defaultdict    # Permet de créer des dictionnaires avec une valeur par défaut lors de l'accès à une clé inexistante.
from collections import deque         # Fournit une file/queue à double entrées (Double-ended queue) pour des opérations efficaces d'ajout/retrait en début/fin.
from heapq import heappush, heappop   # Utilisé pour manipuler des files de priorité (min-heaps/max-heaps).
import sys                           # Pour utiliser des fonctions système telles que la lecture d'entrée standard.
import math                          # Fournit des fonctions mathématiques courantes.
import bisect                        # Pour l'insertion/recherche dans des listes triées.
import random                        # Fournit des générateurs de nombres aléatoires et des fonctions associées.

# Définitions de fonctions utilitaires pour gérer la lecture et la manipulation d'entrées :
def LI():
    # Lit une ligne de l'entrée standard (stdin), la découpe en éléments séparés par des espaces,
    # convertit chaque élément en entier, et retourne la liste d'entiers.
    return list(map(int, sys.stdin.readline().split()))

def I():
    # Lit une seule ligne depuis l'entrée standard, la convertit en entier, et retourne ce nombre.
    return int(sys.stdin.readline())

def LS():
    # Lit une ligne de l'entrée standard, la découpe selon les espaces, puis convertit chaque mot en une liste de caractères.
    # Retourne une liste de listes de caractères.
    return list(map(list, sys.stdin.readline().split()))

def S():
    # Lit une ligne de l'entrée standard, la convertit en une liste de caractères, puis enlève le dernier caractère (souvent un saut de ligne).
    return list(sys.stdin.readline())[:-1]

def IR(n):
    # Crée une liste pour stocker n éléments.
    # Lit n entiers, un par ligne, à partir de l'entrée standard, et les stocke dans la liste.
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    # Crée une liste pour stocker n éléments.
    # Lit n lignes de l'entrée standard, chaque ligne étant convertie en liste d'entiers (via LI), et stocke chaque résultat dans la liste.
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    # Crée une liste pour stocker n éléments.
    # Lit n lignes de l'entrée standard, chaque ligne étant convertie en une liste de caractères (via S), et stocke chaque résultat dans la liste.
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    # Crée une liste pour stocker n éléments.
    # Lit n lignes, chaque ligne est convertie en une liste de listes de caractères (via LS), stockée dans la liste.
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

# Augmenter la limite de récursion de Python pour éviter les erreurs de récursion maximum atteinte dans des cas approfondis.
# Cela est parfois nécessaire dans les problèmes de récursion/de graphe profonds.
sys.setrecursionlimit(1000000)

# Déclaration d'une constante mod qui pourra être utilisée dans les opérations de modulus (très courant dans les problèmes de programmation compétitive).
mod = 1000000007

# Définition de la fonction principale D qui sera appelée à la fin du script.

# Fonction D - Opérations de matrices avancées et simulation mathématique :
from operator import mul   # Importation de la fonction de multiplication élémentaire des deux opérandes.

def D():
    # Fonction utilitaire pour calculer le produit scalaire (dot product) de deux listes (vecteurs) a et b.
    def dot(a, b):
        # Utilise map pour appliquer la multiplication élément à élément entre a et b,
        # puis somme tous les résultats pour obtenir le produit scalaire.
        return sum(map(mul, a, b))

    # Fonction pour multiplier deux matrices (a et b), avec prise de modulus m sur chaque opération.
    def mul_matrix(a, b, m):
        # zip(*b) permet de transposer la matrice b, afin que les lignes de b deviennent ses colonnes. Cela est utile pour la multiplication de matrices.
        tb = tuple(zip(*b))

        # Pour chaque ligne a_i dans la matrice a, et chaque colonne b_j dans la matrice b transposée,
        # on calcule le produit scalaire puis on prend son reste modulo m.
        # Ceci donne une nouvelle ligne de la matrice résultat.
        return [[dot(a_i, b_j) % m for b_j in tb] for a_i in a]

    # Fonction qui élève une matrice a à la puissance n, sous module m.
    # Simplement, effectue une "exponentiation rapide" (modulaire) sur les matrices.
    def pow_matrix(a, n, m):
        # h récupère la taille de la matrice carrée (supposition)
        h = len(a)
        # Initialisation de la matrice identité de taille h x h.
        b = [[1 if i == j else 0 for j in range(h)] for i in range(h)]
        k = n  # Compteur pour l'exposant.
        while k:
            if (k & 1):
                # Si l'exposant k est impair, multiplie la matrice résultat par la matrice courante.
                b = mul_matrix(b, a, m)
            # Multiplie la matrice courante par elle-même (carré), ce qui permet de traiter l'exposant par division par 2.
            a = mul_matrix(a, a, m)
            k >>= 1    # Décale k à droite, équivalent à k //= 2
        return b

    # Commence une boucle infinie. Permet de traiter plusieurs jeux de données sans relancer le programme.
    while 1:
        # Lecture de 6 entiers sur une ligne, assignés aux variables n, m, a, b, c, t respectivement.
        n, m, a, b, c, t = LI()

        # Si tous les paramètres sont à zéro (ou seulement n), alors la boucle s'arrête (condition d'arrêt).
        if n == 0:
            break

        # Lecture d'une ligne de n entiers, stockée dans la liste s.
        s = LI()

        # Crée une liste s2, qui est une liste de listes. Chaque sous-liste contient l'élément s[i].
        # Cela prépare le vecteur pour la multiplication matricielle plus tard (simule un vecteur colonne).
        s2 = [[s[i] for j in range(1)] for i in range(n)]

        # Initialisation d'une matrice carrée mat de taille n x n, avec tous les éléments à 0 au départ.
        mat = [[0 for j in range(n)] for i in range(n)]

        # Remplissage manuel de la matrice mat selon des règles particulières. Cela correspond souvent à des matrices de transition dans les récursions linéaires.
        mat[0][0] = b    # Mettre la valeur de b dans la case [0][0]
        mat[0][1] = c    # Mettre la valeur de c dans la case [0][1]
        # Pour chaque ligne de la 1 à n-2 (i allant de 1 à n-2 inclus), remplir 3 cases selon a, b, c
        for i in range(1, n-1):
            mat[i][i-1] = a
            mat[i][i]   = b
            mat[i][i+1] = c
        mat[n-1][-2] = a  # Remplir avant-dernière colonne de la dernière ligne avec a
        mat[n-1][-1] = b  # Remplir dernière colonne de la dernière ligne avec b

        # Exponentiation de la matrice : mat = mat^t (modulo m)
        mat = pow_matrix(mat, t, m)

        # Multiplie la matrice mat obtenue par le vecteur colonne s2, sous module m.
        mat = mul_matrix(mat, s2, m)

        # Affiche les éléments du vecteur résultat ligne par ligne, tous séparés d'espaces, sauf le dernier qui termine par \n.
        for i in mat[:-1]:
            print(i[0], end=" ")
        print(mat[-1][0])
    return  # Fin de la fonction D

# Bloc d'exécution principal du script.
if __name__ == "__main__":
    # Si ce fichier est exécuté directement, la fonction D est appelée.
    D()