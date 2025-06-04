#!/usr/bin/env python3

# Importation du module numpy sous l'alias np, bien que ce module ne soit pas utilisé dans ce script
import numpy as np

# Importation du module sys, qui fournit diverses fonctions et variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python
import sys

# Déclaration d'une variable 'read' qui pointe sur l'attribut buffer.read de sys.stdin,
# ce qui permettrait de lire les entrées binaires à partir de l'entrée standard,
# cependant, cette variable n'est pas utilisée dans le reste du code
read = sys.stdin.buffer.read

# Définition d'une fonction principale nommée 'main' qui ne prend pas d'argument
def main():
    # Lecture d'une seule ligne depuis l'entrée standard, puis découpage de cette ligne en éléments,
    # puis conversion de chaque élément en entier grâce à 'map(int, ...)'.
    # 'n', 'm', et 'c' sont respectivement le nombre de lignes de la matrice suivante,
    # le nombre de colonnes par ligne, et une constante entière ajoutée plus tard à un calcul.
    n, m, c = map(int, input().split())

    # Lecture d'une deuxième ligne depuis l'entrée standard.
    # Cette ligne est transformée en liste d'entiers à l'aide de 'map(int, ...)' et 'list(...)'.
    # La liste 'l' contient 'm' entiers. Généralement, il s'agit d'une liste de coefficients pondérateurs.
    l = list(map(int, input().split()))

    # Création d'une liste 'p' pour contenir 'n' listes,
    # chaque sous-liste est réalisée en lisant une ligne de l'entrée standard, en la découpant,
    # puis en convertissant chaque élément en entier grâce à 'map(int, ...)'.
    # Ceci est exécuté pour chaque ligne, pour un total de 'n' itérations de boucle for.
    # Le résultat est une liste de listes d'entiers de dimension n x m.
    p = [list(map(int, input().split())) for i in range(n)]

    # Initialisation d'une variable compteur à 0 ; elle servira à compter le nombre de cas répondant à un critère plus loin
    count = 0

    # Boucle sur chaque sous-liste (chaque ligne de la matrice p) ;
    # l'élément courant 'sor' est une liste d'entiers de longueur m.
    for sor in p:
        # La variable temporaire 'tmp' est initialisée avec la valeur de la constante 'c' pour chaque ligne
        tmp = c
        # Boucle sur chaque élément de 'sor' ;
        # enumerate(sor) fournit à chaque itération un index 'i' (entier croissant de 0 à m-1)
        # et l'élément lui-même 'j' (entier à la position i dans la liste courante 'sor')
        for i, j in enumerate(sor):
            # À chaque itération, ajouter au cumul 'tmp' le produit du coefficient l[i]
            # (élément i de la liste l) et de l'élément courant 'j' de la ligne de p;
            # c'est l'équivalent d'une multiplication scalaire partielle.
            tmp = tmp + j * l[i]
        # Après les m itérations, 'tmp' contient la somme initiale 'c' augmentée de la combinaison pondérée
        # des éléments de la ligne courante de p, le tout pondéré par l
        # On vérifie maintenant si 'tmp' est strictement positif (supérieur à zéro)
        if tmp > 0:
            # Si oui, on incrémente le compteur 'count' de 1 pour noter que cette ligne vérifie la condition
            count += 1
    # Après avoir traité toutes les lignes de la matrice p, afficher la valeur finale de 'count' sur la sortie standard
    print(count)

# Condition qui vérifie si le script est exécuté directement (et non pas importé comme module dans un autre fichier)
if __name__ == '__main__':
    # Appel de la fonction principale 'main' si le script est exécuté comme programme principal
    main()