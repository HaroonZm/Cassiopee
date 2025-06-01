from math import atan2
from collections import defaultdict, deque
def cross(a,b,c):
    return sum(map(lambda x,y,z:(y-x)*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0]),[a],[b],[c]))
def convex_hull(ps):
    from functools import reduce
    def proceed(qs,p):
        while len(qs)>1 and cross(qs[-1], qs[-2], p)>0: qs.pop()
        qs.append(p)
        return qs
    qs1=reduce(proceed, ps, [])
    qs2=reduce(proceed, reversed(ps[:-1]), qs1)
    return qs2
def outer_check(R,S):
    it=iter(R); cur=next(it,None)
    for e in S:
        if cur==e: cur=next(it,None)
    return cur is None
def cyclic_slice(lst,start):
    return lst[start:]+lst[:start]
def sort_key_factory(P,i):
    x0,y0=P[i]
    def f(p):
        return atan2(P[p][1]-y0,P[p][0]-x0)
    return f
def rotate_index(xs, val):
    return next(i for i,v in enumerate(xs) if v==val)
def min_and_rotate(xs):
    m=min(xs)
    p=rotate_index(xs,m)
    return cyclic_slice(xs,p)
from operator import itemgetter
while 1:
    C,W=map(int,input().split())
    if C==0and W==0:break
    G0=[[]for _ in range(C)]
    P=[list(map(int,input().split()))for _ in range(C)]
    P0=[p+[i]for i,p in enumerate(P)]
    P0.sort(key=itemgetter(0,1))
    Q0=convex_hull(P0)
    R=[x[2]for x in Q0][:-1]
    R=min_and_rotate(R)
    for _ in range(W):
        s,t=map(int,input().split())
        s-=1;t-=1
        G0[s].append(t)
        G0[t].append(s)
    for i in range(C):
        G0[i].sort(key=sort_key_factory(P,i))
    E=defaultdict(list)
    cur=0
    for v in range(C):
        for b,v0 in enumerate(G0[v]):
            prv=v
            st=[v]
            while 1:
                g=G0[v0]
                c=(g.index(prv)+1)%len(g)
                if v0==v and c==b:break
                st.append(v0)
                prv,v0=v0,g[c]
            if min(st)==v and not outer_check(R,st):
                for i in range(len(st)):
                    p,q=st[i-1],st[i]
                    if not p<q:p,q=q,p
                    E[(p,q)].append(cur)
                cur+=1
    G=[[]for _ in range(cur+1)]
    for es in E.values():
        if len(es)==2:a,b=es
        else:a=es[0]; b=cur
        G[a].append(b)
        G[b].append(a)
    D=[-1]*(cur+1)
    D[cur]=0
    que=deque([cur])
    while que:
        v=que.popleft()
        d=D[v]
        for w in G[v]:
            if D[w]!=-1:continue
            D[w]=d+1
            que.append(w)
    print(max(D))