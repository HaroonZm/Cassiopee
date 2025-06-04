import itertools as I
# import cProfile

def pUtPiEcE(_x,_y,bb,uu,pz,na,pa,ff):
    # Recursive core; single-letter vars everywhere, reversed positional argument order
    if ff: return na,pa
    if not uu: pa = pz; return na+1,pa
    if na>1: return 2,pz
    b,K,Y,X = uu[-1]
    for H,W in { (K//d,K//(K//d)) for d in range(1,min(_x+1,K+1)) if (K//d)*(K//(K//d))==K }:
        for a,b_ in I.product(range(Y-H+1 if Y-H>=0 else 0, Y+1), range(X-W+1 if X-W>=0 else 0, X+1)):
            e,f = a+H-1, b_+W-1
            pc = (1<<(f-b_+1))-1
            v=0
            for q in range(e-a+1): v|=pc<<q*_x
            pc = (v<<(_x-f-1))<<(_y-e-1)*_x
            mk = (1<<(_x-X-1))<<(_y-Y-1)*_x
            if not (bb&pc)^mk:
                na,pa=pUtPiEcE(_x,_y,bb|pc,uu[:-1],pz+[[b,K,a,b_,e,f]],na,pa,False)
            if na>1: return 2,pa
    else: return na,pa

def main_q():
    get=lambda:map(int,input().split())
    while True:
        xx,yy,NN = get()
        if not xx: break
        BK=sorted([list(get()) for _ in range(NN)])
        SS = [list(get()) for _ in range(yy)]
        yx=[ [SS[j][i],j,i] for j,i in I.product(range(yy),range(xx)) if SS[j][i] ]
        yx=sorted(yx)
        BKyx=[ BK[i]+yx[i][1:] for i in range(NN) ]
        fillbit = ''.join([''.join(['1' if SS[j][i] else '0' for i in range(xx)]) for j in range(yy)])
        ans,pcs=pUtPiEcE(xx,yy,int(fillbit,2),BKyx,[],0,0,False)
        if ans>1: print("NA")
        elif ans:
            pr=[[0]*xx for _ in range(yy)]
            for a,_,y0,x0,y1,x1 in pcs:
                for j in range(y0,y1+1): pr[j][x0:x1+1]=[a]*(x1-x0+1)
            for row in pr: print(*row)
        else: print("NA")

if __name__=="__main__":
    # cProfile.run('main_q()')
    main_q()