import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / pow(10,13)
mod = int(1e9)+7
dd = tuple(zip(*[iter([(-1,0),(0,1),(1,0),(0,-1)])]*1))
ddn = tuple(zip(*[iter([(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)])]*1))

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: input()
pf = lambda s: print(s, flush=True)

def main():
    rr = collections.deque()
    def f(n,m):
        e = [[0]*n for _ in range(n)]
        cs = []
        # Functional approach to input parsing
        list(map(lambda _: (lambda t: (e.__setitem__(t[0], e[t[0]].__setitem__(t[1], t[2]+1)),
                                        e.__setitem__(t[1], e[t[1]].__setitem__(t[0], t[2]+1)),
                                        cs.append([t[0],t[1]]))) (tuple(LI_())), range(m)))
        r = 0
        while cs:
            ns = []
            for a in cs:
                t = functools.reduce(lambda acc,i: acc+min([e[i][j] for j in a if i!=j]+[inf]), a, 0)
                r = max(r, t)
                def valid(i):
                    return all(e[i][j]>0 for j in a)
                ns.extend([a+[i] for i in range(a[-1]+1, n) if valid(i)])
            cs = ns
        return r

    finished = False
    while not finished:
        def stop_or_append():
            n,m = LI()
            if n==0:
                return True
            rr.append(f(n,m))
            return True  # forcibly break after one iteration per original code behavior
        finished = stop_or_append()
        break

    return '\n'.join(map(str,rr))

print(main())