def maxHeapify(A, i):
    """
    Maintient la propriété de tas maximum à partir du noeud d'indice i dans le tableau A.

    Si l'un des enfants du noeud i est plus grand que A[i], échange A[i] avec le plus grand enfant et continue récursivement.

    Args:
        A (list): Tableau représentant le tas (1-indicé).
        i (int): Indice du noeud à vérifier/corriger dans le tas.

    Returns:
        None: La fonction modifie le tableau A en place.
    """
    # Calculer les indices des fils gauche et droit du noeud i dans le tableau 1-indicé
    l = 2 * i          # Fils gauche
    r = 2 * i + 1      # Fils droit

    # Chercher le plus grand entre i, son fils gauche (s'il existe), et son fils droit (s'il existe)
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= H and A[r] > A[largest]:
        largest = r

    # Si le noeud i n'est pas le plus grand, échanger avec le plus grand enfant et continuer récursivement
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Échange des valeurs
        maxHeapify(A, largest)               # Continuer récursivement


def buildMaxHeap(A):
    """
    Transforme le tableau A en un tas maximum en organisant les éléments selon la propriété de tas.

    Parcourt les noeuds internes du tas (de H//2 à 1) et appelle maxHeapify sur chacun pour corriger le sous-tas.

    Args:
        A (list): Tableau d'entiers (1-indicé) à transformer en tas maximum.

    Returns:
        None: Modifie le tableau A sur place.
    """
    # Parcourir chaque noeud interne depuis le dernier parent vers la racine
    for i in range(H // 2, 0, -1):
        maxHeapify(A, i)


# Lecture de la taille du tas (nombre d'éléments)
H = int(input())

# Lecture des éléments du tas, insertion d'un zéro fictif à l'indice 0 pour simplifier les calculs d'indices (1-indicé)
A = [0] + list(map(int, input().split()))

# Construction du tas maximum à partir des éléments
buildMaxHeap(A)

# Suppression de l'élément fictif à l'indice 0 pour préparer l'affichage du résultat
A.pop(0)

# Affichage du tas maximum sous forme d'une chaîne d'entiers séparés par un espace
print(" " + " ".join([str(num) for num in A]))