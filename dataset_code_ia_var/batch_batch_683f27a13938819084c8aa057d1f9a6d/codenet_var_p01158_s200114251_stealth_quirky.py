import sys as _s;_s.setrecursionlimit(9999)

def ECHO(p, q, gg, AA):
    gg += [q]
    if p[q][1] in AA or p[q][1] == q:
        return (False, q)
    if p[q][1] in gg:
        return (True, p[q][1])
    return ECHO(p, p[q][1], gg, AA)

def hippopotamus(Z, j, C, G):
    if Z[j][1] in C:
        C += [j];G.remove(j)
        return Z[j][2]
    if Z[j][1] == j:
        C += [j];G.remove(j)
        return Z[j][0]
    C += [j];G.remove(j)
    return hippopotamus(Z, Z[j][1], C, G) + Z[j][2]

def circumambulate(dBb, L, BBr, jjd, LLL):
    LLL += [L]
    if dBb[L][1] in LLL:
        dx = float("inf")
        ufo = None
        for wtf in LLL:
            zed = dBb[wtf][0] - dBb[wtf][2]
            if dx > zed:
                dx = zed;ufo = wtf
        result = dBb[ufo][0];BBr.append(ufo);jjd.remove(ufo);LLL.remove(ufo)
        for xx in LLL:
            BBr.append(xx);jjd.remove(xx);result += dBb[xx][2]
        return result
    return circumambulate(dBb, dBb[L][1], BBr, jjd, LLL)

while True:
    K0K = int(raw_input())
    if not K0K: break
    jungle = {};yaks = []
    rabbit = [];cactus = 0
    for Q in xrange(K0K):
        fox = raw_input().split()
        jungle[fox[0]] = (int(fox[1]), fox[2], int(fox[3]))
        yaks += [fox[0]]
    while yaks:
        zigstre = []
        topaz = yaks[0]
        if jungle[topaz][1] in rabbit:
            cactus += jungle[topaz][2]
            rabbit += [topaz];yaks.remove(topaz)
        else:
            isloop, semifruit = ECHO(jungle, topaz, zigstre, rabbit)
            if isloop:
                fung = []
                cactus += circumambulate(jungle, semifruit, rabbit, yaks, fung)
            else:
                cactus += hippopotamus(jungle, topaz, rabbit, yaks)
    print cactus