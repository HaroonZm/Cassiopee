#!/usr/bin/env python

"""
input:
4
1 2 3 5

output:
30
"""

# Importation du module sys pour accéder à sys.stdin, qui permet de lire depuis l'entrée standard (par exemple, lors d'un lancement du script depuis un terminal avec des entrées données via un pipe ou une redirection).
import sys

# Importation de la fonction reduce depuis functools.
# reduce permet d'appliquer de façon cumulative une fonction binaire (qui prend deux arguments) à une séquence, pour la réduire à une seule valeur.
from functools import reduce

# Importation de la fonction mod depuis le module operator.
# mod représente l'opérateur modulo, équivalent à l'opérateur % qui donne le reste de la division entière.
from operator import mod

# Définition d'une fonction pour calculer le PGCD (Plus Grand Commun Diviseur) de deux entiers.
def gcd(x, y):
    # Si x est strictement inférieur à y, on échange les valeurs de x et y.
    # Ceci pour s'assurer que x soit toujours supérieur ou égal à y, ce qui simplifie l'algorithme.
    if x < y:
        x, y = y, x

    # Boucle tant que y est strictement supérieur à 0.
    # Le but est de trouver un entier qui divise à la fois x et y sans laisser de reste.
    while y > 0:
        # On calcule le reste de la division de x par y.
        r = mod(x, y)
        # On met à jour x avec la valeur de y, car dans l'algorithme d'Euclide, la prochaine étape considère y comme le nouveau "grand" nombre.
        x = y
        # On met à jour y avec le reste calculé précédemment, selon l'algorithme d'Euclide.
        y = r

    # Lorsque y est égal à 0, x contient le PGCD (le plus grand entier positif qui divise x et y).
    return x

# Définition d'une fonction pour calculer le PPCM (Plus Petit Commun Multiple) de deux entiers a et b.
def lcm(a, b):
    # Le PPCM de deux entiers est obtenu en multipliant a et b, puis en divisant par leur PGCD.
    # (Ceci fonctionne car PPCM(a, b) x PGCD(a, b) = a x b)
    # La division entière (//) garantit un résultat entier.
    return a * b // gcd(a, b)

# Définition d'une fonction de résolution du problème, prenant une liste d'entiers en paramètre.
def solve(_n_list):
    # On utilise reduce pour appliquer la fonction lcm à tous les éléments de la liste.
    # L'opération commence sur les deux premiers éléments, puis applique le résultat à l'élément suivant, etc.
    # Cela permet de trouver le PPCM de toute la séquence d'entiers.
    return reduce(lcm, _n_list)

# Début du script principal : ce bloc s'exécutera seulement si ce fichier est exécuté comme un script principal.
if __name__ == '__main__':
    # sys.stdin.readlines() lit toutes les lignes de l'entrée standard et retourne une liste de chaînes de caractères.
    # Exemple : Si l'utilisateur tape "4" puis "1 2 3 5", on obtiendra ['4\n', '1 2 3 5\n']
    _input = sys.stdin.readlines()
    # On convertit la première ligne (indice 0) en entier pour obtenir le nombre d'éléments à traiter.
    # On enlève automatiquement le caractère de saut de ligne avec int().
    cnt = int(_input[0])
    # On traite la deuxième ligne (indice 1), on enlève les espaces superflus au début/à la fin,
    # on découpe la chaine en fonction des espaces avec split(), 
    # puis on convertit chaque sous-chaîne obtenue en un entier (grâce à map(int, ...)), 
    # et enfin on transforme l'objet map en tuple pour obtenir n_list.
    n_list = tuple(map(int, _input[1].split()))
    # On appelle la fonction solve avec la liste d'entiers obtenue, et on affiche le résultat avec print.
    print(solve(n_list))