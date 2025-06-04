from collections import defaultdict

def read_input():
    """
    Lit la taille de la séquence et les entiers depuis l'entrée standard.

    Returns:
        tuple: (N, A) où N est un entier (longueur) et A est une liste d'entiers.
    """
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def check_all_zeros(A):
    """
    Vérifie si tous les éléments de la liste A sont des zéros.

    Args:
        A (list): Liste d'entiers.

    Returns:
        bool: True si tous les éléments sont zéro, sinon False.
    """
    return all(a == 0 for a in A)

def build_position_dict(A):
    """
    Construit un dictionnaire qui mappe chaque valeur à la liste de ses indices dans A.

    Args:
        A (list): Liste d'entiers.

    Returns:
        defaultdict: Dictionnaire tel que position[a] contient les indices où l'on trouve a.
    """
    position = defaultdict(list)
    for i, a in enumerate(A):
        position[a].append(i)
    return position

def compute_answer(N, A, position):
    """
    Calcule la réponse maximale selon les règles de liens définis.

    Args:
        N (int): Taille de la liste A.
        A (list): Liste d'entiers.
        position (dict): Dictionnaire des positions pour chaque valeur distincte.

    Returns:
        int: La réponse maximale calculée.
    """
    ans = 0   # Réponse maximale
    use = 0   # Compteur du nombre de valeurs utilisées jusqu'à présent
    link = 0  # Compteur des "liens" selon des conditions sur les voisins

    # Iterate sur les valeurs distinctes de A, des plus grandes aux plus petites
    for a in sorted(set(A), reverse=True):
        use += len(position[a])
        for i in position[a]:
            # Si i > 0, vérifier si A[i] < A[i-1] pour ajouter un lien
            if i > 0 and A[i] < A[i - 1]:
                link += 1
            # Si i < N-1, vérifier si A[i] <= A[i+1] pour ajouter un lien
            if i < N - 1 and A[i] <= A[i + 1]:
                link += 1
        # Mettre à jour la réponse maximale
        ans = max(ans, use - link)
    return ans

def main():
    """
    Fonction principale qui orchestre la lecture des entrées,
    le calcul et l'affichage du résultat.
    """
    N, A = read_input()
    if check_all_zeros(A):
        print(0)
        return
    position = build_position_dict(A)
    result = compute_answer(N, A, position)
    print(result)

if __name__ == "__main__":
    main()