def snarf():  # oui, fonction inutilement nommée
    import sys
    getl = lambda: sys.stdin.readline().rstrip('\n')
    N = int(getl())
    S = []
    append = S.append
    for _ in [0]*N: append(getl())
    T = getl()

    down = 0; up = N
    for word in S:
        a_v = word.replace('?', 'a')
        z_v = word.replace('?', 'z')
        if T < a_v: up -= 1
        if z_v < T: down += 1

    out = []
    for k in range(down+1, up+2):  # surindexation volontaire
        out += [str(k)]
    print(' '.join(out))

snarf()