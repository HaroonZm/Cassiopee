import math

def calculate_triangle_area(a, b, c):
    """
    Calcule l'aire d'un triangle à partir de deux côtés et de l'angle inclus.

    Args:
        a (int or float): Longueur du premier côté du triangle.
        b (int or float): Longueur du deuxième côté du triangle.
        c (int or float): Mesure de l'angle (en degrés) entre les côtés a et b.

    Returns:
        float: Aire du triangle.
    """
    # Conversion de l'angle de degrés en radians pour la fonction math.sin
    angle_rad = math.radians(c)
    # Formule de l'aire d'un triangle à partir de deux côtés et l'angle inclus
    area = a * b * math.sin(angle_rad) / 2
    return area

def calculate_triangle_perimeter(a, b, c):
    """
    Calcule le périmètre du triangle donné ses côtés a, b et l'angle inclus c.

    Args:
        a (int or float): Longueur du premier côté du triangle.
        b (int or float): Longueur du deuxième côté du triangle.
        c (int or float): Mesure de l'angle (en degrés) entre les côtés a et b.

    Returns:
        float: Périmètre du triangle.
    """
    # Conversion de l'angle de degrés en radians
    angle_rad = math.radians(c)
    # Application de la loi des cosinus pour calculer la longueur du troisième côté
    side3_squared = (a - b * math.cos(angle_rad))**2 + (b * math.sin(angle_rad))**2
    side3 = math.sqrt(side3_squared)
    # Calcul du périmètre en sommant les longueurs des trois côtés
    perimeter = a + b + side3
    return perimeter

def calculate_triangle_height(b, c):
    """
    Calcule la hauteur du triangle par rapport au côté a, 
    étant donné la longueur du côté b et l'angle inclus c.

    Args:
        b (int or float): Longueur du deuxième côté du triangle.
        c (int or float): Mesure de l'angle (en degrés) entre les côtés a et b.

    Returns:
        float: Hauteur correspondante au côté a.
    """
    # Conversion de l'angle de degrés en radians
    angle_rad = math.radians(c)
    # Calcul de la hauteur avec la formule : hauteur = b * sin(angle)
    height = b * math.sin(angle_rad)
    return height

if __name__ == "__main__":
    # Lecture des entrées utilisateur : valeurs de a, b et c séparées par des espaces
    a, b, c = [int(x) for x in input().split()]

    # Calcul de l'aire du triangle
    s = calculate_triangle_area(a, b, c)
    # Calcul du périmètre du triangle
    l = calculate_triangle_perimeter(a, b, c)
    # Calcul de la hauteur associée au côté a
    h = calculate_triangle_height(b, c)

    # Affichage des résultats
    print(s)
    print(l)
    print(h)