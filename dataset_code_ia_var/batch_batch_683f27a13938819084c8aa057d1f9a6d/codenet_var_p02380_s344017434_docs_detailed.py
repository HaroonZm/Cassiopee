import sys
import math

def read_input():
    """
    Lit les entrées depuis l'entrée standard et retourne les valeurs sous forme d'entiers.
    
    Retour:
        tuple: Trois entiers correspondant à la longueur des côtés a, b et l'angle (en degrés) compris entre eux.
    """
    # Lire la ligne de l'entrée standard, enlever les espaces superflus et convertir les valeurs en entiers
    a, b, angle = map(int, sys.stdin.read().strip().split())
    return a, b, angle

def compute_third_side(a, b, angle):
    """
    Calcule la longueur du troisième côté d'un triangle à l'aide de la loi des cosinus.
    
    Args:
        a (int or float): Longueur du premier côté.
        b (int or float): Longueur du deuxième côté.
        angle (int or float): Angle compris entre les deux côtés (en degrés).
        
    Retour:
        float: Longueur du troisième côté.
    """
    # Convertir l'angle en radians pour l'utiliser avec math.cos
    rad = math.radians(angle)
    # Appliquer la loi des cosinus pour trouver le troisième côté
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(rad))
    return c

def compute_perimeter(a, b, c):
    """
    Calcule le périmètre du triangle.
    
    Args:
        a (float): Longueur du premier côté.
        b (float): Longueur du deuxième côté.
        c (float): Longueur du troisième côté.
    
    Retour:
        float: Périmètre du triangle.
    """
    # Additionner les longueurs des trois côtés
    return a + b + c

def compute_area(a, b, c):
    """
    Calcule l'aire d'un triangle en utilisant la formule de Héron.

    Args:
        a (float): Longueur du premier côté.
        b (float): Longueur du deuxième côté.
        c (float): Longueur du troisième côté.

    Retour:
        float: Aire du triangle.
    """
    # Calculer le demi-périmètre
    s = (a + b + c) / 2
    # Appliquer la formule de Héron
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def compute_height_from_side(area, base):
    """
    Calcule la hauteur du triangle correspondant à la base donnée.

    Args:
        area (float): Aire du triangle.
        base (float): Longueur de la base.

    Retour:
        float: Hauteur correspondant à la base.
    """
    # La hauteur est donnée par 2 * aire / base
    return (2 * area) / base

def format_and_print_results(area, perimeter, height):
    """
    Affiche les résultats demandés avec un format de 8 décimales.

    Args:
        area (float): Aire du triangle.
        perimeter (float): Périmètre du triangle.
        height (float): Hauteur du triangle.
    """
    # Itérer sur chaque valeur et afficher avec 8 décimales de précision
    for val in (area, perimeter, height):
        print('{0:.8f}'.format(val))

def main():
    """
    Fonction principale qui orchestre la lecture des entrées, les calculs et l'affichage des résultats.
    """
    # Lecture des entrées
    a, b, angle = read_input()
    # Calcul de la longueur du troisième côté
    c = compute_third_side(a, b, angle)
    # Calcul du périmètre
    perimeter = compute_perimeter(a, b, c)
    # Calcul de l'aire
    area = compute_area(a, b, c)
    # Calcul de la hauteur par rapport au côté a
    height = compute_height_from_side(area, a)
    # Affichage des résultats
    format_and_print_results(area, perimeter, height)

if __name__ == "__main__":
    main()