import sys
import math

def can_place_balloon(r, w, needles):
    """
    Vérifie s'il est possible de placer une sphère de rayon r qui repose sur le sol (z=0)
    sans toucher les parois ni les aiguilles.
    
    Arguments:
    - r: rayon de la sphère
    - w: hauteur des murs de la boîte
    - needles: liste de tuples (x_i, y_i, h_i) pour chaque aiguille
    
    Retour:
    - True si placement possible, False sinon
    """
    # Si le ballon a un rayon supérieur à la hauteur des murs,
    # ou s'il va déborder des murs (car il doit être placé sur le sol,
    # son centre est donc en (cx, cy, r) et la sphère entière doit tenir)
    if r > w:
        return False
    
    # Le centre du ballon est donc à hauteur r au-dessus du sol
    # Sa projection dans le plan XY est le point (cx, cy), inconnu
    
    # Pour que la sphère ne touche pas les murs, le centre doit être
    # à au moins une distance r des bords carrés (0,0)-(100,100)
    # donc cx et cy dans [r, 100 - r]
    
    # Pour chaque aiguille, la distance verticale entre le centre du ballon (z=r)
    # et le sommet de l'aiguille (z = h_i) est |h_i - r|. La sphère a rayon r,
    # donc la distance horizontale entre centre ballon et aiguille doit être au moins
    # sqrt(r^2 - (h_i - r)^2), sinon la sphère empiète sur l'aiguille.
    # Si (h_i - r)^2 > r^2 => impossible à cause de la hauteur verticale
    
    # Méthode : sur une grille, on cherche si un point (cx, cy) existe avec
    # r <= cx <= 100-r, r <= cy <= 100-r et à respecter les contraintes.

    # Pour optimisation, on va discrétiser le domaine et faire un test.
    # n discrétisations suffisent pour 0.01 de précision.
    
    steps = 200  # 0.5 unité pour la grille
    delta = (100 - 2 * r) / steps
    if delta < 0:  # pas d'espace possible
        return False
    
    # On crée les listes possibles de positions du centre possible
    x_candidates = [r + i * delta for i in range(steps + 1)]
    y_candidates = x_candidates

    # Pour chaque point du centre, on vérifie les contraintes sur les aiguilles
    for cx in x_candidates:
        for cy in y_candidates:
            ok = True
            for (x_i, y_i, h_i) in needles:
                dz = abs(h_i - r)
                if dz > r:  # La sphère ne pourrait pas éviter l'aiguille en z
                    ok = False
                    break
                # distance horizontale minimale entre centre et aiguille :
                required_dist_xy = math.sqrt(r * r - dz * dz)
                dist_xy = math.hypot(cx - x_i, cy - y_i)
                if dist_xy < required_dist_xy - 1e-14:
                    # empiètement sur l'aiguille
                    ok = False
                    break
            if ok:
                return True
    return False

def solve():
    input = sys.stdin.read().strip().split()
    idx = 0
    results = []
    while True:
        if idx+1 >= len(input):
            break
        n = int(input[idx]); idx+=1
        w = int(input[idx]); idx+=1
        if n == 0 and w == 0:
            break
        needles = []
        for _ in range(n):
            x_i = int(input[idx]); idx+=1
            y_i = int(input[idx]); idx+=1
            h_i = int(input[idx]); idx+=1
            needles.append((x_i, y_i, h_i))

        # La borne supérieure est au maximum w car on ne peut pas dépasser
        # la hauteur des murs (sinon le ballon sort)
        # La borne inférieure est 0.
        low, high = 0.0, float(w)
        for _ in range(40):  # binaire résolution assez fine (1e-12)
            mid = (low + high) / 2
            if can_place_balloon(mid, w, needles):
                low = mid
            else:
                high = mid

        results.append(low)
    for r in results:
        print(f"{r:.5f}")

if __name__ == "__main__":
    solve()