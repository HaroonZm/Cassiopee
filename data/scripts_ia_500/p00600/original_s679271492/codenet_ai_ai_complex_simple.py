import sys
input=sys.stdin.readline
import heapq as h, itertools as it

class FancyHeap:
    def __init__(self): self.q=[]
    def push(self,x): h.heappush(self.q,x)
    def pop(self):
        while self.q:
            c,a,b=h.heappop(self.q)
            if vis[a]^vis[b]: return c,a,b
        return None

while 1:
    s,d=map(int,input().split())
    if s==0: break
    vis=[0]*100
    fh=FancyHeap()
    adj=[[] for _ in range(100)]
    for i in range(s):
        vis[i]=1
        w=list(map(int,input().split()))
        for j,cost in enumerate(w):
            if cost>0: fh.push((cost,i,s+j))
    for i in range(d-1):
        row=list(map(int,input().split()))
        for j, cost in enumerate(row, i+1):
            if cost>0:
                adj[s+i].append((s+j,cost))
                adj[s+j].append((s+i,cost))

    res=k=0
    while k<d:
        c,a,b=fh.pop()
        res+=c; k+=1
        a=b if vis[a] else a
        vis[a]=1
        for e,cost in adj[a]:
            if not vis[e]: fh.push((cost,a,e))
    print(res)