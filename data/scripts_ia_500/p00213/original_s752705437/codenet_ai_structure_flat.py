from itertools import product

while True:
    X,Y,n = map(int,input().split())
    if X == 0: break
    bk = [list(map(int,input().split())) for _ in range(n)]
    bk.sort()
    ss = [list(map(int,input().split())) for _ in range(Y)]
    yxs = []
    for i in range(Y):
        for j in range(X):
            if ss[i][j]:
                yxs.append([ss[i][j],i,j])
    yxs.sort()
    bkyx = []
    for i in range(n):
        bkyx.append(bk[i]+yxs[i][1:])
    filled_str = ""
    for i in range(Y):
        for j in range(X):
            filled_str += "1" if ss[i][j] else "0"
    bitmap = int(filled_str,2)

    def putpiece(X,Y,bitmap,unused,pieces,numans,pcsans):
        if not unused:
            return numans + 1, pieces
        if numans > 1:
            return 2, pieces
        b,k,y,x = unused[-1]
        hs_ws = set()
        for i in range(1,min(X+1,k+1)):
            h = k//i
            w = k//(k//i)
            if h*w == k:
                hs_ws.add((h,w))
        for h,w in hs_ws:
            ps = max(0,y - h + 1)
            pe = min(Y - h + 1,y + 1)
            qs = max(0,x - w + 1)
            qe = min(X - w + 1,x + 1)
            for pt in range(ps,pe):
                for qt in range(qs,qe):
                    rt = pt + h -1
                    st = qt + w -1
                    piece = 0
                    for j in range(rt - pt + 1):
                        piece += (2**(st - qt +1) -1) << (j*X)
                    piece = piece << (X - st -1)
                    piece = piece << ((Y - rt -1)*X)
                    mark = 1 << (X - x -1)
                    mark = mark << ((Y - y -1)*X)
                    if (bitmap & piece) ^ mark == 0:
                        numans,pcsans = putpiece(X,Y,bitmap|piece,unused[:-1],pieces+[[b,k,pt,qt,rt,st]],numans,pcsans)
                    if numans > 1:
                        return 2, pcsans
        return numans,pcsans

    nans, pcs = putpiece(X,Y,bitmap,bkyx,[],0,0)
    if nans > 1:
        print("NA")
    elif nans == 1:
        toprint = [[0]*X for _ in range(Y)]
        for i,_,sy,sx,ey,ex in pcs:
            for j in range(sy,ey+1):
                for k in range(sx,ex+1):
                    toprint[j][k] = i
        for row in toprint:
            print(" ".join(str(c) for c in row))
    else:
        print("NA")