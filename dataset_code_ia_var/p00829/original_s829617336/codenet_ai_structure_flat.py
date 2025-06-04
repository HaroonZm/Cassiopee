import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

rr = []
n = int(sys.stdin.readline())
ni = 0

while ni < n:
    ni += 1
    a = []
    while len(a) < 9:
        a += sys.stdin.readline().split()
    t = int(a[-1], 16)
    a = [int(x,16) for x in a[:-1]]
    r = 0
    i = 0
    while i < 32:
        ii = 2**i
        iii = 2**(i+1)
        b = t & ii
        c = 0
        for d in a:
            c += d ^ r
        if (c & ii) != b:
            r += ii
        i += 1
    rr.append('{:0x}'.format(r))

print('\n'.join(str(x) for x in rr))