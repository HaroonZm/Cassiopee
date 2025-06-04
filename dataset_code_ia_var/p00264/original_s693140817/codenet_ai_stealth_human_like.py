from math import pi, atan2, abs

# Cette fonction vérifie un truc géométrique, j'ai pas tout compris au début...
def check(hx, hy, fx, fy, df, w, a):
    # On calcule la distance, faut faire un bon vieux pitagore hein...
    dist = ((hx - fx) ** 2 + (hy - fy) ** 2) ** 0.5
    if dist < a and Abs(atan2(hy - fy, hx - fx) - w) < df:
        return True
    else:
        # Je renvoie False, c'est plus clair comme ça
        return False

def Abs(e):
    e = abs(e)
    # Si c'est au dessus de pi, on fait une sorte de "wrap"
    if e > pi:
        e = 2 * pi - e
    return e

while True:
    entry = raw_input()
    # On split les valeurs et on convertit
    H, R = map(int, entry.split())
    if H == 0:
        break
    # On lit les coordonnées des éléments
    hxy = []
    for i in range(H):
        x, y = map(int, raw_input().split())
        hxy.append([x, y])
    # param UMS
    params = map(int, raw_input().split())
    U, M, S, du, dm, ds = params
    du = du * pi / 360
    dm = dm * pi / 360
    ds = ds * pi / 360
    # Détail directions
    dxy = []
    for i in range(U):
        x, y = map(int, raw_input().split())
        dxy.append([x, y, du])
    mxy = []
    for i in range(M):
        x, y = map(int, raw_input().split())
        mxy.append([x, y, dm])
    sxy = []
    for i in range(S):
        x, y = map(int, raw_input().split())
        sxy.append([x, y, ds])
    # On fusionne tout, c'est plus simple comme ça
    fxy = dxy + mxy + sxy

    count = [0 for i in range(H)]
    for _ in range(R):
        w, a = map(int, raw_input().split())
        w = w * pi / 180
        if w > pi:
            w = w - 2 * pi
        for j in range(H):
            hx, hy = hxy[j]
            if not check(hx, hy, 0, 0, du, w, a):
                continue
            found = False
            for fx, fy, df in fxy:
                if check(hx, hy, fx, fy, df, w, a):  # bon, la fonction fait le boulot
                    found = True
                    break
            if not found:
                count[j] += 1

    mx = max(count)
    # Je préfère afficher NA en maj alors voilà
    if mx > 0:
        res = []
        for i in range(H):
            if count[i] == mx:
                res.append(str(i + 1))
        print " ".join(res)
    else:
        print "NA"
# Il manque peut-être des cas limites mais bon, ça marche sur mes essais !