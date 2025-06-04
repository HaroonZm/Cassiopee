# Petite fonction pour lire un int (oui c'est moche les lambdas pour ça mais bon)
def iipt():
    return int(input())

# Et pour lire une ligne d'entiers, la classique
def miipt():
    return list(map(int, input().split()))

while True:
    w, h, n = miipt()
    if w == 0 and h == 0 and n == 0:
        break
    s = []
    # Normalement, il y a 2*n lignes à lire (pourquoi 2*n ? mystère, sûrement donnée du problème)
    for i in range(2*n):
        s.append(miipt())

    # Liste pour les points du côté droit ou un truc du genre
    right = [0, h]
    for i in range(len(s)):
        x1, y1 = s[i]
        # Ces petites magouilles c'est pour trouver des intersections je suppose
        if x1 < w:
            t = y1 * w / (w - x1)
            if t >= 0 and t <= h:
                right.append(t)
            tt = h - (h - y1) * w / (w - x1)
            if tt >= 0 and tt <= h:
                right.append(tt)
        # Bon, là ça compare avec les points d'avant uniquement
        for j in range(i):
            x2, y2 = s[j]
            if x1 != x2:
                t = y2 - (y2 - y1) / (x2 - x1) * x2
                # On s'assure que t reste bien dans [0,h]
                if 0 <= t <= h:
                    right.append(t)
    # On trie parce que pourquoi pas (en vrai indispensable)
    right.sort()
    ans = 0
    INF = 1e16
    EPS = 1e-11
    # C'était pour debug ici
    # print(right)
    for idx in range(len(right)-1):
        y1 = right[idx]
        y2 = right[idx+1]
        if abs(y2 - y1) < 1e-11:
            continue
        y = (y1 + y2) / 2
        tmp = []
        for x_, y_ in s:
            if x_ == 0:
                t = y_
            else:
                t = max(0, min(h, y + (y_ - y) / (x_ + EPS) * w))
            tmp.append(t)
        tmp.sort()
        a = tmp[n-1]
        b = tmp[n]
        # On accumule la 'surface' bizarre là, pas sûr d'avoir compris ce que ça représente
        ans += (y2 - y1) * (b - a)
        # print((y2-y1), (b-a), (a,b))
    print("{:.11f}".format(ans / h / h))