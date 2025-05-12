import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def main():
    a,b,c,d,e,f = LI()
    f += 1
    a *= 100
    b *= 100
    m = [0] * f
    s = [0] * f
    m[0] = 1
    s[0] = 1
    for i in range(f-a):
        if m[i] == 1:
            m[i+a] = 1
    for i in range(f-b):
        if m[i] == 1:
            m[i+b] = 1

    for i in range(f-c):
        if s[i] == 1:
            s[i+c] = 1
    for i in range(f-d):
        if s[i] == 1:
            s[i+d] = 1

    mr = 0
    r = [a,0]
    e = e / (100+e)
    for i in range(0,f):
        if m[i] == 0:
            continue
        for j in range(1,f-i):
            if i+j >= f:
                break
            if s[j] == 0:
                continue
            k = j / (i+j)
            if k > e:
                break
            if k > mr:
                mr = k
                r = [i+j, j]

    return ' '.join(map(str,r))

print(main())