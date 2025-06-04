import sys
import math

def dist_point_to_segment(px, py, x1, y1, x2, y2):
    """Calcule la distance minimale entre un point (px, py) et un segment défini par (x1, y1)-(x2, y2)."""
    # Vecteur du segment
    vx = x2 - x1
    vy = y2 - y1
    # Vecteur du point vers le début du segment
    wx = px - x1
    wy = py - y1
    # Calcul du paramètre t pour la projection du point sur le segment
    c1 = vx * wx + vy * wy
    c2 = vx * vx + vy * vy
    if c2 == 0:
        # Les deux points de segment sont confondus
        return math.hypot(px - x1, py - y1)
    t = c1 / c2
    if t < 0:
        # Projection avant le segment
        return math.hypot(px - x1, py - y1)
    elif t > 1:
        # Projection après le segment
        return math.hypot(px - x2, py - y2)
    else:
        # Projection sur le segment
        projx = x1 + t * vx
        projy = y1 + t * vy
        return math.hypot(px - projx, py - projy)

def is_safe_point(px, py, beams, radius):
    """
    Vérifie si la machine placée en (px, py) ne chevauche aucun rayon laser.
    beams : liste de tuples (x1, y1, x2, y2, thickness)
    radius : rayon de la machine
    Le chevauchement se produit si la distance machine-laser est inférieure à radius
      ou, vu la largeur de laser, s'il y a un overlap des deux disques (machine) et
      bande laser (ligne avec épaisseur).
    """
    for (x1, y1, x2, y2, thickness) in beams:
        # Distance minimale entre machine et segment laser
        dist = dist_point_to_segment(px, py, x1, y1, x2, y2)
        # La moitié de l'épaisseur de laser
        half_thick = thickness / 2.0
        # Si les deux disques se chevauchent (rayon machine + demi épaisseur laser > distance)
        if dist <= radius + half_thick - 1e-12:
            return False
    return True

def solve():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx + 4 > len(input):
            break
        W, H, N, R = map(int, input[idx:idx+4])
        idx += 4
        if W == 0 and H == 0 and N == 0 and R == 0:
            # Fin de l'entrée
            break

        beams = []
        for _ in range(N):
            # Chaque ligne: x1 y1 x2 y2 thickness
            x1, y1, x2, y2, t = map(int, input[idx:idx+5])
            idx += 5
            beams.append((x1, y1, x2, y2, t))

        # Manuel pour résoudre le problème:
        # Nous voulons savoir s'il existe au moins un point (x,y) dans [R, W-R] x [R, H-R]
        # qui ne chevauche aucun rayon laser.
        # La machine étant circulaire de rayon R, ses centres valides sont dans cette zone
        # car le disque doit être totalement dans la fenêtre.
        #
        # On ne peut pas tester tous les points car continu.
        # Approche discrète:
        # - On échantillonne la zone avec une grille assez fine (par exemple pas plus gros que R/2)
        #   car le rayon est la distance critique.
        # - Pour chaque point, on teste si safe.
        #
        # Si on trouve un point safe, on imprime "Yes", sinon "No".
        #
        # Cette méthode est acceptable compte tenu des contraintes: 
        #   W ≤ 640, H ≤ 480, N ≤ 100, ce qui donne un maximum de ~ (640/ R/2) * (480/ R/2) points.
        #
        # Alternative serait de tester la géométrie exacte mais complexe.

        # Le pas d'échantillonnage: on choisit R/2 ou 1 pixel minimum pour couvrir correctement.
        step = max(R / 2.0, 1.0)
        safe_found = False
        # Parcours dans la zone autorisée (centre machine)
        y = R
        while y <= H - R and not safe_found:
            x = R
            while x <= W - R and not safe_found:
                if is_safe_point(x, y, beams, R):
                    safe_found = True
                x += step
            y += step

        print("Yes" if safe_found else "No")

if __name__ == "__main__":
    solve()