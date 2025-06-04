def calculate_remaining_area(square_length: int, covered_area: int) -> int:
    """
    Calcule la surface restante après avoir soustrait une surface couverte d'un carré donné.

    Args:
        square_length (int): La longueur d'un côté du carré.
        covered_area (int): La surface qui est couverte à soustraire du total.

    Returns:
        int: La surface restante après soustraction.
    """
    # Calculer l'aire du carré à partir de la longueur de son côté
    total_area = square_length * square_length
    # Soustraire la surface couverte à l'aire totale
    remaining_area = total_area - covered_area
    # Retourner la surface restante
    return remaining_area

# Demander à l'utilisateur de saisir la longueur d'un côté du carré
N = int(input("Entrez la longueur d'un côté du carré (N) : "))

# Demander à l'utilisateur de saisir la surface couverte à soustraire
A = int(input("Entrez la surface couverte à soustraire (A) : "))

# Calculer et afficher la surface restante
result = calculate_remaining_area(N, A)
print(result)