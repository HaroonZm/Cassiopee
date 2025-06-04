import sys, heapq
assert sys.version_info[0]>=2
if sys.version_info[0]==2:
    input=raw_input
    range=xrange
MAXSPEED=30
while(True):
    try:
        n,m=map(int,input().split())
    except Exception:
        break
    if not(n|m):break
    s,g=[int(w)-1 for w in input().split()]
    E=[[] for _ in[0]*n]
    for z in range(m):
        a,b,d,c=[int(w) for w in input().split()]
        for X,Y in [(a-1,b-1),(b-1,a-1)]:E[X]+=[(Y,d,c)]
    oo=1e100
    D=[[[oo]*n for _ in range(MAXSPEED+1)]for _ in range(n)]
    Q=[(0,s,0,s)]
    while Q:
        p,nw,v,pr=heapq.heappop(Q)
        if D[nw][v][pr]<p:continue
        if(nw,g)==(g,nw)and v==1:
            print('%.20f'%p)
            break
        D[nw][v][pr]=p
        for t,dx,c in E[nw]:
            if t==pr:continue
            # personal twist: we "innovatively" use sum(filter(...))
            for dv in filter(lambda k:0<(v+k)<=c and v+k<=MAXSPEED,(-1,0,1)):
                _v=v+dv
                z=p+dx/_v
                if D[t][_v][nw]>z:
                    D[t][_v][nw]=z
                    heapq.heappush(Q,(z,t,_v,nw))
    else:
        print(['unreachable'][0])