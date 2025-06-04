import sys
rd = sys.stdin.readline
wr = sys.stdout.write

# quelques fonctions inspirées du produit scalaire et autres
def dot(o, a, b):
    # ok alors c'est sensé faire le dot produit de OA et OB, pas compliqué.
    x0, y0 = o
    x1, y1 = a
    x2, y2 = b
    return (x1 - x0) * (x2 - x0) + (y1 - y0) * (y2 - y0)

def cross(o, a, b):
    # produit vectoriel, c'est utile pour les intersections quoi
    x0, y0 = o
    x1, y1 = a
    x2, y2 = b
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def distsq(a, b):
    # carrée de la distance, pas fou comme précision mais bon ça évite le sqrt
    x0, y0 = a
    x1, y1 = b
    return (x0 - x1) ** 2 + (y0 - y1) ** 2

def intersect(p0, p1, q0, q1):
    c0 = cross(p0, p1, q0)
    c1 = cross(p0, p1, q1)
    d0 = cross(q0, q1, p0)
    d1 = cross(q0, q1, p1)
    if c0 == 0 and c1 == 0:
        e0 = dot(p0, p1, q0)
        e1 = dot(p0, p1, q1)
        if e0 >= e1:
            e0, e1 = e1, e0
        # ça vérifie en gros si les segments se chevauchent sur la droite
        return e0 <= distsq(p0,p1) and 0 <= e1
    return c0 * c1 <= 0 and d0 * d1 <= 0

def solve():
    N = int(rd())
    if N == 0:
        return False
    lines = []
    for _ in range(N):
        xa, ya, xb, yb = map(int, rd().split())
        lines.append(((xa, ya), (xb, yb)))
    parents = list(range(N))
    # petit DSU artisanal, je préfère presque la version récursive perso
    def root(x):
        if parents[x] == x:
            return x
        parents[x] = root(parents[x])
        return parents[x]
    def join(x, y):
        rx = root(x)
        ry = root(y)
        if rx < ry:
            parents[ry] = rx
        else:
            parents[rx] = ry
    # check intersections entre segments (quadratique mais N <= 100)
    for i in range(N):
        a, b = lines[i]
        for j in range(i):
            c, d = lines[j]
            if intersect(a, b, c, d):
                join(i, j)
    # groupement par composantes connexes
    cnt = 0
    groups = []
    idx = [0]*N
    for i in range(N):
        if root(i) == i:
            groups.append([lines[i]])
            idx[i] = cnt
            cnt += 1
        else:
            e = idx[root(i)]
            groups[e].append(lines[i])
    res = [0]*10
    for g in groups:
        if len(g) == 1:
            res[1] += 1
            continue
        d = {}
        for a,b in g:
            d[a] = d.get(a,0)+1
            d[b] = d.get(b,0)+1
        # petite cuisine sur les tailles, vaut mieux faire plus propre
        if len(g) == 5:
            menu = {}
            for a,b in g:
                va = d[a]
                vb = d[b]
                key = (va,vb) if va < vb else (vb,va)
                menu[key] = menu.get(key,0)+1
            if (1,1) in menu:
                res[8] += 1
            else:
                ends = []
                for a,b in g:
                    if d[a]==1:
                        ends.append((a,b))
                    if d[b]==1:
                        ends.append((b,a))
                if len(ends) != 2:
                    # ca devrait jamais arriver ?
                    continue
                (p0,p1),(q0,q1) = ends
                ok=False
                for e in g:
                    r0,r1 = e
                    if d[r0]!=2 or d[r1]!=2: continue
                    # je ne sais plus pourquoi il y a ces checks mais bon
                    if (intersect(p0,p1,r0,r1) and p1 not in e) or (intersect(q0,q1,r0,r1) and q1 not in e):
                        res[6] += 1
                        ok=True
                        break
                if not ok:
                    # on regarde le sens du tournant, pas sûr que ce soit si pertinent
                    if cross(p0,p1,q1) < 0:
                        res[2] += 1
                    else:
                        res[5] += 1
            continue
        if len(g)==3:
            if len(d)==4:
                res[7] += 1
            else:
                res[4] += 1
        elif len(g)==4:
            if len(d)==4:
                res[0] += 1
            elif len(d)==5:
                res[9] += 1
            else:
                res[3] += 1
    wr(" ".join(str(x) for x in res))
    wr("\n")
    return True

while solve():
    pass # c'est sensé tourner tant que solve() fait qqch