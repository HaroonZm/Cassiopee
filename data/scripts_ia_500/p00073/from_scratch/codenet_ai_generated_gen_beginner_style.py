import math

while True:
    x = int(input())
    h = int(input())
    if x == 0 and h == 0:
        break
    # coté de la base carrée
    # hauteur de la pyramide
    # calculette la surface
    # surface base
    base_area = x * x
    # surface des 4 triangles
    # longueur du coté du triangle
    # hauteur slant = racine(h² + (x/2)²)
    slant_height = math.sqrt(h*h + (x/2)*(x/2))
    triangle_area = (x * slant_height) / 2
    side_area = 4 * triangle_area
    surface_area = base_area + side_area
    print(surface_area)