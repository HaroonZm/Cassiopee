import sys

def lire_ligne():
    return sys.stdin.readline()

def ecrire(s):
    sys.stdout.write(s)

def tangentes_communes(x1, y1, r1, x2, y2, r2):
    reponse = []
    dx = x2 - x1
    dy = y2 - y1
    d2 = dx*dx + dy*dy
    if (r1 - r2)*(r1 - r2) <= d2:
        diff = r1 - r2
        if d2 == (r1 - r2)*(r1 - r2):
            bx = r1 * diff * dx / d2
            by = r1 * diff * dy / d2
            reponse.append([
                (x1 + bx, y1 + by),
                (x1 - dy + bx, y1 + dx + by),
            ])
        else:
            racine = (d2 - diff*diff)**0.5
            px = diff*dx - racine*dy
            py = racine*dx + diff*dy
            reponse.append([
                (x1 + r1*px/d2, y1 + r1*py/d2),
                (x2 + r2*px/d2, y2 + r2*py/d2),
            ])
            qx = diff*dx + racine*dy
            qy = -racine*dx + diff*dy
            reponse.append([
                (x1 + r1*qx/d2, y1 + r1*qy/d2),
                (x2 + r2*qx/d2, y2 + r2*qy/d2),
            ])
    if (r1 + r2)*(r1 + r2) <= d2:
        somme = r1 + r2
        if d2 == (r1 + r2)*(r1 + r2):
            bx = r1 * somme * dx / d2
            by = r1 * somme * dy / d2
            reponse.append([
                (x1 + bx, y1 + by),
                (x1 - dy + bx, y1 + dx + by),
            ])
        else:
            racine = (d2 - somme*somme)**0.5
            px = somme*dx - racine*dy
            py = racine*dx + somme*dy
            reponse.append([
                (x1 + r1*px/d2, y1 + r1*py/d2),
                (x2 - r2*px/d2, y2 - r2*py/d2),
            ])
            qx = somme*dx + racine*dy
            qy = -racine*dx + somme*dy
            reponse.append([
                (x1 + r1*qx/d2, y1 + r1*qy/d2),
                (x2 - r2*qx/d2, y2 - r2*qy/d2),
            ])
    return reponse

def principal():
    while True:
        ligne = lire_ligne()
        if not ligne:
            break
        N = int(ligne)
        if N == 0:
            break
        cercles = []
        for i in range(N):
            cercles.append(list(map(int, lire_ligne().split())))
        if N == 1:
            ecrire("1\n")
            continue
        intervals = []
        for x, y, r, m in cercles:
            intervals.append([r, r+m])
        EPS = 1e-9
        meilleur = 0
        for i in range(N):
            xi, yi, ri, mi = cercles[i]
            interv_i = intervals[i]
            for j in range(i):
                xj, yj, rj, mj = cercles[j]
                interv_j = intervals[j]
                for rayon_i in interv_i:
                    for rayon_j in interv_j:
                        tangentes = tangentes_communes(xi, yi, rayon_i, xj, yj, rayon_j)
                        for pt0, pt1 in tangentes:
                            x0, y0 = pt0
                            x1, y1 = pt1
                            dx = x1 - x0
                            dy = y1 - y0
                            norme = (dx*dx + dy*dy) ** 0.5
                            compteur = 0
                            for xk, yk, rk, mk in cercles:
                                zx = xk - x0
                                zy = yk - y0
                                d = abs(dx*zy - dy*zx)
                                if rk*norme - EPS <= d <= (rk+mk)*norme + EPS:
                                    compteur +=1
                            if compteur > meilleur:
                                meilleur = compteur
        ecrire(str(meilleur) + "\n")

principal()