import math

while True:
    x = int(input())
    h = int(input())
    if x == 0 and h == 0:
        break
    # calcul de la longueur de l'arête latérale de la pyramide
    a = math.sqrt(h**2 + (x/2)**2)
    # surface des 4 triangles latéraux
    lateral_area = 2 * x * a
    # surface du carré de base
    base_area = x**2
    # surface totale
    S = base_area + lateral_area
    print(f"{S:.6f}")