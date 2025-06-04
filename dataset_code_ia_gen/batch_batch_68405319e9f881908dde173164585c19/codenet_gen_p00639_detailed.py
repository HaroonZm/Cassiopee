import math
import sys

def dot(u, v):
    # Produit scalaire de deux vecteurs 2D
    return u[0]*v[0] + u[1]*v[1]

def norm(v):
    # Norme euclidienne d'un vecteur 2D
    return math.sqrt(v[0]*v[0] + v[1]*v[1])

def reflect(v, n):
    # Réflexion du vecteur v par rapport à la normale n (v et n sont unitaires)
    # v' = v - 2*(v·n)*n
    vn = dot(v, n)
    return (v[0] - 2*vn*n[0], v[1] - 2*vn*n[1])

def solve(D, px, py, vx, vy):
    R = 1.0  # rayon du mur virtuel
    EPS = 1e-14  # epsilon petites erreurs flottantes

    pos = (px, py)
    vel = (vx, vy)

    dist_total = 0.0

    # On simule les déplacements par segment jusqu'à distance D
    # A chaque segment, on cherche l'intersection avec le cercle R=1
    # puis on calcule l'intersection avec l'origine
    # Si on touche l'origine on renvoie la distance
    # Si on dépasse D sans toucher, on renvoie impossible

    while dist_total <= D + EPS:
        # 1) On vérifie si on touche le centre (0,0) avant le mur (rayon 1)
        # La trajectoire : P(t) = pos + vel*t
        # -> distance du point à l'origine: ||pos + vel*t||=0 => chercher t
        # En fait on cherche s'il existe t>0 tel que P(t)=(0,0)
        # P(t)=(0,0) => pos + vel*t= (0,0) => t = -pos/vel (composantes)
        # mais on veut t unique, pos et vel sont 2D... sauf si vel nul? non

        # On cherche intersection paramétrique au point (0,0). Car la cible est un point,
        # on résout l'équation vectorielle pos + vel t=0 => on cherche un t ≥0 tel que les deux composantes nulles
        # ce n'est possible que si pos et vel sont colinéaires et de sens opposé.
        # On peut vérifier si le mouvement passe par l'origine en recherchant t:

        # pos + vel*t = (0,0) => deux équations:
        # px + vx * t =0
        # py + vy * t =0
        # Ces deux équations doivent être cohérentes pour un t unique ≥0.

        t1 = None
        if abs(vx) > EPS:
            t_x = -px / vx
        else:
            t_x = None
        if abs(vy) > EPS:
            t_y = -py / vy
        else:
            t_y = None

        t_hit = None
        if t_x is not None and t_y is not None:
            # les deux existent, vérifier s'ils sont approx égaux
            if abs(t_x - t_y) < 1e-14 and t_x >= -EPS:
                t_hit = t_x
        elif t_x is not None:
            # vy nul, alors py doit être nul aussi
            if abs(py) < 1e-14 and t_x >= -EPS:
                t_hit = t_x
        elif t_y is not None:
            # vx nul, alors px doit être nul aussi
            if abs(px) < 1e-14 and t_y >= -EPS:
                t_hit = t_y
        else:
            # vx et vy nuls, vitesse nulle donc pas de mouvement
            # si position différente de zéro, pas possible d'atteindre origine
            t_hit = None

        if t_hit is not None and t_hit > EPS:
            # La distance parcourue jusqu'au hit est |vel|*t_hit
            dist_to_hit = norm(vel)*t_hit
            if dist_total + dist_to_hit <= D + EPS:
                # on touche la cible avant l'épuisement de la portée
                return dist_total + dist_to_hit

        # 2) Sinon, chercher le temps t_intersect où la trajectoire touche le cercle de rayon R=1
        # pos=(px, py), vel=(vx, vy), R=1
        # ||pos + vel t||^2 = R^2
        # Equation quadratique:
        # (px + vx t)^2 + (py + vy t)^2 = 1^2
        # (vx^2 + vy^2) t^2 + 2(px vx + py vy) t + (px^2 + py^2 -1) = 0
        a = vel[0]*vel[0] + vel[1]*vel[1]
        b = 2*(pos[0]*vel[0] + pos[1]*vel[1])
        c = pos[0]*pos[0] + pos[1]*pos[1] - R*R

        discriminant = b*b - 4*a*c
        if discriminant < -EPS:
            # Pas d'intersection, trajectoire ne touche plus le cercle
            # On n'atteint donc pas la cible
            break
        discriminant = max(0.0, discriminant)

        sqrt_disc = math.sqrt(discriminant)

        t_candidates = []
        t_a = (-b - sqrt_disc) / (2*a)
        t_b = (-b + sqrt_disc) / (2*a)
        # On conserve t strictement positif, on cherche la plus petite positive
        for t_cand in [t_a, t_b]:
            if t_cand > EPS:
                t_candidates.append(t_cand)
        if not t_candidates:
            # Pas d'intersection future avec le cercle
            break
        t_wall = min(t_candidates)

        # 3) Vérifier que la distance parcourue sur ce segment ne dépasse pas D
        segment_dist = norm(vel)*t_wall
        if dist_total + segment_dist > D + EPS:
            # On dépasse la limite de distance sans toucher la cible
            break

        # 4) Avancer à la naissance collision avec le mur
        pos = (pos[0] + vel[0]*t_wall, pos[1] + vel[1]*t_wall)
        dist_total += segment_dist

        # 5) Calculer la normale au point d'impact sur le cercle (origine->pos)
        n = (pos[0]/R, pos[1]/R)  # vecteur unitaire normal extérieur

        # 6) Réfléchir la vitesse selon la normale
        v_len = norm(vel)
        v_normed = (vel[0]/v_len, vel[1]/v_len)
        v_reflected = reflect(v_normed, n)
        # Garder la même norme de vitesse
        vel = (v_reflected[0]*v_len, v_reflected[1]*v_len)

        # Petite protection anti-boucle infinie: si la vitesse est trop faible, on quitte
        if norm(vel) < 1e-12:
            break

        px, py = pos
        vx, vy = vel

    return None  # impossible de toucher

def main():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx >= len(input):
            break
        D = float(input[idx])
        idx += 1
        if D == 0:
            break
        px = float(input[idx])
        py = float(input[idx+1])
        vx = float(input[idx+2])
        vy = float(input[idx+3])
        idx += 4

        res = solve(D, px, py, vx, vy)
        if res is None:
            print("impossible")
        else:
            print(f"{res:.8f}")

if __name__ == "__main__":
    main()