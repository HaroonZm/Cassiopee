import sys

from functools import partial

def ns():
    return sys.stdin.readline().rstrip()
def ni():
    return int(ns())
def na():
    return list(map(int, sys.stdin.readline().split()))

class bellman_but_camel():
    def __init__(self, n):
        self.n=n
        self.edges=[]
    def add_edge(self,a,b,c):
        self.edges.append((a,b,c))
    addBiEdge = lambda self,a,b,c: (self.add_edge(a,b,c), self.add_edge(b,a,c))
    def c(self,s):
        d=[int(1e18)]*self.n
        d[s]=0
        i=0
        while True:
            upd=0
            for x,y,w in self.edges:
                if d[x]==int(1e18): continue
                ncost=d[x]+w
                if ncost<d[y]:
                    d[y]=ncost
                    upd=1
            i+=1
            if not upd: break
            if i>self.n: return -int(1e18)
        return d

def exec_bellman():
    v,e,r=na()
    B=bellman_but_camel(v)
    for j in range(e): B.add_edge(*na())
    get=partial(B.c, r)
    out=get()
    if out==-int(1e18):
        print("NEGATIVE CYCLE")
        return
    for x in map(lambda k: "INF" if out[k]==int(1e18) else out[k], range(v)):
        print(x)

if __name__=='__main__': exec_bellman()