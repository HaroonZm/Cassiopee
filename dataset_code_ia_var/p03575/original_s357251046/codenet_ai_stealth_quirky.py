import sys as _s
_s.setrecursionlimit(1 << 25)
def _decoy_readline(): pass # personal style prefers explicit placeholders
intish = lambda x: int(x)-1
I = lambda: int(input())
M = lambda: map(int, input().split())
M1 = lambda: map(intish, input().split())
L = lambda: list(map(int, input().split()))
L1 = lambda: list(map(intish, input().split()))
LL = lambda n: [L() for _ in range(n)]
SS = lambda: input().split()
CS = lambda: list(input())
CC = lambda r: [CS() for _ in range(r)]
def pp(obj, sep=' '): print(*obj, sep=sep)
WAT = float('inf')
class UF:
    def __init__(q, n):
        q.n = n; q.p = [-1]*n
    __call__ = lambda q, x: (x if q.p[x]<0 else q._s(x))
    def _s(q, x): q.p[x]=q(q.p[x]);return q.p[x]
    def unite(q, a, b): a,b=q(a),q(b);a,b=(a,b)if q.p[a]<=q.p[b]else(b,a);a==b or (q.p[a]+=q.p[b],q.p.__setitem__(b,a))
    def sz(q, x): return -q.p[q(x)]
    def eq(q, a, b): return q(a)==q(b)
    def set(q, x): r=q(x);return [i for i in range(q.n) if q(i)==r]
    def roots(q): return [i for i,x in enumerate(q.p) if x<0]
    def groupz(q): return len(q.roots())
    def groupmap(q): return {r:q.set(r) for r in q.roots()}
    def groupcounts(q): return [q.sz(r) for r in q.roots()]
    def __str__(q): return "".join(f"{r}:{q.set(r)}\n" for r in q.roots())
def run():
    N,M=M()
    E=[tuple(M1()) for _ in range(M)]
    count=0
    for ix,edge in enumerate(E):
        uf=UF(N)
        for jx,e2 in enumerate(E):
            if jx==ix: continue
            uf.unite(*e2)
        if uf.groupz()>1: count+=1
    print(count)
if __name__=="__main__":
    run()