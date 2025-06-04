# Importation du module sys, qui fournit certaines fonctions et variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python
import sys
# Importation du module os, qui offre de nombreuses fonctions pour interagir avec le système d'exploitation
import os
# Importation du module math, qui fournit des fonctions mathématiques courantes (n'est pas utilisé dans ce code, mais inclus ici comme dans le code d'origine)
import math

# Lecture d'une ligne sur l'entrée standard (le clavier), qui est censée contenir un nombre entier (le nombre de personnes)
N = int(input())  # Conversion immédiate de l'entrée (qui est de type chaîne de caractères) en entier avec la fonction int()

# Création d'une liste appelée A qui contient 6 zéros, qui va servir à compter le nombre d’individus dans chaque intervalle de taille
# On utilise l'opérateur de multiplication pour créer une liste de taille 6 remplie de zéros : [0, 0, 0, 0, 0, 0]
A = [0] * 6

# Boucle for qui itère N fois, où chaque itération correspond à une personne dont la taille sera saisie
for i in range(N):
    # Lecture de la taille de la personne sur une ligne d'entrée, convertie en nombre à virgule flottante (fonction float())
    h = float(input())
    
    # Test conditionnel pour vérifier dans quelle plage se trouve la taille de la personne (variable h)
    # On utilise des instructions if...elif...else pour répartir dans le bon intervalle
    
    # Si la taille est strictement inférieure à 165.0, incrémenter le premier élément de la liste A (indice 0)
    if h < 165.0:
        A[0] += 1  # On ajoute 1 à l'élément situé à l'indice 0 de la liste A
    # Si la condition précédente est fausse, mais que la taille est strictement inférieure à 170.0, incrémenter le second élément (indice 1)
    elif h < 170.0:
        A[1] += 1  # On ajoute 1 à l'élément situé à l'indice 1 de la liste A
    # Si les conditions précédentes sont fausses, mais que la taille est strictement inférieure à 175.0, incrémenter le troisième élément (indice 2)
    elif h < 175.0:
        A[2] += 1
    # Si la taille est strictement inférieure à 180.0, on incrémente le quatrième élément (indice 3)
    elif h < 180.0:
        A[3] += 1
    # Si la taille est strictement inférieure à 185.0, on incrémente le cinquième élément (indice 4)
    elif h < 185.0:
        A[4] += 1
    # Si aucune des conditions précédentes n'est vraie (donc h >= 185.0), on incrémente le dernier élément (indice 5)
    else:
        A[5] += 1

# Boucle for pour parcourir la liste A avec l'indice i et la valeur correspondante a à chaque position
# La fonction enumerate fournit à la fois l'indice (i) et la valeur (a) pour chaque itération
for i, a in enumerate(A):
    # Création d'une chaîne de caractères s qui affiche l'intervalle de taille (i+1 car les humains comptent à partir de 1, alors que les indices Python commencent à 0)
    # puis le caractère '*' répété autant de fois qu'il y a de personnes dans cet intervalle (c'est-à-dire la valeur de a)
    s = "{}:{}".format(i+1, '*' * a)  # Cela concatène le numéro du groupe et les étoiles (une par personne)
    # Affichage de la chaîne s à l'écran grâce à print()
    print(s)