import math
from itertools import permutations

def angle_between_vectors(v1, v2):
    # Calcule l'angle en degrés entre deux vecteurs 2D v1 et v2
    # sans tenir compte du sens (on prend l'angle minimal entre les deux)
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    det = v1[0] * v2[1] - v1[1] * v2[0]  # Produit vectoriel 2D (déterminant)
    angle_rad = math.atan2(abs(det), dot)  # angle minimal en radians (angle positif dans [0, pi])
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def vector_from_to(p1, p2):
    # Retourne le vecteur (direction) normalisé allant de p1 à p2
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    norm = math.hypot(dx, dy)
    return (dx / norm, dy / norm)

def solve():
    N = int(input())
    shops = [tuple(map(int, input().split())) for _ in range(N)]
    home = (0, 0)

    # Satake commence à la maison, orienté dans la direction (1,0)
    initial_dir = (1, 0)

    min_total_rotation = float('inf')

    # On essaye toutes les permutations de l'ordre des magasins
    for order in permutations(shops):
        total_rotation = 0.0
        current_pos = home
        current_dir = initial_dir

        # Parcours: maison -> magasin1 -> ... -> magasinN -> maison
        for shop in order:
            # Calcul du vecteur direction du déplacement
            move_dir = vector_from_to(current_pos, shop)
            # Calcul de l'angle entre la direction actuelle et la nouvelle direction
            angle = angle_between_vectors(current_dir, move_dir)
            total_rotation += angle  # On ajoute cet angle à la rotation totale

            # Avance vers le magasin: direction et position mises à jour
            current_pos = shop
            current_dir = move_dir

        # Retour vers la maison
        move_dir = vector_from_to(current_pos, home)
        angle = angle_between_vectors(current_dir, move_dir)
        total_rotation += angle

        # Mise à jour du minimum
        if total_rotation < min_total_rotation:
            min_total_rotation = total_rotation

    # Affichage avec une précision suffisante
    print(f"{min_total_rotation:.9f}")

if __name__ == "__main__":
    solve()