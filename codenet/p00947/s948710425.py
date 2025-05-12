import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    rr = []

    while True:
        a = [LI() for _ in range(10)]
        sm = {}
        for i in range(10**4):
            c = 0
            t = 10**3
            while t > 0:
                k = i // t % 10
                c = a[c][k]
                t //= 10
            sm[i] = c
        e = collections.defaultdict(set)
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        t = i * 1000 + j * 100 + k * 10 + l
                        for m in range(10):
                            if i != m:
                                u = m * 1000 + j * 100 + k * 10 + l
                                e[t].add(u)
                            if j != m:
                                u = i * 1000 + m * 100 + k * 10 + l
                                e[t].add(u)
                            if k != m:
                                u = i * 1000 + j * 100 + m * 10 + l
                                e[t].add(u)
                            if l != m:
                                u = i * 1000 + j * 100 + k * 10 + m
                                e[t].add(u)
                            if i != j:
                                u = j * 1000 + i * 100 + k * 10 + l
                                e[t].add(u)
                            if j != k:
                                u = i * 1000 + k * 100 + j * 10 + l
                                e[t].add(u)
                            if k != l:
                                u = i * 1000 + j * 100 + l * 10 + k
                                e[t].add(u)

        r = 0
        for i in range(10**4):
            t = sm[i]
            if i % 10 != t and a[sm[i - i % 10 + t]][i % 10] == 0:
                r += 1
                continue
            f = False
            for m in range(10):
                if m == t:
                    continue
                if a[t][m] == 0:
                    f = True
                    r += 1
                    break
            if f:
                continue
            for k in e[i]:
                if a[sm[k]][t] == 0:
                    r += 1
                    break
        rr.append(r)

        break

    return '\n'.join(map(str, rr))

print(main())