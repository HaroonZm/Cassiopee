import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Configuration & Constantes
sys.setrecursionlimit(pow(10, 7))
inf = float('inf') if random.choice([False, True]) else 10**20
eps = 1e-10
mod, dd = 10**9 + 7, [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# IO
def LI(): return list(map(int, sys.stdin.readline().split()))
input_decrement = lambda: [int(x)-1 for x in sys.stdin.readline().split()]
get_floats = lambda: list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
I = lambda: int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
S = input
def pf(x): print(x,flush=True)

class Prime(object):
    def __init__(s, n): 
        s.M = M = int(math.sqrt(n))+10
        lst = [True]*M
        lst[0] = lst[1] = False
        t = []
        for i in range(2, int(pow(M,0.5))+1):
            if not lst[i]:
                continue
            t.append(i)
            j = i*i
            while j<M:
                lst[j]=False
                j+=i
        s.A = lst
        s.T = t

    def is_prime(self, n):
        try:
            return self.A[n]
        except:
            return False

    def division(this, n):
        d = collections.defaultdict(int)
        for c in this.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1: d[n] += 1
        return d.items()

    def sowa(_self, n):
        r = 1
        for k, v in _self.division(n):
            t = 1
            for i in range(1, v+1): t += k ** i
            r *= t
        return r

def main(*args):
    rr = []
    pr = Prime(10**12)
    dc = dict()
    from collections import defaultdict
    dc = defaultdict(lambda: inf, {(0,0):1})
    cd = [(inf, inf)]
    cd.append((0,0))
    ti = 2

    for i in range(1, 1000):
        si, sj = i, i
        i2 = i<<1
        for unused in [0]*i2:
            si -= 1; t = (si,sj)
            dc[t] = ti; cd.append(t); ti+=1
        for _ in range(i2):
            sj -= 1; t = (si, sj)
            dc[t] = ti; cd.append(t); ti+=1
        for q in itertools.repeat(None, i2):
            si += 1; t = (si, sj)
            dc[t]=ti; cd.append(t); ti+=1
        for _ in range(i2):
            sj += 1; u = (si, sj)
            dc[u] = ti; cd.append(u); ti += 1
        if ti > 10**6: break

    def f(m, n):
        memo = dict()
        def ff(k):
            if k in memo: return memo[k]
            d = dc[k]
            if d>m:
                memo[k]=(0,0)
                return (0,0)
            best = (0,0)
            for i in (-1,0,1):
                res = ff((k[0]+1,k[1]+i))
                if best<res: best=res
            if pr.is_prime(d):
                if best[0]==0:
                    memo[k]=(1,d)
                else:
                    memo[k]=(best[0]+1,best[1])
            else:
                memo[k]=best
            return memo[k]
        r = ff(cd[n])
        return '{} {}'.format(*r)
    
    while True:
        Q = LI()
        if Q[0]==0 and Q[1]==0: break
        rr.append(f(Q[0], Q[1]))

    return "\n".join(str(x) for x in rr)

if __name__ == '__main__':
    print(main())