import numpy as np
from collections import Counter

def count_zero_sum_subarrays():
    """
    Lit une séquence d'entiers depuis l'entrée standard,
    puis calcule le nombre de sous-tableaux dont la somme est nulle.
    
    Utilise la technique des sommes cumulées et un Counter pour compter
    le nombre de paires d'indices ayant la même somme cumulée.
    
    Entrée :
        - La première ligne contient un entier n : la taille du tableau.
        - La seconde ligne contient n entiers séparés par des espaces.
    
    Sortie :
        - Un entier indiquant le nombre de sous-tableaux dont la somme est nulle.
    """
    # Lecture de la taille du tableau
    n = int(input())
    # Lecture de la liste d'entiers et ajout d'un zéro au début pour la gestion de la somme cumulée
    a = [0] + list(map(int, input().split()))
    # Calcul du tableau des sommes cumulées
    cumsum = np.cumsum(a)
    # Comptage du nombre d'occurrences de chaque somme cumulée
    c = Counter(cumsum)
    cnt = 0  # Initialise le compteur de sous-tableaux de somme nulle
    # Pour chaque somme cumulée apparaissant plusieurs fois,
    # le nombre de sous-tableaux correspondants est comb(n, 2)
    for i in c.values():
        if i > 1:
            cnt += int(i * (i - 1) / 2)
    # Affichage du résultat
    print(cnt)

# Appel de la fonction principale
count_zero_sum_subarrays()