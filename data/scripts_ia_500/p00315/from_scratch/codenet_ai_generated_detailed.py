import sys
input = sys.stdin.readline

def is_symmetric(matrix, n):
    """
    Vérifie si une matrice n x n est à la fois symétrique verticalement et horizontalement.
    Symétrie verticale: la ligne i doit être égale à la ligne n-1-i
    Symétrie horizontale: pour chaque ligne, l'élément j doit être égal à l'élément n-1-j
    """
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n - 1 - i][j]:  # vertical mirror check
                return False
            if matrix[i][j] != matrix[i][n - 1 - j]:  # horizontal mirror check
                return False
    return True

def main():
    # Lecture du nombre de coasters C et la taille N (N est pair)
    C, N = map(int, input().split())
    # Lecture de la première image : matrice N x N
    matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

    count_symmetric = 0

    # Vérifier la première image
    if is_symmetric(matrix, N):
        count_symmetric += 1

    # Pour chaque image suivante, appliquer les différences à partir de l'image précédente
    for _ in range(C - 1):
        D = int(input())  # nombre de pixels modifiés
        for __ in range(D):
            r, c = map(int, input().split())
            # Inverser la valeur du pixel modifié (0 <-> 1)
            matrix[r-1][c-1] = 1 - matrix[r-1][c-1]

        # Vérifier la symétrie de la nouvelle image
        if is_symmetric(matrix, N):
            count_symmetric += 1

    # Afficher le nombre d'images satisfaisant la symétrie verticale et horizontale
    print(count_symmetric)

if __name__ == "__main__":
    main()