import sys

def parse_input_line(line):
    """
    Convertit une ligne d'entrée en 8 flottants représentant les coordonnées
    des coins opposés de deux rectangles.

    Args:
        line (str): La ligne de texte contenant 8 valeurs séparées par des espaces.

    Returns:
        tuple: Un tuple de 8 flottants (xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2).
    """
    # Découpe, convertit en float et retourne les coordonnées
    return tuple(map(float, line.strip().split(' ')))

def rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
    """
    Détermine si deux rectangles s'intersectent ou se touchent.

    Les rectangles sont définis chacun par deux sommets opposés (coin inférieur-gauche et coin supérieur-droit).

    Args:
        xa1, ya1, xa2, ya2 (float): Coordonnées du premier rectangle.
        xb1, yb1, xb2, yb2 (float): Coordonnées du second rectangle.

    Returns:
        bool: True si les rectangles se chevauchent, False sinon.
    """
    # Normalise les coordonnées pour s'assurer d'avoir toujours le coin inférieur-gauche et supérieur-droit
    xa_min, xa_max = min(xa1, xa2), max(xa1, xa2)
    ya_min, ya_max = min(ya1, ya2), max(ya1, ya2)
    xb_min, xb_max = min(xb1, xb2), max(xb1, xb2)
    yb_min, yb_max = min(yb1, yb2), max(yb1, yb2)

    # Vérifie la superposition sur l'axe X
    x_overlap = not (xa_max < xb_min or xb_max < xa_min)
    # Vérifie la superposition sur l'axe Y
    y_overlap = not (ya_max < yb_min or yb_max < ya_min)

    return x_overlap and y_overlap

def main():
    """
    Parcourt les entrées standard ligne par ligne pour lire les coordonnées de deux rectangles,
    puis affiche "YES" s'ils se chevauchent, "NO" sinon.
    """
    # Lecture ligne par ligne de l'entrée standard
    for line in sys.stdin:
        # Extraction des coordonnées à partir de la ligne d'entrée
        xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = parse_input_line(line)
        # Utilisation de la fonction de test de recouvrement
        if rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
            print('YES')
        else:
            print('NO')

# Point d'entrée du script
if __name__ == '__main__':
    main()