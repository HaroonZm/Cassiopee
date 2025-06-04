import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

rr = []
n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(sys.stdin.readline().split())

for pair in a:
    s, t = pair[0], pair[1]
    r1 = 0
    c1 = 1
    for ch in s:
        if ch == 'm':
            r1 += c1 * 1000
            c1 = 1
        elif ch == 'c':
            r1 += c1 * 100
            c1 = 1
        elif ch == 'x':
            r1 += c1 * 10
            c1 = 1
        elif ch == 'i':
            r1 += c1
            c1 = 1
        else:
            c1 = int(ch)
    r2 = 0
    c2 = 1
    for ch in t:
        if ch == 'm':
            r2 += c2 * 1000
            c2 = 1
        elif ch == 'c':
            r2 += c2 * 100
            c2 = 1
        elif ch == 'x':
            r2 += c2 * 10
            c2 = 1
        elif ch == 'i':
            r2 += c2
            c2 = 1
        else:
            c2 = int(ch)
    total = r1 + r2
    result = ''
    if total >= 1000:
        k = total // 1000
        if k > 1:
            result += str(k)
        result += 'm'
        total %= 1000
    if total >= 100:
        k = total // 100
        if k > 1:
            result += str(k)
        result += 'c'
        total %= 100
    if total >= 10:
        k = total // 10
        if k > 1:
            result += str(k)
        result += 'x'
        total %= 10
    if total >= 1:
        k = total
        if k > 1:
            result += str(k)
        result += 'i'
    rr.append(result)

print('\n'.join(map(str, rr)))