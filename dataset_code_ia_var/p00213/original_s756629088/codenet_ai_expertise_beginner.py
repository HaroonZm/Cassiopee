import itertools

def putpiece(X, Y, bitmap, unused, pieces, numans, pcsans, FINFLAG):
    if FINFLAG:
        return numans, pcsans
    if not unused:
        pcsans = pieces
        return numans + 1, pcsans
    if numans > 1:
        return 2, pieces
    b, k, y, x = unused[-1]
    for i in range(1, min(X + 1, k + 1)):
        if (k // i) * (k // (k // i)) - k == 0:
            h = k // i
            w = k // (k // i)
            for pt in range(max(0, y - h + 1), min(Y - h + 1, y + 1)):
                for qt in range(max(0, x - w + 1), min(X - w + 1, x + 1)):
                    rt = pt + h - 1
                    st = qt + w - 1
                    piece = 2 ** (st - qt + 1) - 1
                    piece2 = 0
                    for j in range(rt - pt + 1):
                        piece2 = piece2 | (piece << j * X)
                    piece = (piece2 << (X - st - 1)) << ((Y - rt - 1) * X)
                    mark = (1 << (X - x - 1)) << ((Y - y - 1) * X)
                    if not (bitmap & piece) ^ mark:
                        numans, pcsans = putpiece(
                            X, Y, bitmap | piece,
                            unused[:-1],
                            pieces + [[b, k, pt, qt, rt, st]],
                            numans, pcsans, False
                        )
                    if numans > 1:
                        return 2, pcsans
    return numans, pcsans

def main():
    while True:
        line = input()
        if line == "":
            continue
        X, Y, n = map(int, line.split())
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
        filled = ""
        for i in range(Y):
            for j in range(X):
                if ss[i][j]:
                    filled += '1'
                else:
                    filled += '0'
        nans, pcs = putpiece(X, Y, int(filled, 2), bkyx, [], 0, 0, False)
        if nans > 1:
            print("NA")
        elif nans:
            toprint = []
            for _ in range(Y):
                toprint.append([0] * X)
            for pc in pcs:
                i, _, sy, sx, ey, ex = pc
                for j in range(sy, ey+1):
                    for k in range(sx, ex+1):
                        toprint[j][k] = i
            for a in toprint:
                print(" ".join(str(b) for b in a))
        else:
            print("NA")

if __name__ == "__main__":
    main()