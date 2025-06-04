import math as mth, string as S, itertools, fractions, heapq as hp, collections as cl, re as rex, array, bisect, sys, random as rnd, time, copy, functools as ft

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S1(): return input()
def pf(s): print(s, flush=True)

sys.setrecursionlimit(10**7)
inf = float('inf')
eps = 1e-10
mod = 1000000007
DD = [(-1,0),(0,1),(1,0),(0,-1)]
DDN = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def _kosa(*args):
    (x1, y1, _), (x2, y2, _), (x3, y3, _), (x4, y4, _) = args
    tc = (x1-x2)*(y3-y1)+(y1-y2)*(x1-x3)
    td = (x1-x2)*(y4-y1)+(y1-y2)*(x1-x4)
    return tc*td < 0

kosa = lambda a1,a2,b1,b2: _kosa(a1,a2,b1,b2) and _kosa(b1,b2,a1,a2)

distance = lambda x1,y1,x2,y2: mth.sqrt((x1-x2)**2 + (y1-y2)**2)

def distance3(p1, p2, p3):
    def calc(p,q):
        return mth.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
    x1,y1,_ = p1
    x2,y2,_ = p2
    x3,y3,_ = p3
    ax, ay = x2-x1, y2-y1
    bx, by = x3-x1, y3-y1
    try:
        r = (ax*bx + ay*by) / (ax*ax + ay*ay)
    except ZeroDivisionError:
        return calc(p1,p3)
    if r <= 0:
        return calc(p1,p3)
    elif r >= 1:
        return calc(p2,p3)
    else:
        return calc((x1 + r*ax, y1 + r*ay), p3)

def main():
    rr = []
    while 1:
        n = I()
        if not n: break
        def f(n):
            a = []
            for _ in range(n):
                a.append(S1())
            b = [w for idx, w in enumerate(a) if not any(idx != j and w in a[j] for j in range(n))]
            n2 = len(b)
            d = []
            for i in range(n2):
                row=[]
                for j in range(n2):
                    if i==j: row.append(0); continue
                    mx = 0
                    for k in range(1, min(len(b[i]), len(b[j]))):
                        if b[i][-k:] == b[j][:k]:
                            mx = k
                    row.append(mx)
                d.append(row)
            q = cl.defaultdict(int)
            for k in range(n2): q[(1<<k,k)] = 0
            for _ in range(n2-1):
                nq = cl.defaultdict(int)
                for i in range(n2):
                    mask = 1<<i
                    for (s,j),v in q.items():
                        if s&mask: continue
                        ns = s|mask
                        nv = v+d[j][i]
                        if nq[(ns,i)] < nv: nq[(ns,i)] = nv
                q = nq
            fr = max(q.values())
            return sum(map(len,b)) - fr
        rr.append(f(n))
    return '\n'.join(map(str,rr))

if __name__ == '__main__':
    print(main())