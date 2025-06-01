from itertools import product

while True:
    X,Y,n = map(int,input().split())
    if X == 0:
        break
    bk = sorted([list(map(int,input().split())) for _ in range(n)])
    ss = [list(map(int,input().split())) for _ in range(Y)]
    yxs = sorted([ss[i][j],i,j] for i,j in product(range(Y),range(X)) if ss[i][j])
    bkyx = [bk[i]+yxs[i][1:] for i in range(n)]
    filled = "".join("".join("1" if ss[i][j] else "0" for j in range(X)) for i in range(Y))
    bitmap = int(filled,2)
    unused = bkyx
    pieces = []
    numans = 0
    pcsans = 0
    stack = [(bitmap, unused, pieces, numans, pcsans)]
    result_numans = 0
    result_pcsans = []
    while stack:
        bitmap, unused, pieces, numans, pcsans = stack.pop()
        if not unused:
            result_numans = numans + 1
            result_pcsans = pieces
            if result_numans > 1:
                break
            continue
        if numans > 1:
            result_numans = 2
            break
        b,k,y,x = unused[-1]
        found = False
        for h,w in set((k//i, k//(k//i)) for i in range(1, min(X+1,k+1)) if (k//i)*(k//(k//i)) == k):
            ps = max(0,y-h+1)
            pe = min(Y-h+1,y+1)
            qs = max(0,x-w+1)
            qe = min(X-w+1,x+1)
            for pt,qt in product(range(ps,pe), range(qs,qe)):
                rt = pt + h - 1
                st = qt + w - 1
                piece = 0
                for j in range(rt - pt + 1):
                    piece |= ((2**(st - qt + 1) - 1) << (pt + j)*X + (X - st - 1))
                piece <<= (Y - rt - 1)*X
                mark = 1 << ((Y - y - 1)*X + (X - x - 1))
                if not (bitmap & piece) ^ mark:
                    newbitmap = bitmap | piece
                    newunused = unused[:-1]
                    newpieces = pieces + [[b,k,pt,qt,rt,st]]
                    newnumans = numans
                    newpcsans = pcsans
                    stack.append((newbitmap, newunused, newpieces, newnumans, newpcsans))
                    found = True
        if not found:
            # no fitting piece found, backtrack
            continue
    if result_numans > 1 or result_numans == 0:
        print("NA")
    else:
        toprint = [[0]*X for _ in range(Y)]
        for i,_,sy,sx,ey,ex in result_pcsans:
            for j in range(sy, ey+1):
                for k_ in range(sx, ex+1):
                    toprint[j][k_] = i
        for row in toprint:
            print(" ".join(str(x) for x in row))