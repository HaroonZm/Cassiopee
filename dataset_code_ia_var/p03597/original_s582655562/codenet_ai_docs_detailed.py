def calculate_bichrome_cells(square_size: int, black_cells: int) -> int:
    """
    Calcule le nombre de cases bicolores restantes dans un carré de taille donnée après soustraction des cases noires.

    Args:
        square_size (int): La taille du côté du carré (le carré est de dimensions square_size x square_size).
        black_cells (int): Le nombre de cases noires à soustraire.

    Returns:
        int: Le nombre de cases restantes après soustraction.
    """
    # Calcul du total de cases dans le carré
    total_cells = square_size ** 2

    # Calcul du nombre de cases bicolores restantes
    bichrome_cells = total_cells - black_cells

    return bichrome_cells

# Lecture du côté du carré depuis l'entrée standard
n = int(input())  # La taille du côté du carré

# Lecture du nombre de cases noires depuis l'entrée standard
k = int(input())  # Le nombre de cases noires à soustraire

# Calcul et affichage du résultat
print(calculate_bichrome_cells(n, k))