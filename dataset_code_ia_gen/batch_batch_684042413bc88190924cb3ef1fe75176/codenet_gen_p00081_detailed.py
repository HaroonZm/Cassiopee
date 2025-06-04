import sys

def reflect_point_across_line(x1, y1, x2, y2, xq, yq):
    """
    Calcule la réflexion du point Q par rapport à la droite passant par P1(x1,y1) et P2(x2,y2).
    
    Approche :
    - La droite est définie par les points P1 et P2.
    - On calcule la projection orthogonale du point Q sur la droite, appelons-la M.
    - Le point réfléchi R est tel que M est le milieu de Q et R.
    - Formules :
      * vecteur u = (x2-x1, y2-y1)
      * paramètre t pour la projection : t = ((xq - x1)*u_x + (yq - y1)*u_y) / (norme_u^2)
      * M = (x1 + t*u_x, y1 + t*u_y)
      * R = (2*M_x - xq, 2*M_y - yq)
    """
    ux = x2 - x1
    uy = y2 - y1
    norm_u_sq = ux*ux + uy*uy

    # Calcul du paramètre t pour la projection orthogonale
    t = ((xq - x1)*ux + (yq - y1)*uy) / norm_u_sq

    # Coordonnées du point projeté M
    mx = x1 + t * ux
    my = y1 + t * uy

    # Coordonnées du point réfléchi R
    rx = 2 * mx - xq
    ry = 2 * my - yq

    return rx, ry

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Lecture des valeurs en supprimant les espaces et séparant par ","
        parts = line.split(',')
        if len(parts) != 6:
            continue
        try:
            x1, y1, x2, y2, xq, yq = map(float, parts)
        except ValueError:
            continue

        rx, ry = reflect_point_across_line(x1, y1, x2, y2, xq, yq)

        # Affichage avec six décimales, tolérance 0.0001 acceptée
        print(f"{rx:.6f} {ry:.6f}")

if __name__ == "__main__":
    main()