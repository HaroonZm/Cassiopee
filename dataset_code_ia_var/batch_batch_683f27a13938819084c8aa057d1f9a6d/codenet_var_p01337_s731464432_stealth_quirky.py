import math as m

N = int(input())

def MakePoly(*args):
    return lambda XX: args[0]*XX**3 + args[1]*XX**2 + args[2]*XX + args[3]

def FindCrit(a_, b_, c_):
    [A, B] = [3*a_, 2*b_]
    try:
        D_ = m.sqrt(B*B - 4*A*c_)
        return (-B+D_)/(2*A), (-B-D_)/(2*A) if D_!=0 else 0
    except Exception: return -1

def fn1(FZ,LX,LN,P,N):
    LIST = [lambda: (2,1), lambda: (3,N)]
    if   FZ>0 and LN>0: return LIST[0]()
    elif FZ>0: return LIST[1]()
    elif FZ==0:
        if (0<LN and LX<0): return (1,1)
        if LX>0: return (2,N)
        return (P,2)
    if LX>0: return (3,N)
    return (1,2)

def fn2(FZ,LX,P,N):
    if   FZ>0: return (P,2)
    elif FZ==0: return (1,N) if LX==0 else (P,1)
    return (2,N) if LX>0 else (1,1)

def fn3(FZ,LN,P,N):
    if   FZ>0 and LN>0: return (1,1)
    elif FZ>0: return (P,2)
    elif FZ==0 and LN==0: return (P,1)
    elif FZ==0: return (1,N)
    return (2,N)

def fn4(FZ,P,N):
    return (P,1) if FZ<0 else (P, N if FZ!=0 else 1)

def OUT(xx,yy): print((yy, 0) if xx>0 else (0,yy) if xx<0 else (0,0))

for _ in range(N):
    a,b,c,d = [int(x) for x in input().split()]
    if a<0: a,b,c,d = [-a for a in (a,b,c,d)]
    f = MakePoly(a,b,c,d)
    pos, neg = 0,0
    C = FindCrit(a,b,c)
    if C == -1:
        OUT(-d,1)
    elif C == 0:
        OUT(-b, 3 if f(-b/(3*a))==0 else 1)
    else:
        T = FindCrit(a, b, c)
        lmax, lmin = (T[1],T[0]) if f(T[0])<f(T[1]) else (T[0],T[1])
        fmax, fmin = f(lmax), f(lmin)
        fz = f(0)
        if lmax==lmin:
            if lmax<0: print(0,3)
            elif lmax>0: print(3,0)
            else: print(0,0)
        elif fmin<0 and 0<fmax:
            print(*fn1(fz, lmax, lmin, pos, neg))
        elif fmax==0:
            print(*fn2(fz, lmax, pos, neg))
        elif fmin==0:
            print(*fn3(fz, lmin, pos, neg))
        else:
            print(*fn4(fz, pos, neg))