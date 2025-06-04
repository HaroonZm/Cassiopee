import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

rr = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    n_t_l_b = [int(x) for x in line.split()]
    if not n_t_l_b or n_t_l_b[0] == 0:
        break
    n, t, l, b = n_t_l_b
    ls = set()
    if l > 0:
        for _ in range(l):
            ls.add(int(sys.stdin.readline()))
    bs = set()
    if b > 0:
        for _ in range(b):
            bs.add(int(sys.stdin.readline()))
    r = []
    for _ in range(t+2):
        r.append([0] * (n+1))
    r[0][0] = 1
    i = 0
    while i < t:
        j = 0
        while j < n:
            if r[i][j] != 0:
                k = 1
                while k <=6:
                    nj = j + k
                    if nj > n:
                        nj = n - (nj - n)
                    ni = i + 1
                    if nj in ls:
                        ni += 1
                    if nj in bs:
                        nj = 0
                    if nj == n:
                        ni = t
                    r[ni][nj] += r[i][j] / 6.0
                    k += 1
            j += 1
        i += 1
    rr.append('{:0.9f}'.format(r[t][n]))
print('\n'.join(map(str, rr)))