import sys
import math
import collections

def read_board():
    """
    Lit une grille 3x3 depuis l'entrée standard et la stocke dans une liste à une dimension.

    Returns:
        list: Liste de 9 entiers représentant la grille ligne par ligne.
    """
    # Chaque ligne est lue séparément, puis les entiers sont ajoutés à la liste 'a'
    a1, a2, a3 = map(int, input().split())
    a4, a5, a6 = map(int, input().split())
    a7, a8, a9 = map(int, input().split())
    return [a1, a2, a3, a4, a5, a6, a7, a8, a9]

def mark_called_numbers(board, num_called, called_numbers):
    """
    Marque les numéros appelés sur la grille.

    Args:
        board (list): Liste des 9 entiers de la grille.
        num_called (int): Nombre total de numéros appelés.
        called_numbers (list): Liste des entiers appelés.

    Returns:
        list: Liste binaire de taille 9, où 1 indique que l'élément correspondant a été appelé.
    """
    # Initialise la liste de marqueurs à 0 pour chaque position 
    marked = [0 for _ in range(9)]
    # Pour chaque numéro appelé, si il existe dans la grille, on met 1 à la position correspondante
    for b in called_numbers:
        for j in range(9):
            if board[j] == b:
                marked[j] = 1
    return marked

def is_bingo(marked):
    """
    Vérifie si un bingo a été réalisé (une ligne, colonne ou diagonale est entièrement marquée).

    Args:
        marked (list): Liste binaire de taille 9 indiquant les positions cochées.

    Returns:
        bool: True si une ligne, une colonne ou une diagonale complète est marquée, False sinon.
    """
    # Liste des index de positions représentant les lignes, colonnes et diagonales de la grille
    win_patterns = [
        [0, 1, 2],  # première ligne
        [3, 4, 5],  # deuxième ligne
        [6, 7, 8],  # troisième ligne
        [0, 3, 6],  # première colonne
        [1, 4, 7],  # deuxième colonne
        [2, 5, 8],  # troisième colonne
        [0, 4, 8],  # diagonale principale
        [2, 4, 6]   # diagonale inverse
    ]
    # Vérifie chaque motif de victoire
    for pattern in win_patterns:
        if sum([marked[i] for i in pattern]) == 3:
            return True
    return False

def main():
    """
    Fonction principale orchestrant la lecture de la grille, la prise en compte des numéros appelés 
    et la vérification du bingo. Affiche "Yes" si bingo, "No" sinon.
    """
    # Lecture de la grille de bingo
    board = read_board()
    # Lecture du nombre de numéros appelés
    n = int(input())
    # Lecture des numéros appelés
    called_numbers = []
    for _ in range(n):
        called_numbers.append(int(input()))
    # Marquer les cases du board correspondant aux nombres appelés
    marked = mark_called_numbers(board, n, called_numbers)
    # Déterminer s'il y a un bingo
    if is_bingo(marked):
        print("Yes")
        sys.exit()
    else:
        print("No")

if __name__ == "__main__":
    main()