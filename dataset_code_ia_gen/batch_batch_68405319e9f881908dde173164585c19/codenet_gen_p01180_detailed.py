import sys
import math

# On définit une classe Circle pour stocker informations sur chaque cercle
class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

# Fonction pour calculer la distance entre deux cercles selon l'énoncé
def circles_distance(c1, c2):
    # Distance euclidienne entre les centres
    center_dist = math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)
    # Distance entre bords des cercles = distance des centres - somme des rayons,
    # toujours au moins 0 car les cercles ne se chevauchent pas
    return max(0.0, center_dist - (c1.r + c2.r))

# Algorithme "Closest pair" adapté aux cercles
# Fonction récursive principale qui cherche la plus petite distance entre cercles.
# circles_x est la liste des cercles triés par coordonnée x
# circles_y est la liste des cercles triés par coordonnée y
def closest_pair(circles_x, circles_y):
    n = len(circles_x)
    # Cas de base : on calcule la distance par force brute
    if n <= 3:
        min_d = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                dist = circles_distance(circles_x[i], circles_x[j])
                if dist < min_d:
                    min_d = dist
        return min_d

    # Diviser en deux moitiés
    mid = n // 2
    mid_x = circles_x[mid].x

    left_x = circles_x[:mid]
    right_x = circles_x[mid:]

    # Construction des listes circles_y pour chaque moitié
    left_y, right_y = [], []
    for c in circles_y:
        if c.x <= mid_x:
            left_y.append(c)
        else:
            right_y.append(c)

    # Recherche récursive dans les moitiés
    d_left = closest_pair(left_x, left_y)
    d_right = closest_pair(right_x, right_y)
    d = min(d_left, d_right)

    # Recherche dans la bande centrale ±d autour de la verticale mid_x
    # On cherche les cercles dont x est dans [mid_x - d, mid_x + d]
    strip = [c for c in circles_y if abs(c.x - mid_x) <= d]

    # On essaie toutes les paires dans strip qui sont proches en y (propriété connue)
    min_strip = d
    for i in range(len(strip)):
        # On compare avec les prochains cercles dans strip dont la coordonnée y est dans ±d
        j = i + 1
        while j < len(strip) and (strip[j].y - strip[i].y) <= d:
            dist = circles_distance(strip[i], strip[j])
            if dist < min_strip:
                min_strip = dist
            j += 1
    return min_strip

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N = line.strip()
        if N == '0':  # Fin des cas de test
            break
        N = int(N)
        circles = []
        for _ in range(N):
            r, x, y = map(float, input().split())
            circles.append(Circle(r, x, y))

        # On trie d'abord par x puis par y
        circles_x = sorted(circles, key=lambda c: c.x)
        circles_y = sorted(circles, key=lambda c: c.y)

        # Calcul de la distance minimale entre cercles
        result = closest_pair(circles_x, circles_y)

        # Affichage avec précision demandée (erreur ≤ 0.00001)
        print(f"{result:.5f}")

if __name__ == "__main__":
    main()