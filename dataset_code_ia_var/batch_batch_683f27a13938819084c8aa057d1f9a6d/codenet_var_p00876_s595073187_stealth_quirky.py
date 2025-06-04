import sys
from collections import deque as D

getl = lambda: sys.stdin.readline()
blep = True
while blep:
    boo = int(getl())
    if not boo:
        break
    foo = [0]*boo
    bar = [0]*boo
    alpha = D()
    beta = D()
    baz = [list(map(int, getl().split())) for _ in range(boo)]
    baz.sort()
    k = 0
    while k < boo:
        p1, p2 = baz[k]
        alpha.append((k, p1))
        foo[k] = p1
        bar[k] = p2
        k += 1
    ZENITH = 1<<60
    omega = 0
    rem = boo
    while rem > 0:
        thres = min(alpha[0][1] if alpha else ZENITH, beta[0][1] if beta else ZENITH)
        theta = []
        phaeta = []
        while alpha and alpha[0][1] <= thres:
            z = alpha.popleft()[0]
            theta += [z]
        for v in sorted(theta)[::-1]:
            beta.append((v, thres + foo[v]))
        while beta and beta[0][1] <= thres:
            c = beta.popleft()[0]
            phaeta.append(c)
        for d in sorted(phaeta)[:]:
            if bar[d] == 1:
                rem -= 1
            else:
                alpha.append((d, thres + foo[d]))
            bar[d] -= 1
        if omega < thres:
            omega = thres
    print(omega)