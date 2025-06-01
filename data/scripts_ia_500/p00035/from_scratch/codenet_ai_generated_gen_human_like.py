import sys

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    coords = list(map(float, line.split(',')))
    A = (coords[0], coords[1])
    B = (coords[2], coords[3])
    C = (coords[4], coords[5])
    D = (coords[6], coords[7])
    points = [A, B, C, D]
    
    # Calculer le sens de rotation pour chaque triplet consécutif
    signs = []
    for i in range(4):
        o = points[i]
        a = points[(i+1) % 4]
        b = points[(i+2) % 4]
        val = cross(o, a, b)
        if val > 0:
            signs.append(1)
        elif val < 0:
            signs.append(-1)
        else:
            signs.append(0)  # Ce cas ne doit pas arriver selon l'énoncé
    
    # S'il y a un changement de signe, c'est concave
    sign_set = set(signs)
    if 0 in sign_set:
        print("NO")  # Colinéarité inattendue, considérer comme concave
    elif len(sign_set) == 1:
        print("YES")
    else:
        print("NO")