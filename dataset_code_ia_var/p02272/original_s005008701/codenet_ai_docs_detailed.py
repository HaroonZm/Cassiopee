import math

# Définition de la valeur sentinelle suffisamment grande pour garantir qu'aucun élément du tableau ne la dépasse lors de la fusion.
sentinel = 1e9 + 1
# Variable globale utilisée pour compter le nombre d'opérations de fusion effectuées.
counter = 0

def merge(a, left, mid, right):
    """
    Fusionne deux sous-tableaux triés de 'a' du segment [left:mid) et [mid:right) en un seul sous-tableau trié.
    Utilise une valeur sentinelle pour éviter de vérifier la fin des tableaux L et R à chaque itération.
    Met à jour la variable globale 'counter' en ajoutant le nombre d'éléments fusionnés.

    Args:
        a (list of int): Tableau principal contenant les éléments à trier.
        left (int): Indice de début (inclus) du premier sous-tableau.
        mid (int): Indice de séparation des deux sous-tableaux.
        right (int): Indice de fin (exclu) du second sous-tableau.

    Returns:
        None: Modifie le tableau 'a' en place.
    """
    global counter

    # Création des sous-tableaux gauche et droit, chacun agrémenté d'une valeur sentinelle à la fin.
    L = a[left:mid] + [sentinel]
    R = a[mid:right] + [sentinel]
    i, j = 0, 0

    # Parcours de la plage [left, right) pour fusionner L et R dans 'a'
    for k in range(left, right):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

    # Mise à jour du compteur (nombre d'opérations de fusion réalisées)
    counter += right - left

def mergeSort(a, left, right):
    """
    Trie récursivement le segment [left:right) du tableau 'a' avec l'algorithme du tri fusion.

    Args:
        a (list of int): Tableau contenant les éléments à trier.
        left (int): Indice de début (inclus) du segment à trier.
        right (int): Indice de fin (exclu) du segment à trier.

    Returns:
        None: Modifie le tableau 'a' en place.
    """
    # Si le segment contient plus d'un élément, le diviser et trier/réaliser la fusion récursivement
    if left + 1 < right:
        mid = (left + right) // 2
        # Trier la moitié gauche
        mergeSort(a, left, mid)
        # Trier la moitié droite
        mergeSort(a, mid, right)
        # Fusionner les deux moitiés triées
        merge(a, left, mid, right)

# Lecture de la taille du tableau à trier depuis l'entrée standard.
n = int(input())
# Lecture du tableau d'entiers à trier, converti depuis l'entrée standard.
a = list(map(int, input().split()))
# Tri du tableau entier avec mergeSort.
mergeSort(a, 0, n)
# Affichage du tableau trié (éléments séparés par des espaces).
print(*a)
# Affichage du compteur d'opérations de fusion.
print(counter)