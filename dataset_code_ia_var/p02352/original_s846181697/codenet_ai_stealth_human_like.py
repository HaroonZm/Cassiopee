import math, string, collections, itertools, heapq, array, bisect, copy, functools, fractions, re, sys, random
import time

sys.setrecursionlimit(10**7)  # Oof, hope that's high enough
inf = 10**20
eps = 1e-10  # Eh, floating point business
mod = 1000000007  # classic MOD
mod2 = 998244353  # not always used
dd = [(-1,0),(0,1),(1,0),(0,-1)]  # 4 directions
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]  # diag

def LI():
    # List of ints
    return list(map(int, sys.stdin.readline().split()))
def LLI():
    # List of lists
    lines = sys.stdin.readlines()
    return [list(map(int, line.split())) for line in lines]
def LI_():
    # List of ints (0-index)
    return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    # floating point input
    return float(sys.stdin.readline())
def S():
    return input()
def pf(s):
    print(s, flush=True)
def pe(s):
    print(str(s), file=sys.stderr)
def JA(a, sep):
    # join array
    return sep.join(map(str, a))
def JAA(arr, s, t):
    # 2D join
    return s.join(t.join(map(str, row)) for row in arr)

class RangeAddMin:
    # segment tree for range add & min
    def __init__(self, n):
        # get power of two
        i = 1
        while 2**i < n: i += 1
        self.N = 2**i
        self.A = [0]*(2*self.N)
        self.B = [0]*(2*self.N)  # I hope its enough

    def add(self, a, b, x, k, l, r):
        # a, b: range, x: add, [l,r)
        def _add(k, l, r):
            # print("call", k, l, r)
            if b <= l or r <= a:
                return
            if a <= l and r <= b:
                self.A[k] += x
            else:
                m = (l + r) // 2
                _add(k*2+1, l, m)
                _add(k*2+2, m, r)
                self.B[k] = min(self.B[k*2+1]+self.A[k*2+1], self.B[k*2+2]+self.A[k*2+2])
        _add(k, l, r)

    def query(self, a, b, k, l, r):
        def _query(k, l, r):
            if b <= l or r <= a:
                return inf
            if a <= l and r <= b:
                return self.A[k] + self.B[k]
            m = (l+r)//2
            rl = _query(k*2+1, l, m)
            rr = _query(k*2+2, m, r)
            return min(rl, rr) + self.A[k]
        return _query(k, l, r)

def main():
    n, q = LI()
    queries = [LI() for _ in range(q)]

    # build tree
    ram = RangeAddMin(n)
    output = []
    for query in queries:
        s = query[1]
        t = query[2] + 1
        if query[0] == 0:
            value = query[3]
            ram.add(s, t, value, 0, 0, n)
        else:
            res = ram.query(s, t, 0, 0, n)
            output.append(res)
        # print(query, ram.A, ram.B) # debug

    return JA(output, '\n')  # by lines

#print("Time:", time.time())
print(main())
# if you want to measure time, uncomment the above