def solve():
    import sys as syssys
    from itertools import permutations as perms
    from heapq import heapify as hheapify, heappop as hheappop, heappush as hheappush

    fi = syssys.stdin

    N, K = map(int, fi.readline().split())
    F = [[-int(x) for x in fi.readline().split()] for _ in range(N)]
    D = int(fi.readline())
    adj = [[] for _ in range(N)]
    indeg = [0]*N
    for _ in range(D):
        a,b = map(int, fi.readline().split())
        a-=1;b-=1
        adj[a].append(b)
        indeg[b]+=1

    E1 = tuple(map(lambda q: int(q)-1, fi.readline().split()))
    M = dict(zip(perms(range(K)), [[] for _ in range(24)]))
    for i in range(N):
        if indeg[i]==0:
            f = F[i]
            for E in M:
                M[E].append([f[e] for e in E]+[i])

    R = int(fi.readline())
    for k in M:
        hheapify(M[k])

    ans = []
    alive = [True]*N
    for _ in range(R):
        raw = fi.readline().split()
        m, *E2 = map(lambda v:int(v)-1, raw)
        tasks = M[E1]
        while len(ans)<=m:
            while True:
                t = hheappop(tasks)
                if alive[t[-1]]:
                    break
            tn = t[-1]
            alive[tn]=False
            ans.append(str(tn+1))
            for nxt in adj[tn]:
                indeg[nxt]-=1
                if indeg[nxt]==0:
                    ff = F[nxt]
                    for E in M:
                        hheappush(M[E],[ff[e] for e in E]+[nxt])
        E1 = tuple(E2)

    tasks = M[E1]
    while len(ans)<N:
        while True:
            t = hheappop(tasks)
            if alive[t[-1]]:
                break
        tn = t[-1]
        ans.append(str(tn+1))
        for nxt in adj[tn]:
            indeg[nxt]-=1
            if indeg[nxt]==0:
                ff = F[nxt]
                hheappush(tasks,[ff[e] for e in E1]+[nxt])

    print('\n'.join(ans))

solve()