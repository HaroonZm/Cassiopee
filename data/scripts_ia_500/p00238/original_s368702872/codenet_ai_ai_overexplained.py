import sys, os  # Importation des modules sys et os, bien que non utilisés dans ce code. Ces modules permettent respectivement l'interaction avec l'interpréteur Python et les fonctions du système d'exploitation.

while 1:  # Boucle infinie qui va continuer à s'exécuter indéfiniment jusqu'à rencontrer une instruction de sortie (break).
    t = int(input())  # Lecture d'une entrée utilisateur sous forme de chaîne de caractères via input(), puis conversion en entier avec int().
    if t == 0:  # Condition qui vérifie si la valeur entrée est 0.
        break  # Sortie de la boucle infinie si la condition est vraie, ce qui met fin au programme.
    n = int(input())  # Lecture d'une deuxième entrée utilisateur, convertie en entier, qui représente un nombre d'intervalles à lire.
    # Lecture de n lignes suivantes où chaque ligne contient plusieurs nombres séparés par des espaces.
    # Chaque ligne est transformée en une liste d'entiers. La compréhension de liste crée une liste contenant n sous-listes.
    sf = [list(map(int, input().split())) for _ in range(n)]
    
    time = 0  # Initialisation d'une variable 'time' à 0. Cette variable accumulera la somme des durées calculées.
    
    for i in sf:  # Parcours de chaque élément (sous-liste) dans la liste 'sf'.
        start, end = i  # Extraction des deux éléments de la sous-liste, probablement représentant des heures de début et fin.
        if start > end:  # Vérification si l'heure de début est supérieure à l'heure de fin, ce qui pourrait indiquer un dépassement de minuit.
            # Calcul de la durée en tenant compte du passage à un nouveau jour (minuit). On soustrait 24 à 'start' pour ajuster.
            time += end - (start - 24)
        else:  # Cas où l'heure de début est inférieure ou égale à l'heure de fin.
            time += end - start  # Calcul simple de la durée entre start et end et ajout à 'time'.
    
    if time >= t:  # Vérification si la somme des durées est suffisante pour atteindre ou dépasser la valeur 't' initiale.
        print("OK")  # Affichage de "OK" si c'est le cas.
    else:  # Sinon,
        print(t - time)  # Affichage de la différence entre 't' et 'time', indiquant combien de temps il manque pour atteindre 't'.