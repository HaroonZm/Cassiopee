import sys
from math import gcd
from functools import reduce
from operator import itemgetter

def rational(p, q=1):
    g = gcd(p, q)
    return (p // g, q // g)

def rat_add(a, b):
    pa, qa = a
    pb, qb = b
    if pa == 0:
        return b
    if pb == 0:
        return a
    g = gcd(qa, qb)
    ra = pa * (qb // g) + pb * (qa // g)
    rb = qa * (qb // g)
    gg = gcd(ra, rb)
    return (ra // gg, rb // gg)

def main():
    readline, write = sys.stdin.readline, sys.stdout.write
    INF = 10 ** 18

    def time_criterion(x):
        vw, _, _, th = x
        return INF if vw == 0 else th / vw

    while True:
        N = int(readline())
        if not N:
            break
        pw = int(readline())
        items = [tuple(map(int, readline().split())) for _ in range(N)]
        items.append((1, 0, 1, 0))
        items.sort(key=time_criterion)
        A = [rational(0)] * (N + 1)
        B = [rational(0)] * (N + 1)
        a, b = rational(pw), rational(0)
        for i, (vw, pf, vf, th) in enumerate(items):
            if vw == 0:
                if th > 0:
                    b = rat_add(b, (th * pf, vf))
                continue
            sgn = th ^ vw
            if vw > 0:
                if sgn >= 0:
                    a = rat_add(a, (-vw * pf, vf))
                    b = rat_add(b, (th * pf, vf))
                    A[i] = rational(vw * pf, vf)
                    B[i] = rational(-th * pf, vf)
            else:
                if sgn >= 0:
                    A[i] = rational(-vw * pf, vf)
                    B[i] = rational(th * pf, vf)
                else:
                    a = rat_add(a, (-vw * pf, vf))
                    b = rat_add(b, (th * pf, vf))
        ans = INF
        for i, (vw, pf, vf, th) in enumerate(items):
            if not vw or ((th ^ vw) < 0):
                continue
            a = rat_add(a, A[i])
            b = rat_add(b, B[i])
            pa, qa = a
            pb, qb = b
            denom = vw * qa * qb
            num = pa * th * qb + pb * vw * qa
            v = num / denom if denom else INF
            if ans + 1e-2 < v:
                break
            ans = min(ans, v)
        write(f"{ans:.16f}\n")

main()