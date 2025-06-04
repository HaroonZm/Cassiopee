import itertools

def putpiece(X, Y, bitmap, unused, pieces, numans, pcsans):
    if len(unused) == 0:
        return numans + 1, pieces
    if numans > 1:
        return 2, pieces

    b, k, y, x = unused[-1]

    for i in range(1, min(X+1, k+1)):
        if (k // i) * (k // (k // i)) == k:
            h = k // i
            w = k // (k // i)
            # Pour chaque façon de placer le morceau
            ps = max(0, y - h + 1)
            pe = min(Y - h + 1, y + 1)
            qs = max(0, x - w + 1)
            qe = min(X - w + 1, x + 1)
            for pt in range(ps, pe):
                for qt in range(qs, qe):
                    rt = pt + h - 1
                    st = qt + w - 1
                    piece = 0
                    for j in range(rt - pt + 1):
                        piece |= ((2 ** (st - qt + 1) - 1) << (qt)) << ((pt + j) * X)
                    mark = 1 << (y * X + x)
                    if (bitmap & piece) == mark:
                        result = putpiece(X, Y, bitmap | piece, unused[:-1], pieces + [[b, k, pt, qt, rt, st]], numans, pcsans)
                        numans, pcsans = result
                    if numans > 1:
                        return 2, pcsans
    return numans, pcsans

def main():
    while True:
        X, Y, n = map(int, input().split())
        if X == 0:
            break
        bk = []
        for _ in range(n):
            bk.append(list(map(int, input().split())))
        ss = []
        for _ in range(Y):
            ss.append(list(map(int, input().split())))
        yxs = []
        for i in range(Y):
            for j in range(X):
                if ss[i][j]:
                    yxs.append([ss[i][j], i, j])
        yxs.sort()
        bk.sort()
        bkyx = []
        for i in range(n):
            bkyx.append(bk[i] + yxs[i][1:])
        # Génère le bitmap des cases déjà remplies
        filled = ""
        for i in range(Y):
            for j in range(X):
                if ss[i][j]:
                    filled += "1"
                else:
                    filled += "0"
        nans, pcs = putpiece(X, Y, int(filled, 2), bkyx, [], 0, 0)
        if nans > 1:
            print("NA")
        elif nans == 1:
            toprint = []
            for _ in range(Y):
                toprint.append([0]*X)
            for p in pcs:
                i, _, sy, sx, ey, ex = p
                for j in range(sy, ey+1):
                    for k in range(sx, ex+1):
                        toprint[j][k] = i
            for a in toprint:
                print(" ".join(str(b) for b in a))
        else:
            print("NA")

if __name__ == "__main__":
    main()