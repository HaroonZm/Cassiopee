import math
import collections as col

M = pow(10, 6)
primes = [True] * (M + 1)
primes[0] = primes[1] = False
def sieve(m):
    i = 2
    while i <= int(math.sqrt(m)):
        if primes[i]:
            j = i * i
            while j <= m:
                primes[j] = False
                j += i
        i += 1
sieve(M)

def f(x):
    s = math.sqrt(x)
    if int(s) & 1:
        p = int(s) >> 1
        if x <= int(s)**2 + int(s):
            a = x - int(s)**2
            return (p + 1, p - a)
        else:
            a = x - (int(s)**2 + int(s))
            return (p + 1 - a, -p-1)
    else:
        p = int(s) // 2
        if x <= int(s)**2 + int(s):
            a = x - int(s)**2
            return (-p, -p + a)
        else:
            a = x - (int(s)**2 + int(s))
            return (-p + a, p)

def make_dict():
    D = {}
    G = lambda x: f(x)
    cnt = 1
    for z in [G(b) for b in range(M+1)]:
        D[z] = cnt
        cnt += 1
    return D

COORDS = list(map(f, range(M+1)))
pos_lookup = make_dict()

while True:
    try:
        s = input()
        m, n = [int(a) for a in s.split()]
    except:
        break
    if not (m or n): break
    d = {}
    Q = col.deque([n])
    d[n] = primes[n]
    S = set()
    while Q:
        cur = Q.popleft()
        if cur in S:
            continue
        S.add(cur)
        px, py = COORDS[cur-1]
        for dx in (-1, 0, 1):
            q = pos_lookup.get((px+dx, py+1), M+1)
            if q <= m:
                Q.append(q)
                d[q] = max(d.get(q, 0), d[cur]+primes[q])
    res_num = res_cnt = 0
    keys = list(d.keys())
    for k in keys:
        if primes[k]:
            if d[k] > res_cnt:
                res_cnt, res_num = d[k], k
            elif d[k] == res_cnt and k > res_num:
                res_num = k
    print(res_cnt, res_num)