import math

def compute_number_of_squares(width, height, color_count):
    """
    Calcule le nombre de carrés minimaux nécessaires pour remplir un rectangle de
    dimensions données, chaque carré étant de la taille du PGCD des dimensions.
    Le résultat est multiplié par un facteur de couleurs.
    
    Args:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.
        color_count (int): Le facteur par lequel multiplier le nombre de carrés.
        
    Returns:
        int: Le résultat du calcul décrit ci-dessus.
    """
    # Calcule le PGCD de la largeur et de la hauteur pour trouver la plus grande taille de carré
    greatest_common_divisor = math.gcd(width, height)
    # Calcule le nombre de carrés nécessaires le long de toute la surface
    squares_count = (width * height) // (greatest_common_divisor ** 2)
    # Multiplie le résultat par le nombre de couleurs ou le facteur donné
    return color_count * squares_count

# Lecture des entrées utilisateur et conversion en entiers
W, H, C = map(int, input().split())

# Appel de la fonction avec les valeurs lues et affichage du résultat
print(compute_number_of_squares(W, H, C))