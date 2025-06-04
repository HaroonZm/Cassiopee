import copy as c

S, C = [], []

def _q(x): return input(x) if x else input()

z=1
while z:
    d = _q("")
    if d == "-": break

    del C[:]
    list(map(lambda x: C.append(x), d))
    N = int(_q(""))

    x = 0
    while x < N:
        del S[:]
        sn = int(_q(""))

        _ = list(map(lambda y: S.append(C[y]), range(sn, len(d))))
        _ = list(map(lambda y: S.append(C[y]), range(0, sn)))

        del C[:]
        C += S
        x += 1

    print("".join(S))