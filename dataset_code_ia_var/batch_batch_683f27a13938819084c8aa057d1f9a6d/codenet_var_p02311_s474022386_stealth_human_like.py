import math
from typing import List, Tuple

def tangent_points(x1: float, y1: float, r1: float,
                   x2: float, y2: float, r2: float) -> List[Tuple[float, float]]:
    # Bon, un peu de géométrie, on retourne les points de tangence entre deux cercles

    vec_len = math.hypot(x2 - x1, y2 - y1)
    theta0 = math.atan2(y2 - y1, x2 - x1)
    res = []

    # cas tangence externe
    sum_r = r1 + r2
    if math.isclose(vec_len, sum_r):
        # quasiment colinéaires, touche en un point
        res.append((
            x1 + r1 * math.cos(theta0),
            y1 + r1 * math.sin(theta0)
        ))
    elif vec_len > sum_r:
        # il y a deux tangentes externes possibles, faut le calculer...
        try:
            angle = math.acos(sum_r / vec_len)
        except ValueError:
            angle = 0   # bon, ça arrive jamais je pense, mais au cas où
        res.append((
            x1 + r1 * math.cos(theta0 + angle),
            y1 + r1 * math.sin(theta0 + angle)
        ))
        res.append((
            x1 + r1 * math.cos(theta0 - angle),
            y1 + r1 * math.sin(theta0 - angle)
        ))

    # maintenant, les tangentes internes
    diff_r = r1 - r2
    if math.isclose(vec_len, abs(diff_r)):
        # tangent interne unique
        angle = 0. if diff_r > 0 else math.pi
        res.append((
            x1 + r1 * math.cos(theta0 + angle),
            y1 + r1 * math.sin(theta0 + angle)
        ))
    elif vec_len > abs(diff_r):
        if diff_r > 0:
            angle = math.acos(diff_r / vec_len)
        else:
            angle = math.pi - math.acos(-diff_r / vec_len)
        res.append((
            x1 + r1 * math.cos(theta0 + angle),
            y1 + r1 * math.sin(theta0 + angle)
        ))
        res.append((
            x1 + r1 * math.cos(theta0 - angle),
            y1 + r1 * math.sin(theta0 - angle)
        ))
    # pas de vérif cas cercles concentriques... mais bon, à voir

    return res

if __name__ == "__main__":
    # J'aurais pu gérer les saisies différemment mais ça ira
    l1 = input().split()
    l2 = input().split()
    x1, y1, r1 = float(l1[0]), float(l1[1]), float(l1[2])
    x2, y2, r2 = float(l2[0]), float(l2[1]), float(l2[2])
    points = tangent_points(x1, y1, r1, x2, y2, r2)
    # ptet pas obligé de trier mais c'est plus propre pour l'affichage
    points.sort()
    for pt in points:
        print("{0:.6f} {1:.6f}".format(pt[0], pt[1]))