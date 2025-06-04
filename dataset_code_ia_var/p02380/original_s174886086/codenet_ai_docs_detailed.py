import math
import sys

# Modification de la fonction d'entrée standard pour supprimer les retours à la ligne en fin de lecture.
input = sys.stdin.readline().rstrip

def calculate_triangle_properties(a: float, b: float, C_deg: float):
    """
    Calcule les propriétés d'un triangle à partir de deux côtés et de l'angle inclus.

    Args:
        a (float): Longueur du premier côté du triangle.
        b (float): Longueur du deuxième côté du triangle.
        C_deg (float): Mesure de l'angle inclus (en degrés) entre les deux côtés.

    Returns:
        tuple: Un triplet contenant :
            - S (float): L'aire du triangle.
            - L (float): Le périmètre du triangle.
            - h (float): La hauteur issue du côté de longueur 'a'.
    """

    # Conversion de l'angle donné de degrés à radians pour utilisation avec les fonctions trigonométriques
    C_rad = math.radians(C_deg)

    # Calcul de l'aire du triangle à l'aide de la formule S = 1/2 * a * b * sin(C)
    S = a * b * math.sin(C_rad) / 2

    # Calcul de la longueur du troisième côté à l'aide du théorème du cosinus
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C_rad))

    # Calcul du périmètre du triangle (somme des longueurs des trois côtés)
    L = a + b + c

    # Calcul de la hauteur issue du côté 'a', via la formule h = b * sin(C)
    h = b * math.sin(C_rad)

    return S, L, h

def main():
    """
    Point d'entrée principal du script.
    Lit les entrées, effectue les calculs et affiche les propriétés du triangle.
    """

    # Lecture d'une ligne d'entrée contenant les deux côtés et l'angle (séparés par des espaces)
    a_str, b_str, C_str = input().split()

    # Conversion des entrées en nombres flottants
    a = float(a_str)
    b = float(b_str)
    C = float(C_str)

    # Calcul des propriétés du triangle
    S, L, h = calculate_triangle_properties(a, b, C)

    # Affichage des résultats (aire, périmètre, hauteur)
    print(S)
    print(L)
    print(h)

if __name__ == "__main__":
    main()