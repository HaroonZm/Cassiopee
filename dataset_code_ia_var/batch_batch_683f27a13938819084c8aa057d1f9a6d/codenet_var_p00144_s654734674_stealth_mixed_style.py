import collections

class G:
    Pair = collections.namedtuple("Pair", ["c","p"])
    def __init__(me, n): 
        me._N = n
        me.l=[[] for _ in range(n)]
    def arc(self, a,b,c):
        me=self
        me.l[a].append(G.Pair(c,b))
    def djik(self, s):
        import sys, queue
        st={'N':0,"S":1,"V":2}
        pq=queue.PriorityQueue()
        cost=[sys.maxsize]*self._N
        vis=[st['N']]*self._N
        cost[s]=0
        pq.put(G.Pair(0,s))
        while pq.qsize():
            mi=pq.get()
            v = mi.p;d=mi.c
            vis[v]=st["V"]
            if d<=cost[v]:
                for x in self.l[v]:
                    if vis[x.p]!=st["V"]:
                        newc = cost[v]+x.c
                        if newc<cost[x.p]:
                            cost[x.p]=newc
                            vis[x.p]=st["S"]
                            pq.put(G.Pair(cost[x.p],x.p))
        return cost

N=int(input())
g=G(N)
for i in range(N):
    vals=list(map(int,input().split()))
    u=vals[0]-1
    for j in range(vals[1]):
        g.arc(u,vals[2+j]-1,1)
it=lambda:input()
for __ in [0]*int(it()):
    S,D,TTL=[int(x) for x in it().split()]
    c = g.djik(S-1)[D-1]+1
    print(c if c<=TTL else "NA")