import math as _M, string as _S, itertools as _IT, fractions as _F, heapq as _H, collections as _C, re as _R, array as _A, bisect as _B, sys as _Y, random as _D, time as _T, copy as _CP, functools as _U

_Y.setrecursionlimit(int(1e7))
_INFINITY = 10**20
_EPSILON = 1/1e13
_MODULO = 10**9+7
DIRECTIONS_4 = ((-1,0),(0,1),(1,0),(0,-1))
DIRECTIONS_8 = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

Ints = lambda: list(map(int, _Y.stdin.readline().split()))
IntsZ = lambda: [int(x)-1 for x in _Y.stdin.readline().split()]
Floatz = lambda: [float(x) for x in _Y.stdin.readline().split()]
Words = lambda: _Y.stdin.readline().split()
Int = lambda: int(_Y.stdin.readline())
Float = lambda: float(_Y.stdin.readline())
String = lambda: input()
pr = lambda s='': print(s, end='\n', flush=True)

def main__():
    resu=[]
    
    def inner(n):
        items = []
        for __ in range(n):
            items.append(Ints())
        calc1 = max(x[0]*2+x[1] for x in items)
        calc2 = sum(_IT.chain.from_iterable(items))
        mxx = max(((x[0],-x[1]) for x in items), key=lambda x: (x[0], x[1]))
        idx = items.index([mxx[0], -mxx[1]])
        total_a0 = sum(t[0] for t in items) - mxx[0]
        if total_a0 < mxx[0]:
            real_max = mxx[0]
            dparr = [0]*(real_max+1)
            dparr[total_a0] = True
            for j in range(len(items)):
                if j==idx: continue
                c = items[j][1]
                for i in range(real_max - c, -1, -1):
                    dparr[i+c] |= dparr[i]
            nextmax = 0
            for k in range(real_max, -1, -1):
                if dparr[k]:
                    nextmax = k
                    break
            calc2 += real_max - nextmax
        return max(calc1,calc2)
    
    getit = Int
    while True:
        z = getit()
        if z==0: break
        resu.append(inner(z))
    return '\n'.join(str(x) for x in resu)

if __name__=='__main__':
    pr(main__())