import sys  # Importe le module sys, qui fournit des fonctions et variables utilisées pour manipuler différentes parties de l’environnement d’exécution Python, notamment la gestion des entrées/sorties

from collections import deque  # Importe deque depuis le module collections, une structure de données optimisée pour ajouter et retirer des éléments des deux côtés rapidement

readline = sys.stdin.readline  # Associe la fonction sys.stdin.readline à la variable readline pour lire une ligne à partir de l’entrée standard (clavier ou fichier redirigé)

n = int(readline())  # Lit une ligne de l’entrée (attendue être un entier), convertit la chaîne lue en entier, et l’attribue à n (taille de la liste)

li = list(map(int, readline().split()))  # Lit la ligne suivante de l’entrée, la découpe en morceaux selon les espaces, convertit chaque morceau en entier avec map, puis met le tout dans une liste appelée li

def square(P):  # Définition d’une fonction nommée square qui prend un argument P (liste d’entiers)
    G = []  # Crée une liste vide G qui servira à stocker des résultats calculés (les aires)
    L = deque()  # Crée une instance de deque (double-ended queue), qui sera utilisée comme pile pour stocker des tuples (indice, valeur)

    for i, v in enumerate(P):  # Boucle sur les indices (i) et les valeurs (v) de la liste P, enumerate permet d’obtenir la position et la valeur simultanément
        if not L:  # Vérifie si la deque L est vide (aucun élément dedans)
            L.append((i, v))  # Ajoute le tuple (indice, valeur) dans L, car il n’y a rien à comparer
            continue  # Passe directement à l’itération suivante de la boucle, sans exécuter la suite du code dans la boucle pour cette itération

        if v > L[-1][1]:  # Si la valeur actuelle v est strictement plus grande que la valeur du dernier élément ajouté à L (L[-1][1] est la valeur du tuple tout au bout)
            L.append((i, v))  # Ajoute le tuple (indice, valeur) à L, car les valeurs croissantes sont directement empilées
        elif v < L[-1][1]:  # Si par contre la valeur actuelle v est strictement inférieure à la valeur au sommet de la pile
            k = i - 1  # Calcule un nouvel indice k qui est l’indice immédiatement précédent
            while L and v < L[-1][1]:  # Boucle tant que la pile n’est pas vide ET que la valeur actuelle v est strictement inférieure à la valeur au sommet
                a = L.pop()  # Retire et récupère le dernier élément de L, qui sera stocké sous le nom a (un tuple de la forme (indice, valeur))
                # Calcule l’aire possible si on considère un rectangle s’étendant du point de a[0] à k avec une hauteur de a[1]
                G.append((k - a[0] + 1) * a[1])  # Ajoute à G l’aire calculée par la formule (largeur) x (hauteur)
            L.append((a[0], v))  # Après avoir dépilé tous les rectangles plus grands, ajoute dans la pile le nouvel intervalle (retient comme position de départ celle du dernier dépilé)

    # À ce point, toutes les positions ont été traitées, mais il peut rester des éléments dans la pile
    while L:  # Tant qu’il reste au moins un élément dans L
        a = L.pop()  # Retire et récupère le dernier élément de L
        G.append((n - a[0]) * a[1])  # Calcule l’aire du rectangle possible de la position a[0] jusqu’à la fin (indice n-1), hauteur a[1], et l’ajoute à G

    return max(G)  # Retourne la plus grande aire trouvée (valeur maximale de la liste G)

print(square(li))  # Appelle la fonction square avec li comme argument (la liste d’entiers saisie au début) et affiche le résultat retourné par la fonction square