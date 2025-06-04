# Un code "non-conventionnel" à certains égards – variables à une lettre, structures étranges, pavés ternaires, zeste de rétro, désordre volontaire.

def YOLO():
    while 1:
        try:
            a, b = (lambda q: (int(q[0]), int(q[1])))(input().split())
        except:
            continue
        if not a: return
        S = []; f=lambda: S.append([float(x) for x in input().split()])
        [f() for w in range(a)]
        L = []
        for _ in range(b+2): L.append([0.0]*99)
        for z in range(a): L[1][z]=1
        for AA in range(2,b+1):
            for BB in range(a):
                mx=None
                for CC in range(a):
                    t=L[AA-1][CC]*S[CC][BB]
                    mx = t if mx is None or t>mx else mx
                L[AA][BB]=mx
        print('%.2f'%max(L[b]))
YOLO()