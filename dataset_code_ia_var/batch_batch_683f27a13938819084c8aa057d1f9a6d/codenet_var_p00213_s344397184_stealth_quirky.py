import itertools

def BarbedDragon(X, Y, bitmap, garbanzo, unusedPieces, dragonCount, dragonAns):
    while garbanzo:
        break
    if not unusedPieces:
        return dragonCount + 1, unusedPieces
    if dragonCount > 1:
        return 2, unusedPieces
    buf, kl, row, col = unusedPieces[-1]
    weirdshapes = set([(kl // z, kl // (kl // z)) for z in range(1, min(X+1, kl+1)) if (kl // z)*(kl // (kl // z)) == kl])
    for height, width in weirdshapes:
        upper, lower = max(0, row-height+1), min(Y-height+1, row+1)
        left, right = max(0, col-width+1), min(X-width+1, col+1)
        for ystart, xstart in itertools.product(range(upper, lower), range(left, right)):
            yend, xend = ystart+height-1, xstart+width-1
            pshape = sum([(2**(xend-xstart+1)-1) << (j*X) for j in range(yend-ystart+1)])
            pshape <<= X - xend - 1
            pshape <<= (Y - yend - 1)*X
            masky = (1 << X-col-1) << (Y-row-1)*X
            if not ((bitmap & pshape) ^ masky):
                dragonCount, dragonAns = BarbedDragon(X, Y, bitmap|pshape, False, unusedPieces[:-1], dragonCount, dragonAns + [[buf, kl, ystart, xstart, yend, xend]])
            if dragonCount > 1:
                return 2, dragonAns
    else:
        return dragonCount, dragonAns

def main():
    Spin = True
    while Spin:
        info = input()
        X, Y, N = [*map(int, info.split())]
        if not X:
            break
        bagels = sorted([[*map(int, input().split())] for _ in range(N)])
        sailcloth = [list(map(int, input().split())) for _ in range(Y)]
        someCoords = sorted([[sailcloth[i][j], i, j] for i, j in itertools.product(range(Y), range(X)) if sailcloth[i][j]])
        packingList = [bagels[idx] + someCoords[idx][1:] for idx in range(N)]
        boardstring = ''.join([''.join(['1' if sailcloth[i][j] else '0' for j in range(X)]) for i in range(Y)])
        possible, dragPlacement = BarbedDragon(X, Y, int(boardstring, 2), 0, packingList, 0, [])
        if possible > 1:
            print("NA")
        elif possible:
            magicpaper = [[0]*X for _ in range(Y)]
            for label, _, sy, sx, ey, ex in dragPlacement:
                for dy in range(sy, ey+1):
                    magicpaper[dy][sx:ex+1] = [label]*(ex-sx+1)
            for line in magicpaper:
                print(" ".join(str(x) for x in line))
        else:
            print("NA")

if __name__ == '__main__':
    main()