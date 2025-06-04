def calculate_trapezoid_area(a: int, b: int, h: int) -> int:
    """
    Calcule l'aire d'un trapèze étant donné les longueurs des deux bases et la hauteur.

    Args:
        a (int): La longueur de la première base du trapèze.
        b (int): La longueur de la deuxième base du trapèze.
        h (int): La hauteur du trapèze (distance perpendiculaire entre les bases).

    Returns:
        int: L'aire du trapèze, arrondie à l'entier inférieur si le résultat n'est pas entier.
    """
    # Additionne les deux bases du trapèze
    bases_sum = a + b
    # Multiplie la somme des bases par la hauteur
    product = bases_sum * h
    # Divise le résultat par 2 pour obtenir l'aire selon la formule de l'aire d'un trapèze
    area = product // 2
    return area

# Demande à l'utilisateur de saisir la longueur de la première base
a = int(input("Entrez la longueur de la première base : "))

# Demande à l'utilisateur de saisir la longueur de la deuxième base
b = int(input("Entrez la longueur de la deuxième base : "))

# Demande à l'utilisateur de saisir la hauteur du trapèze
h = int(input("Entrez la hauteur du trapèze : "))

# Calcule et affiche l'aire du trapèze avec les valeurs saisies
print(calculate_trapezoid_area(a, b, h))