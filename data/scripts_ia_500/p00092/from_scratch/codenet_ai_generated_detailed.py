import sys

def max_square_without_marks(grid, n):
    """
    Cette fonction calcule la taille du plus grand carré ne contenant que des '.' (pas de '*')
    dans une grille n x n donnée.
    Elle utilise la programmation dynamique :
    dp[i][j] représente la longueur du plus grand carré dont le coin inférieur droit est en (i,j)
    """
    # dp est une matrice n x n initialisée à 0
    dp = [[0]*n for _ in range(n)]

    max_side = 0  # pour garder la taille maximale trouvée

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                if i == 0 or j == 0:
                    # première ligne ou première colonne, on peut seulement avoir un carré 1x1
                    dp[i][j] = 1
                else:
                    # taille minimale des carrés adjacents + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                # mise à jour de la taille maximale
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
            else:
                dp[i][j] = 0  # cell avec '*' ne peut pas faire partie d'un carré sans marquage
    return max_side

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        grid = [input().rstrip('\n') for _ in range(n)]
        # calcul de la taille du plus grand carré sans *
        result = max_square_without_marks(grid, n)
        print(result)

if __name__ == "__main__":
    main()