"""
Ce script Python applique l'algorithme de tri de tas (heapify) sur une liste d'entiers.
Il lit les données depuis l'entrée standard, construit un tas max, puis affiche la liste réorganisée.
"""

def h(i):
    """
    Réajuste l'élément à la position i dans le tas pour maintenir la propriété de tas max.

    Args:
        i (int): L'index du nœud à ajuster dans le tableau A.
    """
    l = 2 * i                 # Index du fils gauche
    r = l + 1                 # Index du fils droit
    # Sélectionne le fils ayant la plus grande valeur (si existant)
    if l < H and A[i] < A[l]:
        g = l
    else:
        g = i
    if r < H and A[g] < A[r]:
        g = r
    # Si un des enfants a une plus grande valeur que le parent, on échange et on poursuit récursivement
    if g > i:
        A[i], A[g] = A[g], A[i]
        h(g)

# Lecture de la taille du tableau (nombre d'éléments), ajusté pour avoir un indice de départ à 1
H = int(input()) + 1
# Lecture du tableau à trier, insertion d'un zéro en première position afin de commencer l'indexation à 1
A = [0] + list(map(int, input().split()))
# On applique l'opération de heapify en partant du dernier parent jusqu'à la racine
for i in range(H // 2, 0, -1):
    h(i)
# Affichage du tableau transformé en tas max (on saute la première valeur fictive)
print(' ' + ' '.join(map(str, A[1:])))