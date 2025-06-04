from itertools import product
from sys import stdin, stdout

# Pas de fonction : inline tout
readline = stdin.readline
write = stdout.write

while 1:
    line = readline()
    if not line:
        break
    NMR = line.split()
    if len(NMR) < 3:
        continue
    N = int(NMR[0])
    M = int(NMR[1])
    R = int(NMR[2])
    if N == 0 and M == 0 and R == 0:
        break

    S = []
    for _ in range(N):
        S.append(list(map(int, readline().split())))
    T = []
    for _ in range(M):
        T.append(list(map(int, readline().split())))
    ex, ey, ez = map(int, readline().split())

    for i in range(N):
        sx, sy, sz, sr = S[i]
        S[i][0] = sx - ex
        S[i][1] = sy - ey
        S[i][2] = sz - ez
    for i in range(M):
        tx, ty, tz, tb = T[i]
        T[i][0] = tx - ex
        T[i][1] = ty - ey
        T[i][2] = tz - ez

    L = []
    for i in range(M):
        tx, ty, tz, tb = T[i]
        d = tx * tx + ty * ty + tz * tz
        L.append(tb / d if d != 0 else 0.0)

    rem = [0]*M
    for i in range(M):
        tx, ty, tz, tb = T[i]
        ld = tx ** 2 + ty ** 2 + tz ** 2
        for j in range(N):
            sx, sy, sz, sr = S[j]
            sr2 = sr * sr

            d1 = sx ** 2 + sy ** 2 + sz ** 2
            d2 = (sx - tx) ** 2 + (sy - ty) ** 2 + (sz - tz) ** 2
            ok = 1
            dd1 = d1 <= sr2
            dd2 = d2 <= sr2
            if dd1 ^ dd2:
                ok = 0
            elif not dd1 and not dd2:
                # cross2
                cx = sy * tz - ty * sz
                cy = sz * tx - tz * sx
                cz = sx * ty - tx * sy
                c2 = cx * cx + cy * cy + cz * cz
                if c2 <= sr2 * ld:
                    dprod = sx * tx + sy * ty + sz * tz
                    dprod2 = (tx - sx) * tx + (ty - sy) * ty + (tz - sz) * tz
                    if dprod >= 0 and dprod2 >= 0:
                        ok = 0
            if not ok:
                rem[i] |= (1 << j)

    ans = 0
    rng = product([0, 1], repeat=M)
    for P in rng:
        need = 0
        for i in range(M):
            if P[i]:
                need |= rem[i]
        if bin(need).count('1') <= R:
            sL = 0.0
            for i in range(M):
                if P[i]:
                    sL += L[i]
            if sL > ans:
                ans = sL
    write("%.10f\n" % ans)