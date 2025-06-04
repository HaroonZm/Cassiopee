import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf, eps, mod = 10**20, 1.0 / 10**10, 10**9+7

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
LF = lambda: list(map(float, sys.stdin.readline().split()))
LS = lambda: sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
S = lambda: input()

def main():
    a,b,c,d,e,f = LI()
    f = functools.reduce(lambda x,y: x+y, [f,1])
    a,b = map(lambda x: x*100, (a,b))

    m = [0] * f
    s = [0] * f

    list(map(lambda x: m.__setitem__(x,1), [0]))
    list(map(lambda x: s.__setitem__(x,1), [0]))

    list(map(lambda delta: [m.__setitem__(i+delta,1) for i in range(f-delta) if m[i]==1], [a,b]))
    list(map(lambda delta: [s.__setitem__(i+delta,1) for i in range(f-delta) if s[i]==1], [c,d]))

    e = 1.0 * e / (100+e)
    results = list()
    for i,mi in filter(lambda x: x[1]==1, enumerate(m)):
        for j,sj in filter(lambda x: x[0]>0 and x[1]==1, enumerate(s)):
            total = i + j
            if total >= f: continue
            conc = j/(i+j)
            if conc > e: continue
            results.append((conc, total, j))
    if results:
        _, w, s_ = max(results, key=lambda x: x[0])
        res = [w, s_]
    else:
        res = [a, 0]
    return ' '.join(map(str,res))

print(main())