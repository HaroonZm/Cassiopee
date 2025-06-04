import math
import collections as c
def x(a,b,c_):
    return (b[0]-a[0])*(c_[1]-a[1])-(b[1]-a[1])*(c_[0]-a[0])
def hull(ps):
    zz=[];n=len(ps)
    for pp in ps:
        while(len(zz)>1 and x(zz[-1],zz[-2],pp)>0):
            del zz[-1]
        zz+=[pp]
    t=len(zz)
    for ii in range(n-2,-1,-1):
        pp=ps[ii]
        while(len(zz)>t and x(zz[-1],zz[-2],pp)>0): zz.pop()
        zz+=[pp]
    return zz
def ochk(R,S):
    u,cc=0,len(R)
    for e_ in S:
        if u<cc and e_==R[u]:u+=1
    return (u==cc)
def grape():
    while True:
        C,W = (lambda l: (int(l[0]),int(l[1])))(input().split())
        if not C|W: return
        Gs=[[] for _ in'_'*C]
        PP=[[*map(int,input().split())] for _ in[0]*C]
        P1=[p+[i] for i,p in enumerate(PP)]
        P1.sort()
        Q=hull(P1)
        RR=[x[2] for x in Q][:-1]
        j=RR.index(min(RR))
        RR=RR[j:]+RR[:j]
        for _ in'$'*W:
            S,T=[int(_) for _ in input().split()];S-=1;T-=1
            Gs[S]+=[T];Gs[T]+=[S]
        for i in range(C):
            x,y = PP[i]
            Gs[i].sort(key=lambda z:math.atan2(PP[z][1]-y,PP[z][0]-x))
        E=c.defaultdict(list)
        curr=0
        for v in range(C):
            for b,vv in enumerate(Gs[v]):
                pv=v;L=[v]
                while 1:
                    g=Gs[vv]
                    cidx=(g.index(pv)+1)%len(g)
                    if vv==v and cidx==b: break
                    L+=[vv]
                    pv,vv=vv,g[cidx]
                if min(L)==v and not ochk(RR,L):
                    for iii in range(len(L)):
                        a,b=L[iii-1],L[iii]
                        if not a<b:a,b=b,a
                        E[(a,b)]+=[curr]
                    curr+=1
        GG=[[]for _ in'.'*(curr+1)]
        for v in E.values():
            if len(v)==2:a,b=v
            else:a,b=v[0],curr
            GG[a]+=[b];GG[b]+=[a]
        DD=[-9]*(curr+1);DD[curr]=0
        q=c.deque([curr])
        while q:
            vv=q.popleft();d=DD[vv]
            for ww in GG[vv]:
                if DD[ww]!=-9:continue
                DD[ww]=d+1;q.append(ww)
        print(max(DD))
grape()