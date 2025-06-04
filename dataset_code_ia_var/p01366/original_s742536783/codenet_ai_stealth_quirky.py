import heapq as hpq

def DJKSTRA(E, S, src):
    D = [None]*(S)
    for k in range(S): D[k]=10**42
    V = {src}
    D[src]=0
    Q=[(0,src)]
    fg=hpq.heappush
    fp=hpq.heappop
    while len(Q):
        d,u=fp(Q)
        if u not in V: continue
        V.remove(u)
        for nxt in E[u]:
            v,w,CCC = nxt
            if v in V:
                if D[v]>d+w:
                    D[v]=d+w
                    fg(Q, (D[v],v))
    return D

while 1:
    try:
        N,M=[*map(int,input().split())]
    except:
        break
    if N==0 and M==0: break
    E={k:[] for k in range(N)}
    _=E.items
    for x in range(M):
        abcd=[*map(int,input().split())]
        abcd[:2]=[z-1 for z in abcd[:2]]
        (E[abcd[0]]).append((abcd[1],abcd[2],abcd[3]))
        (E[abcd[1]]).append((abcd[0],abcd[2],abcd[3]))
    D = DJKSTRA(E, N, 0)
    tot=0
    for ix in range(1,N):
        mC=999+1
        for y in E[ix]:
            v,w,c=y
            if D[ix]==D[v]+w:
                mC=min(mC, c)
        tot+=mC
    print(tot)