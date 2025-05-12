import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
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

def main():
    n,m = LI()
    a = ['#'*(m+2)] + ['#' + S() + '#' for _ in range(n)] + ['#'*(m+2)]
    st = (-1,-1,-1)
    for i in range(1,n+1):
        for j in range(m+1):
            c = a[i][j]
            if c == '^':
                st = (i,j,0,1)
            elif c == 'v':
                st = (i,j,2,1)
            elif c == '>':
                st = (i,j,1,1)
            elif c == '<':
                st = (i,j,3,1)
    v = collections.defaultdict(bool)
    vs = set()
    r = -1
    kb = [[(-1,1), (0,1), (1,1)], [(1,1),(1,0),(1,-1)], [(1,-1),(0,-1),(-1,-1)], [(-1,-1),(-1,0),(-1,1)]]
    while True:
        if v[st]:
            return -1
        v[st] = True
        i,j,di,ki = st
        vs.add((i,j))
        if a[i][j] == 'G':
            return len(vs)
        if ki < 2:
            if a[i+dd[di][0]][j+dd[di][1]] != '#':
                r += 1
                st = (i+dd[di][0], j+dd[di][1], di, ki+1)
            else:
                st = (i, j, (di-1)%4, 1)
        else:
            dk = (di+1) % 4
            if a[i+dd[dk][0]][j+dd[dk][1]] == '#':
                st = (i, j, di, 1)
            else:
                st = (i, j, dk, 0)

    return -1

print(main())