import numpy as np  # Importe la bibliothèque numpy et l'abrège en 'np' pour un accès facile aux fonctions et objets qu'elle contient

import heapq  # Importe la bibliothèque 'heapq' pour manipuler des files de priorité (min-heaps) en Python

N = int(input())  # Lit une entrée utilisateur, qui doit être un nombre entier, puis la convertit en entier et l'assigne à la variable N
a = list(map(int, input().split()))  # Lit une seconde ligne d'entrée utilisateur, fractionne cette chaîne selon les espaces, transforme chaque élément en entier, construit une liste et l'assigne à 'a'
ra = -np.array(a[::-1])  # Prend la liste 'a', la renverse avec une coupe [::-1], la convertit en tableau numpy, prend le négatif de chaque élément et le stocke dans 'ra'

def serchPop(alst):
    """Calcule, pour chaque fenêtre glissante de taille N sur la liste alst (de taille 2*N), 
    la somme minimale possible des N éléments dans cette fenêtre en utilisant un min-heap"""
    h = []  # Initialise une liste vide 'h', qui servira de min-heap (file de priorité) pour stocker les éléments concernés
    total = []  # Initialise une liste vide 'total' afin de stocker les différentes sommes calculées
    sum = 0  # Initialise la variable 'sum' à 0 ; elle contiendra la somme courante des N éléments dans le heap

    # Parcours de chaque indice de 0 jusqu'à 2*N - 1 inclus (soit 2*N éléments)
    for i in range(2 * N):
        heapq.heappush(h, alst[i])  # Ajoute l'élément courant alst[i] au min-heap 'h', de sorte que le plus petit élément reste en tête
        sum += alst[i]  # Ajoute la valeur courante à 'sum', pour tenir à jour la somme des éléments actuellement dans le heap
        
        # S'il y a déjà plus de N éléments dans le heap, on retire le plus petit pour ne conserver que N éléments
        if i >= N:
            tmp = heapq.heappop(h)  # Retire (et récupère) l'élément minimal du min-heap 'h'
            sum -= tmp  # Soustrait cet élément retiré de la somme courante

        # Si le nombre total d'éléments ajoutés atteint au moins N (donc qu'on a formé une première fenêtre complète)
        if i >= N - 1:
            total.append(sum)  # Ajoute la somme courante à la liste 'total'
    
    return total  # Retourne la liste des sommes calculées, au total, il y en aura N+1

ans = -10 ** 20  # Initialise la variable 'ans' à une très petite valeur (nombre négatif arbitraire), garantissant qu'une valeur trouvée sera plus grande au début

ltotal = serchPop(a)  # Calcule la liste des sommes maximales pour chaque fenêtre glissante de taille N au début de la liste 'a'
rtotal = serchPop(ra)  # Calcule de même sur la version inversée et négativée de 'a', obtenant ainsi les valeurs "droites"

# Boucle sur tous les indices de 0 à N inclus pour examiner chaque découpage possible
for i in range(N + 1):
    # Pour chaque découpage, calcule la somme de ltotal[i] (pour les premiers i éléments) et rtotal[N - i] (pour les N derniers moins i à partir de la droite)
    # Utilise max pour garder la valeur maximale rencontrée
    ans = max(ans, ltotal[i] + rtotal[N - i])

print(ans)  # Affiche la valeur finale de 'ans', qui est la plus grande somme obtenue selon la logique précédente