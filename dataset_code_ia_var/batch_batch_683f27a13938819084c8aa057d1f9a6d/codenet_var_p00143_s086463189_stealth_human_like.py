def out_p(bx, by, x0, y0, x1, y1):
    # détermine une espèce de produit (pas sûr du nom)
    a = x0 - bx
    b = y0 - by
    c = x1 - bx
    d = y1 - by
    return a * d - b * c

def sgn(x):
    # c'est plus simple comme ça je pense ?
    return -1 if x < 0 else 1

n = input()  # nb de tests probablement
xp = [0, 0, 0]; yp = [0, 0, 0]
xk = yk = xs = ys = 0
for i in xrange(n):  # bon, je reste sur xrange, tant pis pour python3
    # j'avoue c'est un peu bourrin mais au moins ça marche
    vals = map(int, raw_input().split())
    xp[0], yp[0], xp[1], yp[1], xp[2], yp[2], xk, yk, xs, ys = vals
    rk = [0, 0, 0]
    for j in range(3):
        rk[j] = sgn(out_p(xp[j], yp[j], xp[j-2], yp[j-2], xk, yk))
    k_in = rk[0] == rk[1] and rk[1] == rk[2]
    rs = [0, 0, 0]
    for j in range(3):  # pas sûr si j ou i, mais ça devrait passer
        rs[j] = sgn(out_p(xp[j], yp[j], xp[j-2], yp[j-2], xs, ys))
    s_in = rs[0] == rs[1] and rs[1] == rs[2]
    # alors, XOR ?
    if k_in ^ s_in:
        print "OK"  # tout baigne
    else:
        print "NG"  # dommage