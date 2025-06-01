import sys

def area(x1, y1, x2, y2, x3, y3):
    """
    Calcule l'aire du triangle formé par les points (x1, y1), (x2, y2), (x3, y3)
    en utilisant la formule du produit vectoriel, ce qui donne 2 fois l'aire.
    On renvoie la valeur absolue divisée par 2.
    """
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
    """
    Détermine si le point P(xp, yp) est dans le triangle formé par A(x1, y1), B(x2, y2), C(x3, y3).

    Approche:
    On calcule l'aire du triangle ABC.
    On calcule les aires des triangles PBC, APC, et ABP.
    Si la somme des 3 petites aires est égale à l'aire du triangle ABC (avec une marge de tolérance),
    alors le point est à l'intérieur ou sur le bord du triangle.
    Sinon, il est à l'extérieur.

    La tolérance prend en compte les imprécisions liées aux nombres flottants.
    """
    # Aire du grand triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)
    # Aires des sous-triangles avec P
    A1 = area(xp, yp, x2, y2, x3, y3)
    A2 = area(x1, y1, xp, yp, x3, y3)
    A3 = area(x1, y1, x2, y2, xp, yp)

    # Tolérance pour comparer les aires en float (ex: 1e-9)
    epsilon = 1e-9
    # Somme des sous-aires
    somme = A1 + A2 + A3
    
    # Vérification de l'appartenance
    return abs(somme - A) <= epsilon

def main():
    """
    Lit les données standard jusqu'à EOF, pour chaque dataset vérifie si le point est dans le triangle,
    puis affiche "YES" ou "NO".
    """
    for line in sys.stdin:
        # On ignore les lignes vides ou avec moins de 8 éléments
        parts = line.strip().split()
        if len(parts) != 8:
            continue
        # Conversion des coordonnées en flottants
        x1, y1, x2, y2, x3, y3, xp, yp = map(float, parts)
        # Appel de la fonction de test
        if point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()