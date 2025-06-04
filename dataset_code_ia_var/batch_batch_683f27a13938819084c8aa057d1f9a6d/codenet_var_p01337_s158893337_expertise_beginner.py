import math

n = int(input())

def polynome(a, b, c, d):
    def f(x):
        return a * x**3 + b * x**2 + c * x + d
    return f

def trouver_racines(a, b, c):
    A = 3 * a
    B = 2 * b
    try:
        delta = B * B - 4 * A * c
        if delta < 0:
            return -1
        racine = math.sqrt(delta)
        if racine == 0:
            return 0
        else:
            x1 = (-B + racine) / (2 * A)
            x2 = (-B - racine) / (2 * A)
            return (x1, x2)
    except:
        return -1

def cas_boa(fz, lmax, lmin, p, n):
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

def afficher(x, y):
    if x > 0:
        print(y, 0)
    elif x < 0:
        print(0, y)
    else:
        print(0, 0)

for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a < 0:
        a = -a
        b = -b
        c = -c
        d = -d

    f = polynome(a, b, c, d)
    p = 0
    n_val = 0

    racines = trouver_racines(a, b, c)
    if racines == -1:
        afficher(-d, 1)
    elif racines == 0:
        x0 = -b / (3 * a)
        if f(x0) == 0:
            afficher(-b, 3)
        else:
            afficher(-d, 1)
    else:
        x1, x2 = racines
        if f(x1) < f(x2):
            lmax = x2
            lmin = x1
        else:
            lmax = x1
            lmin = x2
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
            result = cas_boa(fz, lmax, lmin, p, n_val)
            print(result[0], result[1])
        elif fmax == 0:
            result = cas_ao(fz, lmax, p, n_val)
            print(result[0], result[1])
        elif fmin == 0:
            result = cas_bo(fz, lmin, p, n_val)
            print(result[0], result[1])
        else:
            result = cas_aob(fz, p, n_val)
            print(result[0], result[1])