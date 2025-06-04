cnt = 0  # Compteur global pour suivre le nombre d’opérations lors des divisions

def merge_sort(array):
    """
    Trie une liste d'entiers en utilisant l'algorithme de tri fusion (merge sort).
    Incrémente un compteur global à chaque division de la liste.

    Args:
        array (list): La liste d'entiers à trier.

    Returns:
        list: Une nouvelle liste triée contenant les mêmes éléments que 'array'.
    """
    global cnt  # Utilisation de la variable globale cnt pour compter les divisions
    # Cas de base : une liste vide ou de 1 élément est déjà triée
    if len(array) <= 1:
        return array
    # Calcul de l'indice médian pour diviser la liste
    mid = len(array) // 2
    left = array[:mid]    # Sous-liste de gauche
    right = array[mid:]   # Sous-liste de droite
    # Incrémentation du compteur cnt du total d’éléments actuellement dans les sous-listes
    cnt += len(left) + len(right)
    # Tri récursif des sous-listes
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # Fusion des sous-listes triées
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Fusionne deux listes triées en une seule liste triée.

    Args:
        left (list): Première liste triée.
        right (list): Deuxième liste triée.

    Returns:
        list: Liste fusionnée et triée contenant tous les éléments de 'left' et 'right'.
    """
    result = []        # Liste pour stocker le résultat de la fusion
    l_index, r_index = 0, 0  # Indices pour parcourir 'left' et 'right'

    # Boucle jusqu'à ce que l'une des listes soit épuisée
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            # L’élément courant de 'left' est plus petit ou égal : on l’ajoute au résultat
            result.append(left[l_index])
            l_index += 1
        else:
            # L’élément courant de 'right' est plus petit : on l’ajoute au résultat
            result.append(right[r_index])
            r_index += 1

    # On ajoute les éléments restants de 'left' (s’il y en a)
    if l_index < len(left):
        result.extend(left[l_index:])
    # On ajoute les éléments restants de 'right' (s’il y en a)
    if r_index < len(right):
        result.extend(right[r_index:])

    # Renvoie la liste fusionnée et triée
    return result

# Lecture de la taille de la liste (non utilisée directement ici, mais peut servir à la saisie)
n = int(input())
# Lecture de la liste d'entiers à trier
S = list(map(int, input().split()))
# Appel du tri fusion sur la liste saisie
array = merge_sort(S)
# Affichage de la liste triée (éléments séparés par des espaces)
print(" ".join(map(str, array)))
# Affichage du nombre d'opérations de division (calculées par 'cnt')
print(cnt)