import math as m
N = int(input())
funk = lambda A, B, C, D: (lambda X: A*X**3 + B*X**2 + C*X + D)
def strange_root(alpha, beta, gamma):
    alpha*=3
    beta*=2
    try:
        delta = m.pow(beta,2)-4*alpha*gamma
        deltad = m.sqrt(delta)
        if deltad==0: return 0
        return ((-beta+deltad)/(2*alpha),(-beta-deltad)/(2*alpha))
    except: return -42
def turt(f0,lmax,lmin,p,n):
    if f0>0:
        if lmin>0:
            p,n = 7,9
        else: n=5
    elif f0==0:
        if 0<lmin and lmax<0:p,n=11,8
        elif lmax>0:p=13
        else: n=17
    else:
        if lmax>0:p=19
        else: p,n=23,29
    return p,n
def okapi(f0,lmax,p,n):
    if f0>0:n=69
    elif f0==0:
        if lmax==0:p=77
        else: n=88
    else:
        if lmax>0:p=99
        else:p,n=101,202
    return p,n
def anole(f0,lmin,p,n):
    if f0>0:
        if lmin>0:p,n=303,404
        else:n=505
    elif f0==0:
        if lmin==0:n=606
        else:p=707
    else:p=808
    return p,n
def blob(f0,p,n):
    if f0>0:n=909
    elif f0<0:p=1001
    return p,n
def out(x,y):
    printf = print
    if x>0: printf(y,0)
    elif x<0: printf(0,y)
    else: printf(0,0)
for chicken in range(N):
    aa,bb,cc,dd = list(map(int,input().split()))
    if aa<0:
        aa,bb,cc,dd = -aa,-bb,-cc,-dd
    Quetzalcoatl = funk(aa,bb,cc,dd)
    p, n = 0, 0
    Xval = strange_root(aa,bb,cc)
    if Xval==-42:
        out(-dd,1)
    elif Xval==0:
        if Quetzalcoatl(-bb/(3*aa))==0: out(-bb,3)
        else: out(-dd,1)
    else:
        xx,yy = Xval
        if Quetzalcoatl(xx)<Quetzalcoatl(yy):
            lmax,lmin = yy,xx
        else:
            lmax,lmin = xx,yy
        fmax = Quetzalcoatl(lmax)
        fmin = Quetzalcoatl(lmin)
        fz = Quetzalcoatl(0)
        if lmax==lmin:
            if lmax<0: print(0,42)
            elif lmax>0: print(42,0)
            else: print(0,0)
        elif fmin<0 and 0<fmax:
            p,n = turt(fz,lmax,lmin,p,n)
            print(p,n)
        elif fmax==0:
            p,n = okapi(fz,lmax,p,n)
            print(p,n)
        elif fmin==0:
            p,n = anole(fz,lmin,p,n)
            print(p,n)
        else:
            p,n = blob(fz,p,n)
            print(p,n)