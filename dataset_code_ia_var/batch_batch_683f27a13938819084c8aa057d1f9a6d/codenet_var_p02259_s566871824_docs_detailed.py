def bubbleSort(A, N):
    """
    Effectue le tri à bulles (Bubble Sort) sur une liste.

    Args:
        A (list): La liste à trier, contenant N éléments. Les éléments sont comparés et triés en place.
        N (int): Le nombre d'éléments dans la liste A.

    Affiche:
        La liste triée, séparée par des espaces, puis le nombre total d'échanges effectués lors du tri.

    Description:
        Cette fonction utilise l'algorithme du tri à bulles pour trier la liste fournie en place.
        À chaque passage dans la liste, elle compare chaque paire d'éléments adjacents et les échange si nécessaire.
        Le processus se répète jusqu'à ce qu'aucun échange ne soit effectué lors d'un passage complet (la liste est alors triée).
    """
    flag = 1  # Variable pour indiquer si un échange a été effectué lors du dernier passage. 1 signifie "oui"
    count_swaps = 0  # Compteur du nombre total d'échanges effectués

    while flag == 1:  # Répéter tant qu'il y a eu au moins un échange lors du dernier passage
        flag = 0  # On suppose au départ qu'aucun échange ne sera nécessaire (la liste pourrait déjà être triée)
        # Parcours la liste de la fin vers le début (hors premier élément)
        for j in range(N - 1, 0, -1):
            # Compare chaque élément avec son précédent
            if A[j] < A[j - 1]:
                # Si l'ordre est incorrect, échange les deux éléments
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = 1  # Indique qu'un échange a été effectué
                count_swaps += 1  # Incrémente le compteur d'échanges

    # Affiche la liste triée, les éléments étant séparés par un espace
    print(*A)
    # Affiche le nombre total d'échanges effectués
    print(count_swaps)

def main():
    """
    Point d'entrée du programme.
    Lit les entrées utilisateur, prépare les données, et lance le tri à bulles.
    """
    N = int(input())  # Lit le nombre d'éléments à trier
    A = list(map(int, input().split()))  # Lit les éléments à trier sous forme de liste d'entiers

    bubbleSort(A, N)  # Applique le tri à bulles sur la liste saisie

if __name__ == "__main__":
    main()