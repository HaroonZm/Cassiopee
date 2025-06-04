import sys
import math

# On cherche le dernier instant t où le disque représentant le soleil est entièrement couvert par les silhouettes et la zone y ≤ 0.
# Le soleil est un cercle de centre C(t) = (0, -r + t) et rayon r, avec t≥0.

# Approche :
# - Le soleil monte verticalement à vitesse 1 à partir de (0, -r) à t=0.
# - La zone sous l'horizon (y ≤ 0) bloque le soleil partiellement : dès que la partie inférieure du disque dépasse y=0, elle peut être non couverte.
# - Les silhouettes sont des rectangles alignés à l'horizon, de base y=0, hauteur h_i, et couvrent un intervalle [x_li, x_ri].
# - Pour que le soleil soit couvert à l'instant t, TOUTE la zone du disque doit être couverte par l'union des silhouettes et y ≤ 0.
# - On vérifie cela par une méthode basée sur les "fentes" horizontales du cercle : à chaque y dans [y_center - r, y_center + r], on calcule l'intervalle horizontal du cercle, et on vérifie s'il est inclus dans l'union des silhouettes couvrant ce y.
# - Si on trouve une y où cet intervalle n'est pas inclus dans les silhouettes, le soleil n'est pas couvert.
# - On utilise la recherche binaire sur t : si couvert, on peut augmenter t, sinon diminuer.
# - On cherche la borne maximale t≥0 avec couverture.

def merge_intervals(intervals):
    # Fusionne une liste d'intervalles (triés par début), le résultat est une liste d'intervalles non-chevauchants
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for s,e in intervals[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e:
            # chevauchement, fusion
            merged[-1] = (last_s, max(last_e,e))
        else:
            merged.append((s,e))
    return merged

def is_covered_at_y(y, left_intervals):
    # left_intervals : liste d'intervalles sur l'axe x qui couvrent y
    # La question : est-ce que la totalité de l'intervalle du soleil en y est couvert ?
    # Ici on considère la projection horizontale du soleil en y
    
    # retourne True si l'intervalle du soleil en y est couvert par left_intervals, false sinon
    
    # On prend les intervalles couvrant y, on les fusionne, on vérifie si la portion du cercle est incluse
    
    left_intervals_merged = merge_intervals(left_intervals)
    # On veut couvrir [sun_x_left, sun_x_right]
    return left_intervals_merged

def sun_interval_at_y(y, cy, r):
    # Donne l'intervalle horizontal du soleil à l'altitude y, càd la projection horizontale du cercle
    # si y est dans le disque, sinon None
    dy = y - cy
    if abs(dy) > r:
        return None
    dx = math.sqrt(r*r - dy*dy)
    return (-dx, dx)

def silhouettes_coverage_at_y(y, silhouettes):
    # renvoie la liste d'intervalles [x_li,x_ri] des silhouettes couvrant la verticale y
    # on ne prend que les silhouettes avec h_i >= y
    if y < 0:
        # tout le bas est couvert (y≤0)
        # donc zone infinie pour x en bas; mais on le gère dans la fonction de test
        return [(-math.inf, math.inf)]
    intervals = []
    for x_li, x_ri, h_i in silhouettes:
        if h_i >= y:
            intervals.append((x_li, x_ri))
    return intervals

def is_sun_covered(t, r, silhouettes):
    # vérifie si le soleil est couvert au temps t
    # centre du soleil : (0, -r + t)
    cy = -r + t
    # le disque est entre y_min = cy - r et y_max = cy + r
    # pour y dans cet intervalle, on calcule l'intervalle horizontal du soleil et on vérifie qu'il est couvert
    
    y_min = cy - r
    y_max = cy + r
    
    # On échantillonne y pour vérifier couverture
    # plutôt que d'échantillonner assez fin, on fera un balayage en utilisant les hauteurs des silhouettes et les bords du cercle
    # mais comme r ≤ 20, on peut tester sur un pas fin (ex: 0.005) pour précision 0.001 richiesta
    # pour accélérer on fusionnera intervalles et on testera seulement les points critiques:
    # les hauteurs distinctes des silhouettes dans [y_min,y_max] + les bords y_min,y_max
    # et on teste aussi entre ces points
    
    # récupérer les hauteurs des silhouettes dans l'intervalle
    heights = set()
    for _, _, h in silhouettes:
        if y_min <= h <= y_max:
            heights.add(h)
    heights.add(y_min)
    heights.add(y_max)
    heights = sorted(heights)
    
    # On va tester chaque intervalle entre ces hauteurs avec un point au milieu, plus un test sur les hauteurs elles-mêmes
    # car la couverture peut changer à ces hauteurs
    
    for i in range(len(heights)-1):
        y1 = heights[i]
        y2 = heights[i+1]
        test_points = [y1]
        mid = (y1 + y2) / 2
        # si milieu différent de y1 et y2, on teste aussi le milieu
        if mid != y1 and mid != y2:
            test_points.append(mid)
        test_points.append(y2)
        
        for y in test_points:
            # si y < 0, tout sous l'horizon est couvert par définition
            if y <= 0:
                continue
            
            sun_int = sun_interval_at_y(y, cy, r)
            if sun_int is None:
                # pas dans le disque, pas besoin de vérifier couverture
                continue
            x_left, x_right = sun_int
            
            # on récupère les intervalles de silhouettes couvrant y (passons y > 0)
            silhouettes_ints = silhouettes_coverage_at_y(y, silhouettes)

            # la zone sous l'horizon (y <= 0) ne couvre pas cette ligne y > 0, donc pas à inclure
            
            # fusionner les intervalles de silhouettes
            merged = merge_intervals(silhouettes_ints)
            
            # vérifier que l'intervalle (x_left,x_right) est inclus dans l'union des merged
            # parcourir merged à la recherche d'un intervalle incluant entièrement [x_left,x_right]
            covered = False
            for start, end in merged:
                if start <= x_left + 1e-12 and end >= x_right - 1e-12:
                    covered = True
                    break
            if not covered:
                return False
    return True

def solve():
    for line in sys.stdin:
        line=line.strip()
        if line == '':
            continue
        r, n = map(int,line.split())
        if r == 0 and n == 0:
            break
        
        silhouettes = []
        for _ in range(n):
            x_li, x_ri, h_i = map(int, sys.stdin.readline().split())
            silhouettes.append((x_li, x_ri, h_i))
        
        # recherche binaire sur t pour trouver le dernier instant avec couverture
        # t≥0, on sait que c'est fini à un moment : le soleil sort des silhouettes
        
        low = 0.0
        high = 100.0  # assez grand pour qu'on soit sûr que soleil est découverte (ex: t=100 dépasse hauteur max 20+20)
        
        # pour gérer le cas où t=0 tout just est couvert
        # on affine jusqu'à la précision 0.0001 (10^-4)
        for _ in range(50):
            mid = (low + high)/2
            if is_sun_covered(mid, r, silhouettes):
                low = mid
            else:
                high = mid
        
        print(f"{low:.4f}")

if __name__ == "__main__":
    solve()