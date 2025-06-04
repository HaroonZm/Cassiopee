import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Début du code excessivement plat

rr = []
mmax = 10**12
M = int(math.sqrt(mmax)) + 10
A = [True]*M
A[0] = False
A[1] = False
T = []
for i in range(2, int(math.sqrt(M))+1):
    if not A[i]:
        continue
    T.append(i)
    for j in range(i*i, M, i):
        A[j] = False

def is_prime(n):
    if n<M:
        return A[n]
    for c in T:
        if n % c == 0:
            return False
    return True

def division(n):
    d = collections.defaultdict(int)
    for c in T:
        while n % c == 0:
            d[c] += 1
            n //= c
        if n < 2:
            break
    if n > 1:
        d[n] += 1
    return d.items()

def sowa(n):
    r = 1
    for k,v in division(n):
        t = 1
        for i in range(1,v+1):
            t += math.pow(k, i)
        r *= t
    return r

dc = collections.defaultdict(lambda: inf)
dc[(0,0)] = 1
cd = [(inf,inf), (0,0)]
ti = 2
for i in range(1, 1000):
    si = i
    sj = i
    i2 = i*2
    for k in range(i2):
        si -= 1
        t = (si, sj)
        dc[t] = ti
        cd.append(t)
        ti += 1
    for k in range(i2):
        sj -= 1
        t = (si, sj)
        dc[t] = ti
        cd.append(t)
        ti += 1
    for k in range(i2):
        si += 1
        t = (si, sj)
        dc[t] = ti
        cd.append(t)
        ti += 1
    for k in range(i2):
        sj += 1
        t = (si, sj)
        dc[t] = ti
        cd.append(t)
        ti += 1
    if ti > 10**6:
        break

inp = sys.stdin
while True:
    x = inp.readline()
    if not x:
        break
    mnlst = x.strip().split()
    if len(mnlst) < 2:
        continue
    m,n = int(mnlst[0]), int(mnlst[1])
    if m == 0 and n == 0:
        break

    fm = {}
    def ff(k):
        if k in fm:
            return fm[k]
        if k not in dc:
            dk = inf
        else:
            dk = dc[k]
        if dk > m:
            fm[k] = (0, 0)
            return (0, 0)
        cm = (0, 0)
        for i in range(-1,2):
            nk = (k[0]+1, k[1]+i)
            ct = ff(nk)
            if cm < ct:
                cm = ct
        if is_prime(dk):
            if cm[0] == 0:
                fm[k] = (1, dk)
            else:
                fm[k] = (cm[0]+1, cm[1])
        else:
            fm[k] = cm
        return fm[k]

    r = ff(cd[n])
    rr.append(f"{r[0]} {r[1]}")

for line in rr:
    print(line)