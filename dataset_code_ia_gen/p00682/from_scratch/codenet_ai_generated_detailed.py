# Cette solution utilise la formule du polygone de Gauss (Shoelace formula)
# pour calculer l'aire d'un polygone défini par ses sommets.
# La formule est adaptée aux polygones simples, qu'ils soient convexes ou concaves.
# Les sommets sont donnés dans l'ordre de visite (ici dans le sens horaire).

def polygon_area(points):
    """
    Calcule l'aire d'un polygone donné par une liste de points.
    points : liste de tuples (x, y) des sommets du polygone dans l'ordre.
    Retourne l'aire en valeur flottante.
    """
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # Le point suivant, avec retour au premier
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def main():
    import sys
    sequence_number = 1
    for line in sys.stdin:
        n = line.strip()
        if not n:
            continue
        n = int(n)
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            points.append((x, y))
        area = polygon_area(points)
        # Affiche le numéro de la séquence et l'aire avec un chiffre après la virgule
        print(f"{sequence_number} {area:.1f}")
        sequence_number += 1

if __name__ == "__main__":
    main()