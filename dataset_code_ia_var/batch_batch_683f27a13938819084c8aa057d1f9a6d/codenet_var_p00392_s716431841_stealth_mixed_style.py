import sys
from collections import defaultdict as dd

def get_primes(limit):
    flag = [1] * (limit+1)
    flag[0:2] = [0, 0]
    i = 2
    while i*i <= limit:
        if flag[i]:
            for k in range(i*i, limit+1, i):
                flag[k] = 0
        i += 1
    return [x for x, y in enumerate(flag) if y]

def setup_solvers():
    P = get_primes(100000)
    S = [[] for _ in (0,)*100001]
    for p in P:
        idx = p
        while idx <= 100000:
            S[idx].append(p)
            idx += p
    return S

class UF:
    def __init__(self, N):
        self.par = [i for i in range(N)]
    def get(self, x):
        if self.par[x] != x:
            self.par[x] = self.get(self.par[x])
        return self.par[x]
    def connect(self, x, y):
        self.par[self.get(x)] = self.get(y)

def main():
    S = setup_solvers()
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    u = UF(100001)
    for idx, num in enumerate(lst):
        roots = [u.get(s) for s in S[num]+[num]]
        if roots:
            anchor = min(roots)
            for v in S[num]:
                u.connect(v, anchor)
            u.connect(num, anchor)
    buckets = dd(set)
    enumerate(lambda t: buckets[u.get(t[1])].add(t[0]), enumerate(lst))
    arr = sorted(lst)
    for ix, val in enumerate(arr):
        if ix not in buckets[u.get(val)]:
            print(0)
            return
    print(1)

main()