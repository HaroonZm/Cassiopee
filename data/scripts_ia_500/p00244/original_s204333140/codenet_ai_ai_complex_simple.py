from heapq import heappush, heappop
MAX_V = 10**21
def enc(i, j): return i*10 + j
while True:
    n,m = map(int,input().split())
    if n == 0: break
    g = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        a,b,c = map(int,input().split())
        g[a].append((b,c))
        g[b].append((a,c))
    vis = set()
    res = [MAX_V, MAX_V]
    h = []
    heappush(h,(0,1,2))
    while h:
        cost, node, tic = heappop(h)
        idx = 0 if tic==2 else 1
        if tic != 1 and (node, tic) in vis: continue
        if tic != 1:
            vis.add((node,tic))
            if node == n:
                if cost < res[idx]: res[idx] = cost
        if max(res) < MAX_V: break
        for nxt, c in g[node]:
            if tic != 1:
                heappush(h,(cost+c,nxt,tic))
            if tic > 0:
                heappush(h,(cost,nxt,tic-1))
    print(min(res))