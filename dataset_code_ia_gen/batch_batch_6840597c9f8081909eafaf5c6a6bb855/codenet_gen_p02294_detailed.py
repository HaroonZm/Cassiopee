def on_segment(p, q, r):
    # Vérifie si le point q est sur le segment pr
    if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
        return True
    return False

def orientation(p, q, r):
    # Calcule l'orientation de l'ordre des points (p, q, r)
    # 0 -> colinéaire, 1 -> horaire, 2 -> antihoraire
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def segments_intersect(p0, p1, p2, p3):
    # Trouve les orientations nécessaires pour la comparaison
    o1 = orientation(p0, p1, p2)
    o2 = orientation(p0, p1, p3)
    o3 = orientation(p2, p3, p0)
    o4 = orientation(p2, p3, p1)

    # Conditions générales d'intersection des segments
    if o1 != o2 and o3 != o4:
        return True

    # Cas particuliers - colinéaires et chevauchement
    if o1 == 0 and on_segment(p0, p2, p1):
        return True

    if o2 == 0 and on_segment(p0, p3, p1):
        return True

    if o3 == 0 and on_segment(p2, p0, p3):
        return True

    if o4 == 0 and on_segment(p2, p1, p3):
        return True

    # Sinon, pas d'intersection
    return False

# Lecture du nombre de requêtes
q = int(input())

for _ in range(q):
    # Lecture des coordonnées des points
    data = list(map(int, input().split()))
    p0 = (data[0], data[1])
    p1 = (data[2], data[3])
    p2 = (data[4], data[5])
    p3 = (data[6], data[7])

    # Affiche 1 si intersection, 0 sinon
    print(1 if segments_intersect(p0, p1, p2, p3) else 0)