#!/usr/bin/env python

# Importation du module math, qui fournit des fonctions mathématiques standards comme sqrt (racine carrée)
import math

# Définition de la fonction de crible d'Ératosthène, un algorithme classique utilisé pour trouver tous les nombres premiers jusqu'à un certain nombre 'num'
def sieve_of_erastosthenes(num):
    # Création d'une liste appelée 'input_list' de taille 'num' où chaque élément représente un nombre de 0 à num-1
    # On utilise une compréhension de liste pour remplir cette liste selon une condition:
    # Pour chaque index 'i' de 0 à num-1, on vérifie s'il est divisible par 2, 3 ou 5
    # Si 'i' est divisible par 2, 3, ou 5 (c'est-à-dire que 'i % 2 == 0' OU 'i % 3 == 0' OU 'i % 5 == 0'), alors on met la valeur à False
    # Sinon, on met la valeur à True, comme s'il pouvait potentiellement être un nombre premier
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    
    # On sait que 0 et 1 ne sont pas des nombres premiers. On définit donc explicitement 'input_list[0]' et 'input_list[1]' sur False
    input_list[0] = input_list[1] = False
    
    # On sait que 2, 3 et 5 sont des nombres premiers, donc on met explicitement 'input_list[2]', 'input_list[3]' et 'input_list[5]' sur True
    input_list[2] = input_list[3] = input_list[5] = True
    
    # On calcule la racine carrée (sqrt) de 'num' en utilisant la fonction sqrt du module math
    # Criblage jusqu'à la racine carrée suffit car un multiple supérieur a déjà été marqué non premier par un facteur plus petit
    sqrt = math.sqrt(num)

    # On parcourt les nombres impairs à partir de 3 jusqu'à num-1 avec un pas de 2 (pour éviter les nombres pairs, déjà traités)
    for serial in range(3, num, 2):
        # Si 'serial' est supérieur ou égal à la racine carrée de num, on arrête le processus et on retourne la liste
        if serial >= sqrt:
            # On termine la fonction en renvoyant la liste mise à jour
            return input_list
        # Si 'input_list[serial]' est True, c'est donc un nombre premier, il faut alors marquer tous ses multiples comme False (non premiers)
        # Attention : On commence le marquage à 'serial ** 2' parce que les multiples plus petits auraient déjà été marqués par des facteurs plus petits
        for s in range(serial ** 2, num, serial): 
            # On marque l'indice 's' (correspondant à un multiple de 'serial') comme False, c'est-à-dire non premier
            input_list[s] = False

# Appel de la fonction sieve_of_erastosthenes pour générer une table de primalité ('primeTable') jusqu'à 13 fois 10 exposant 5 (soit 1 300 000)
# Cette table est une liste de booléens où l'indice représente le nombre entier et la valeur True/False indique s'il est premier ou non
primeTable = sieve_of_erastosthenes(13*(10**5))

# Début d'une boucle infinie pour traiter des entrées utilisateur jusqu'à condition d'arrêt explicite
while True:
    # Lecture d'une entrée utilisateur via la fonction input() et conversion en entier avec int()
    k = int(input())
    # Si la valeur entrée 'k' est égale à zéro, alors on sort de la boucle avec 'break', ce qui arrête le programme
    if k == 0:
        break
    # Si la valeur à l'indice 'k' dans 'primeTable' est True, cela signifie que 'k' est un nombre premier
    if primeTable[k]:
        # On affiche 0, car la différence entre le plus proche nombre premier supérieur ou égal et inférieur ou égal à 'k' est nulle
        print(0)
    else:
        # Si 'k' n'est pas premier
        # On cherche le prochain nombre premier supérieur à 'k'. On initialise 'i' avec la valeur de 'k'
        i = k
        # Tant que 'primeTable[i]' est False (donc tant que 'i' n'est pas premier), on incrémente 'i' de 1 à chaque tour de boucle
        while primeTable[i] is False: 
            i += 1
        # Maintenant, 'i' est le premier nombre premier supérieur ou égal à 'k'
        # On cherche ensuite le plus grand nombre premier plus petit que 'k'. On initialise 'j' avec 'i-1'
        j = i-1
        # Tant que 'primeTable[j]' est False (donc tant que 'j' n'est pas premier), on décrémente 'j' de 1 à chaque tour de boucle
        while primeTable[j] is False: 
            j -= 1
        # Maintenant, 'j' est le plus grand nombre premier inférieur à 'k'
        # On affiche la différence entre le prochain nombre premier après 'k' et le précédent nombre premier avant 'k'
        print(i-j)