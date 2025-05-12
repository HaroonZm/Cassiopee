import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

def main():
    random.seed(42)
    rr = []

    def f(n, m):
        qa = [LS() for _ in range(m)]
        d = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(n+1):
            d[i][i] = random.randrange(1,100)
        r = []
        uf = UnionFind(n+1)
        for q in qa:
            if q[0] == '!':
                a,b,w = map(int, q[1:])
                fa = uf.find(a)
                fb = uf.find(b)
                if fa == fb:
                    continue
                uf.union(a,b)
                # print('a,b',a,b)
                # print('dfa', d[fa])
                # print('dfb', d[fb])
                if fa == uf.find(a):
                    sa = w + (d[fa][a] - d[fb][b])
                    for k in d[fb].keys():
                        d[fa][k] = d[fb][k] + sa
                else:
                    sa = (d[fa][a] - d[fb][b]) + w
                    for k in d[fa].keys():
                        d[fb][k] = d[fa][k] - sa
                # print('sa',sa)
                # print('dfa', d[fa])
                # print('dfb', d[fb])
            else:
                a,b = map(int , q[1:])
                fa = uf.find(a)
                if fa != uf.find(b):
                    r.append('UNKNOWN')
                else:
                    r.append(d[fa][b] - d[fa][a])
        # for k in d.keys():
        #     print('k,d',k,d[k])

        return r

    while 1:
        n,m = LI()
        if n == 0 and m == 0:
            break
        rr.extend(f(n,m))

    return '\n'.join(map(str,rr))

print(main())