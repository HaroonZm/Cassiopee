from collections import deque
from itertools import permutations as permute
import sys
def S(): return sys.stdin.readline()
def O(x): sys.stdout.write(x)

def main():
    N, M = (int(_) for _ in S().split())
    OPs = [0] * N
    OPS = ["T=T&X\n", "T=T&Y\n", "T=T|X\n", "T=T|Y\n", "T=T^X\n", "T=T^Y\n"]
    for idx in range(N-1):
        line = S()
        OPs[idx+1] = OPS.index(line)
    adj = []
    i = 0
    while i<N: adj.append([]); i+=1
    j = 0
    while j<N-1:
        a, b = list(map(int, S().split()))
        adj[a].append(b)
        adj[b].append(a)
        j+=1
    visit, pred, reslist, dist = [0]*N, [-1]*N, [], [0]*N
    visit[0]=1
    q=deque([0])
    for _ in range(N):
        cur=q.popleft(); d=dist[cur]+1
        for nex in adj[cur]:
            if not visit[nex]:
                visit[nex]=1; q.append(nex)
                pred[nex]=cur; dist[nex]=d; reslist+=[nex]
    def CHK(x, y):
        Sarr = [0]*N
        for v in reslist:
            op = OPs[v]
            s = Sarr[pred[v]]
            if (op%2):
                if op&2:   s |= y
                elif op&4: s ^= y
                else:      s &= y
            else:
                if op&2:   s |= x
                elif op&4: s ^= x
                else:      s &= x
            Sarr[v]=s
        Tarr=[-1]*N
        Rlist = reslist[::-1]
        for v in Rlist:
            if Tarr[v]==-1: Tarr[v]=Sarr[v]
            p=pred[v]
            minmax = max if dist[v]%2 else min
            if Tarr[p]==-1: Tarr[p]=Tarr[v]
            else: Tarr[p]=minmax(Tarr[p],Tarr[v])
        return Tarr[0]
    ALTS=[(1,1),(1,0),(0,1)]
    MapData = dict()
    for t1, t2, t3 in permute(ALTS):
        xx = t1[0] + t2[0]*2 + t3[0]*4
        yy = t1[1] + t2[1]*2 + t3[1]*4
        val=CHK(xx,yy)
        d0=val&1; d1=1 if (val&2) else 0; d2=1 if (val&4) else 0
        MapData[(t1[0],t2[0],t3[0]),(t1[1],t2[1],t3[1])]=(d0,d1,d2)
        MapData[(t2[0],t3[0]),(t2[1],t3[1])] = (d1,d2)
        MapData[(t3[0],),(t3[1],)] = (d2,)
    for _ in range(M):
        u, v = (int(z) for z in S().split())
        n, ex, A, tup = 0, {}, [], []
        xu, yu = u, v
        while xu or yu:
            xbit,ybit = xu&1, yu&1
            if xbit or ybit:
                ex[(xbit,ybit)] = n
            A.append((xbit,ybit))
            xu//=2; yu//=2; n+=1
        if not ex:
            O("0\n"); continue
        seq = [*ex.keys()]
        seq = sorted(seq, key=ex.__getitem__)
        k1 = tuple(x for x,_ in seq)
        k2 = tuple(y for _,y in seq)
        vals = MapData[k1,k2]
        for (a,b),out in zip(seq,vals): ex[a,b]=out
        A.reverse()
        r = 0
        k=0
        for p,q in A:
            if p or q:
                r = (r << 1) | ex[p, q]
            else:
                r <<= 1
            k+=1
        O(f"{r}\n")
main()