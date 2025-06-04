import sys

def reflect_point(p1, p2, p):
    # Calculer le vecteur p1p2
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # Calculer le vecteur p1p
    px = p[0] - p1[0]
    py = p[1] - p1[1]

    # Calculer la projection scalaire de p1p sur p1p2
    dot = px * dx + py * dy
    len_sq = dx * dx + dy * dy
    proj_len = dot / len_sq

    # Trouver le point de projection r sur la ligne p1p2
    rx = p1[0] + proj_len * dx
    ry = p1[1] + proj_len * dy

    # Le point réfléchi x = 2*r - p
    x_reflect = 2 * rx - p[0]
    y_reflect = 2 * ry - p[1]

    return x_reflect, y_reflect

def main():
    input = sys.stdin.readline

    # Lecture des points p1, p2
    x1, y1, x2, y2 = map(int, input().split())
    p1 = (x1, y1)
    p2 = (x2, y2)

    # Nombre de requêtes q
    q = int(input())

    for _ in range(q):
        xi, yi = map(int, input().split())
        p = (xi, yi)

        rx, ry = reflect_point(p1, p2, p)

        # Affichage avec 10 décimales
        print(f"{rx:.10f} {ry:.10f}")

if __name__ == "__main__":
    main()