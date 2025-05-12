def out_p(bx, by, x0, y0, x1, y1):
    a, b = x0-bx, y0-by
    c, d = x1-bx, y1-by
    return a*d - b*c
def sgn(x):
    return -1 if x<0 else 1
n = input()
xp = [0] * 3; yp = [0] * 3;
xk, yk, xs, ys = [0]*4
for i in xrange(n):
    xp[0], yp[0], xp[1], yp[1], xp[2], yp[2], xk, yk, xs, ys = map(int, raw_input().split())
    rk = [0]*3
    for i in xrange(3):
        rk[i] = sgn(out_p(xp[i], yp[i], xp[i-2], yp[i-2], xk, yk))
    k_in = (rk[0] == rk[1] == rk[2])
    rs = [0]*3
    for i in xrange(3):
        rs[i] = sgn(out_p(xp[i], yp[i], xp[i-2], yp[i-2], xs, ys))
    s_in = (rs[0] == rs[1] == rs[2])
    print "OK" if k_in ^ s_in else "NG"