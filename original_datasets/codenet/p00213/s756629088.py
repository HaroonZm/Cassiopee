from itertools import product
# from line_profiler import LineProfiler

def putpiece(X,Y,bitmap,unused,pieces,numans,pcsans,FINFLAG):
    if FINFLAG:
        return numans,pcsans
    if not unused:
        pcsans = pieces
        return numans + 1, pcsans
    if numans > 1:
        return 2, pieces
    b,k,y,x = unused[-1]
    for h,w in set([ (k//i,k//(k//i)) for i in range(1,min(X+1,k+1)) if not (k//i)*(k//(k//i)) - k]):
        for pt,qt in product(range(max(0,y-h+1),min(Y-h+1,y+1)),range(max(0,x-w+1),min(X-w+1,x+1))):
            rt,st = pt+h-1, qt+w-1
            piece = 2**(st-qt+1)-1
            piece2 = 0
            for j in range(rt-pt+1): piece2 |= piece << j*X
            piece = ( piece2 << X-st-1 ) << (Y-rt-1)*X
            mark = ( 1 << X-x-1 ) << (Y-y-1)*X
            if not (bitmap&piece)^mark: numans,pcsans = putpiece(X,Y,bitmap|piece,unused[:-1],pieces+[[b,k,pt,qt,rt,st]],numans,pcsans,False)
            if numans > 1: return 2, pcsans
    else:
        return numans,pcsans

def main():
    while(True):
        X,Y,n = map(int,input().split())
        if not X: break
        bk = sorted([list(map(int,input().split())) for _ in range(n)])
        ss = [list(map(int,input().split())) for _ in range(Y)]
        yxs = sorted([ss[i][j],i,j] for i,j in product(range(Y),range(X)) if ss[i][j])
        bkyx = [ bk[i]+yxs[i][1:] for i in range(n)]
        filled = "".join([ "".join(["1" if ss[i][j] else "0" for j in range(X)]) for i in range(Y)])
        nans,pcs = putpiece(X,Y,int(filled,2),bkyx,[],0,0,False)
        if nans > 1:
            print("NA")
        elif nans:
            toprint = [[0]*X for _ in range(Y)]
            for i,_,sy,sx,ey,ex in pcs:
                for j in range(sy,ey+1): toprint[j][sx:ex+1] = [i]*(ex-sx+1)
            for a in toprint: print(" ".join(str(b) for b in a))
        else:
            print("NA")

if __name__ == "__main__":
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.add_function(putpiece)
    # prf.runcall(main)
    # prf.print_stats()
    main()