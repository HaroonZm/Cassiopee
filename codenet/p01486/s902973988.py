import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    s = S()
    l = len(s)
    d = collections.defaultdict(int)

    m = {}
    m[''] = True
    def f(s):
        if s in m:
            return m[s]
        if s[0] != 'm' or s[-1] != 'w':
            m[s] = False
            return False
        l = len(s)
        for i in range(1,l-1):
            if s[i] != 'e':
                continue
            if f(s[1:i]) and f(s[i+1:-1]):
                m[s] = True
                return True
        m[s] = False
        return False

    if f(s):
        return 'Cat'
    return 'Rabbit'

print(main())