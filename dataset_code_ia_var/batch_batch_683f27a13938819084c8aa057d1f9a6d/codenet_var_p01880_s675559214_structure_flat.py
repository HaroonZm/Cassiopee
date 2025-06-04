import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

rr = []

while True:
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    r = -1
    i = 0
    while i < n:
        b = a[i]
        j = i + 1
        while j < n:
            c = a[j]
            t = b * c
            if r >= t:
                j += 1
                continue
            s = str(t)
            ok = True
            k = 0
            while k < len(s)-1:
                if int(s[k]) != int(s[k+1])-1:
                    ok = False
                    break
                k += 1
            if ok:
                r = t
            j += 1
        i += 1
    rr.append(r)
    break

print('\n'.join(map(str, rr)))