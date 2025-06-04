import sys

def read_bingo_grid():
    """
    Lit une grille 3x3 pour le bingo à partir de l'entrée standard.
    Chaque ligne doit contenir trois entiers séparés par des espaces.

    Returns:
        list[list[int]]: La grille 3x3 représentée sous forme de liste de listes d'entiers.
    """
    return [list(map(int, input().split())) for _ in range(3)]

def read_drawn_numbers():
    """
    Lit le nombre total de numéros tirés, puis lit chacun des numéros tirés.

    Returns:
        list[int]: Liste des numéros tirés.
    """
    N = int(input())
    return [int(input()) for _ in range(N)]

def mark_drawn_numbers(bingo_grid, drawn_numbers):
    """
    Marque les cases de la grille dont la valeur correspond à un numéro tiré.

    Args:
        bingo_grid (list[list[int]]): Grille du bingo 3x3 avec les valeurs initiales.
        drawn_numbers (list[int]): Liste des numéros tirés.

    Returns:
        list[list[bool]]: Grille 3x3 de valeurs booléennes indiquant les cases marquées.
    """
    marked = [[False for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if bingo_grid[i][j] in drawn_numbers:
                marked[i][j] = True
    return marked

def check_bingo(marked):
    """
    Vérifie si la grille marquée contient une ligne, une colonne ou une diagonale complète.

    Args:
        marked (list[list[bool]]): Grille 3x3 de valeurs booléennes indiquant les cases marquées.

    Returns:
        bool: True si une ligne, une colonne ou une diagonale est complètement marquée, False sinon.
    """
    # Vérification des lignes et des colonnes
    for i in range(3):
        # Vérifie la i-ème colonne
        if marked[0][i] and marked[1][i] and marked[2][i]:
            return True
        # Vérifie la i-ème ligne
        if marked[i][0] and marked[i][1] and marked[i][2]:
            return True

    # Vérifie la diagonale principale
    if marked[0][0] and marked[1][1] and marked[2][2]:
        return True

    # Vérifie la diagonale secondaire
    if marked[0][2] and marked[1][1] and marked[2][0]:
        return True

    return False

def main():
    """
    Fonction principale qui gère la logique du jeu de Bingo:
    - Lecture de la grille
    - Lecture des numéros tirés
    - Marquage des numéros dans la grille
    - Vérification de l'état de victoire
    Affiche "Yes" si une ligne, colonne ou diagonale complète est marquée, sinon "No".
    """
    bingo_grid = read_bingo_grid()
    drawn_numbers = read_drawn_numbers()
    marked = mark_drawn_numbers(bingo_grid, drawn_numbers)
    if check_bingo(marked):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()