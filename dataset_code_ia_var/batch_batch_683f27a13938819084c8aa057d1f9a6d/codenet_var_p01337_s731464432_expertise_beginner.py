import math

n = int(input())

def calc_poly(a, b, c, d):
    # Fonction qui retourne une fonction polynôme de degré 3
    def poly(x):
        return a * x ** 3 + b * x ** 2 + c * x + d
    return poly

def calc_extremum(a, b, c):
    # Calcul des extremums (racines de la dérivée)
    a_der = 3 * a
    b_der = 2 * b
    try:
        delta = b_der ** 2 - 4 * a_der * c
        if delta < 0:
            return -1
        racine = math.sqrt(delta)
        if racine == 0:
            return 0
        x1 = (-b_der + racine) / (2 * a_der)
        x2 = (-b_der - racine) / (2 * a_der)
        return (x1, x2)
    except:
        return -1

def cas_boa(fz, lmax, lmin, p, n):
    # Pour certains cas où fmin<0< fmax
    if fz > 0:
        if lmin > 0:
            p = 2
            n = 1
        else:
            n = 3
    elif fz == 0:
        if 0 < lmin and lmax < 0:
            p = 1
            n = 1
        elif lmax > 0:
            p = 2
        else:
            n = 2
    else:
        if lmax > 0:
            p = 3
        else:
            p = 1
            n = 2
    return p, n

def cas_ao(fz, lmax, p, n):
    if fz > 0:
        n = 2
    elif fz == 0:
        if lmax == 0:
            p = 1
        else:
            n = 1
    else:
        if lmax > 0:
            p = 2
        else:
            p = 1
            n = 1
    return p, n

def cas_bo(fz, lmin, p, n):
    if fz > 0:
        if lmin > 0:
            p = 1
            n = 1
        else:
            n = 2
    elif fz == 0:
        if lmin == 0:
            n = 1
        else:
            p = 1
    else:
        p = 2
    return p, n

def cas_aob(fz, p, n):
    if fz > 0:
        n = 1
    elif fz < 0:
        p = 1
    return p, n

def affiche(x, y):
    if x > 0:
        print(y, 0)
    elif x < 0:
        print(0, y)
    else:
        print(0, 0)

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a < 0:
        a = -a
        b = -b
        c = -c
        d = -d

    f = calc_poly(a, b, c, d)
    p = 0
    nval = 0

    racines = calc_extremum(a, b, c)
    if racines == -1:
        affiche(-d, 1)
    elif racines == 0:
        valeur = f(-b / (3 * a))
        if valeur == 0:
            affiche(-b, 3)
        else:
            affiche(-d, 1)
    else:
        if f(racines[0]) < f(racines[1]):
            lmin = racines[0]
            lmax = racines[1]
        else:
            lmin = racines[1]
            lmax = racines[0]
        fmax = f(lmax)
        fmin = f(lmin)
        fz = f(0)

        if lmax == lmin:
            if lmax < 0:
                print(0, 3)
            elif lmax > 0:
                print(3, 0)
            else:
                print(0, 0)
        elif fmin < 0 and 0 < fmax:
            p_n = cas_boa(fz, lmax, lmin, p, nval)
            print(p_n[0], p_n[1])
        elif fmax == 0:
            p_n = cas_ao(fz, lmax, p, nval)
            print(p_n[0], p_n[1])
        elif fmin == 0:
            p_n = cas_bo(fz, lmin, p, nval)
            print(p_n[0], p_n[1])
        else:
            p_n = cas_aob(fz, p, nval)
            print(p_n[0], p_n[1])