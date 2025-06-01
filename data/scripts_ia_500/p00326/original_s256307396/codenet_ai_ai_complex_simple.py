def solve():
    import sys
    f_i = sys.stdin.__iter__()
    N,K=map(int,next(f_i).split())
    F=[list(map(lambda x:-int(x),next(f_i).split())) for _ in range(N)]
    D=int(next(f_i))
    adj=[[] for _ in range(N)]
    indeg=[0]*N
    list(map(lambda _: (lambda a,b: (adj[a-1].append(b-1), indeg.__setitem__(b-1, indeg[b-1]+1))) (*map(int,next(f_i).split())), range(D)))
    )
    E1=tuple(map(lambda x:int(x)-1,next(f_i).split()))
    from itertools import permutations
    M={p:[] for p in permutations(range(K))}
    for i in range(N):
        if indeg[i]==0:
            f=F[i]
            for E in M.keys():
                M[E].append([f[e] for e in E]+[i])
    import heapq
    for k in M:
        heapq.heapify(M[k])
    R=int(next(f_i))
    unprocessed=[True]*N
    ans=[]
    for _ in range(R):
        line=tuple(map(int,next(f_i).split()))
        m=line[0]-1
        E2=tuple(x-1 for x in line[1:])
        tsk=M[E1]
        while len(ans)<=m:
            while True:
                top=heapq.heappop(tsk)
                if unprocessed[top[-1]]:
                    break
            cur=top[-1]
            unprocessed[cur]=False
            ans.append(str(cur+1))
            for nxt in adj[cur]:
                indeg[nxt]-=1
                if indeg[nxt]==0:
                    f=F[nxt]
                    for E in M:
                        heapq.heappush(M[E],[f[e] for e in E]+[nxt])
        E1=E2
    tsk=M[E1]
    while len(ans)<N:
        while True:
            top=heapq.heappop(tsk)
            if unprocessed[top[-1]]:
                break
        cur=top[-1]
        unprocessed[cur]=False
        ans.append(str(cur+1))
        for nxt in adj[cur]:
            indeg[nxt]-=1
            if indeg[nxt]==0:
                f=F[nxt]
                heapq.heappush(tsk,[f[e] for e in E1]+[nxt])
    print('\n'.join(ans))
solve()