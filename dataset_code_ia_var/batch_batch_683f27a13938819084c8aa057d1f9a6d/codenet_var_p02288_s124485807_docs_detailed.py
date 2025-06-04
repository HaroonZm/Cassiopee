"""
Ce script convertit une liste d'entiers A représentant un tas (heap) non ordonné en un tas binaire conforme à la propriété de tas min (min-heap).
L'utilisateur donne la taille du tableau et les éléments. Le résultat est affiché sous la forme d'une ligne d'entiers représentant le tas minifié.
"""

def heapify(i):
    """
    Maintient la propriété de tas min (min-heap) en vérifiant le nœud à l'indice i et ses enfants, 
    puis permute les éléments si nécessaire, de manière récursive jusqu'à l'obtention d'un tas min.

    Args:
        i (int): Indice du nœud racine du sous-arbre à 'tasifier'
    """
    left = 2 * i                    # Indice du fils gauche
    right = left + 1                # Indice du fils droit
    # Supposons initialement que le plus petit est la racine (i)
    smallest = i

    # Si le fils gauche existe et qu'il est plus petit que la racine, mettre à jour smallest
    if left < H and A[smallest] > A[left]:
        smallest = left

    # Si le fils droit existe et qu'il est plus petit que smallest, mettre à jour smallest
    if right < H and A[smallest] > A[right]:
        smallest = right

    # Si le plus petit n'est pas la racine, échanger et continuer récursivement
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        heapify(smallest)

# Lecture de la taille du tas (nombre d'éléments de la liste)
H = int(input()) + 1  # +1 pour gérer le décalage d'index, car on commence à 1

# Lecture des éléments du tas, ajout d'un zéro initial pour un indexage à partir de 1
A = [0] + list(map(int, input().split()))

# Construire le tas min (min-heap) en appelant heapify sur tous les nœuds internes, de bas en haut
for i in range(H // 2, 0, -1):
    heapify(i)

# Affiche le tas minifié (en ignorant l'élément à l'index 0)
print(' ' + ' '.join(map(str, A[1:])))