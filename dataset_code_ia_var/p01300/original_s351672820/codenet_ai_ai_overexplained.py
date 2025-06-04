#!/usr/bin/env python

# Importation du module deque depuis collections, permettant de créer des files à double extrémité
from collections import deque
# Importation du module itertools avec un alias court 'it', utile pour manipuler des itérateurs rapides
import itertools as it
# Importation du module sys, nécessaire pour gérer certains paramètres comme la récursivité ou les flux
import sys

# On fixe la limite maximale de récursivité avec setrecursionlimit pour éviter les erreurs de dépassement de pile
# Cela permet à certains appels récursifs intensifs de ne pas s'arrêter prématurément
sys.setrecursionlimit(1000000)

# Début d'une boucle infinie qui ne sera interrompue que par une instruction explicite (break)
while True:
    # Lecture d'une chaîne de caractères depuis l'entrée standard de l'utilisateur avec raw_input
    # Note : raw_input() lit une ligne sous forme de string, y compris si elle ne contient que des chiffres
    S = raw_input()
    # Si l'utilisateur saisit uniquement '0', on considère que c'est le signal pour arrêter le programme
    if S == '0':
        # On sort de la boucle infinie grâce à l'instruction break
        break
    # Création d'un dictionnaire 'm' vide qui servira de table de hachage, pour indexer des listes selon un entier de 0 à 10
    m = {}
    # Boucle sur les entiers de 0 à 10 inclus (car range(11) va jusqu'à 10)
    for i in range(11):
        # Chaque clé du dictionnaire m représente un reste possible mod 11 et est initialisée par une liste vide
        m[i] = []
    # On ajoute la valeur 11 à la liste correspondant à la clé 0 dans le dictionnaire m
    # Cela sert probablement à initialiser une structure de référence utilisée plus tard
    m[0].append(11)
    # On initialise une variable diff à 0, représentant la différence alternée des chiffres selon la parité
    diff = 0
    # On utilise la variable 'even', booléenne, pour indiquer si on traite un chiffre dans une position paire (True) ou impaire (False)
    even = True
    # On inverse l'ordre de la chaîne S pour traiter les chiffres du dernier au premier
    S = reversed(S)
    # On parcourt chaque caractère (donc chiffre) de la chaîne inversée
    for c in S:
        # On convertit le caractère c en entier afin d'effectuer des opérations arithmétiques dessus
        num = int(c)
        # Si la position actuelle est paire (even == True)
        if even:
            # On ajoute le chiffre num à diff si la position est paire
            diff += num
        else:
            # On soustrait le chiffre num de diff si la position est impaire
            diff -= num
        # On réduit diff modulo 11 afin qu'il reste toujours compris entre 0 et 10
        diff %= 11
        # On ajoute le chiffre courant num à la liste des chiffres ayant ce reste diff dans le dictionnaire m
        m[diff].append(num)
        # On inverse l'état de even, pour alterner entre position paire et impaire à chaque chiffre
        even = (not even)
    # On initialise une variable de réponse ans à 0, qui servira à accumuler le résultat final
    ans = 0
    # #print m   # Ligne commentée : affichage optionnel du dictionnaire m pour déboguer
    # On parcourt tous les indices de 0 à 10 pour traiter les listes du dictionnaire m correspondant à chaque reste possible mod 11
    for i in range(11):
        # On récupère la liste lst des chiffres correspondant au reste i
        lst = m[i]
        # On parcourt tous les indices de cette liste, pour accéder à la position de chaque chiffre dans la liste
        for i in range(len(lst)):
            # Si le chiffre stocké à la position i de lst est différent de zéro
            if lst[i] != 0:
                # On ajoute la position i à la variable de réponse ans (et non la valeur !)
                ans += i
    # On affiche enfin la variable ans à la sortie standard, c'est le résultat calculé à partir de la chaîne S
    print ans