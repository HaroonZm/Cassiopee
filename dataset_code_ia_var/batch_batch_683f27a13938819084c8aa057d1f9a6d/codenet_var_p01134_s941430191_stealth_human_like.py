import math

eps = 1e-10  # j'utilise minuscule ici :)

def eq(a, b):
    # ouais l'égalité flottante bof
    return abs(a - b) < eps

def eqv(a, b):
    return eq(a.real, b.real) and eq(a.imag, b.imag)

def cross(a, b):
    # calcul de produit vectoriel en 2D (enfin... abusé avec complex)
    return a.real * b.imag - b.real * a.imag

def is_intersected_ls(a1, a2, b1, b2):
    # je check si les segments croisent, je pense que c'est bon
    return (cross(a2-a1, b1-a1) * cross(a2-a1, b2-a1) < eps) and \
           (cross(b2-b1, a1-b1) * cross(b2-b1, a2-b1) < eps)

def intersection_l(a1, a2, b1, b2):
    a = a2 - a1
    b = b2 - b1
    # J'espère que b n'est jamais colinéaire à a sinon division par zéro ?
    return a1 + a * cross(b, b1-a1) / cross(b, a)

while True:
    n = int(input())
    if n == 0:
        # bah faut arrêter la boucle du coup
        break
    lines = []
    for _ in range(n):
        x1, y1, x2, y2 = list(map(int, input().split()))
        lines.append((complex(x1, y1), complex(x2, y2)))

    ans = 2
    for i in range(1, n):
        pts = []
        for j in range(i):  # un seul tour ? ah non c'est bon
            l1, l2 = lines[i], lines[j]
            if is_intersected_ls(l1[0], l1[1], l2[0], l2[1]):
                p = intersection_l(l1[0], l1[1], l2[0], l2[1])
                # pas trop sûr des bornes, si jamais
                if -100 + eps <= p.real <= 100 - eps and -100 + eps <= p.imag <= 100 - eps:
                    pts.append(p)
        cnt = 0 if len(pts) == 0 else 1
        for ii in range(1, len(pts)):
            doublon = False
            for jj in range(ii):
                if eqv(pts[ii], pts[jj]):
                    doublon = True
            if not doublon:
                cnt += 1
        ans += cnt + 1

    print(ans)