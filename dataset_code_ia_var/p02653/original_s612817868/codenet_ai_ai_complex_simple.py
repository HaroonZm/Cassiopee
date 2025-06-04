import math
from functools import reduce
from itertools import accumulate, product, chain, groupby, permutations, combinations
from operator import mul, xor, and_, or_, add, sub
from collections import defaultdict, deque, Counter
from copy import deepcopy

def make_divisors(n):
    # Trouver les diviseurs à l'envers, flat, set, triés sans utiliser sort explicitement
    return sorted(set(chain.from_iterable(
        (i, n//i) for i in range(1, int(math.isqrt(n))+1) if n % i == 0
    )))

def ValueToBits(x, digit):
    # Utilisation de divmod et d'un accumulate
    l = []
    for _ in range(digit):
        x, r = divmod(x, 2)
        l.append(r)
    return l

def BitsToValue(arr):
    # Enfold via reduce avec XOR pour du fun, puis retour add
    return sum(b<<i for i, b in enumerate(arr))

def ZipArray(a):
    # Trie et remplace en une ligne funky
    n = len(a)
    b = [0]*n
    for idx, val in enumerate(sorted(range(n), key=lambda i:a[i])):
        b[val]=idx+1
    return b

def ValueToArray10(x, digit):
    # Format string trick
    return list(map(int, f"{x:0{digit}d}"[-digit:]))

def Zeros(a, b):
    # List comprehension imbriquée, one-liner sans if
    return [[0]*b for _ in range(a)] if b > -1 else [0]*a

def AddV2(v, w):
    # Vectorized sum
    return list(map(add, v, w))

dir4 = list(product([0,1,-1], repeat=2))
dir4 = [d for d in dir4 if abs(d[0])+abs(d[1])==1]

def clamp(x, y, z):
    # sorted slice
    return sorted((y, z, x))[1]

class Bit:
    def __init__(self, n):
        self.size, self.tree = n, [0]*(n+1)
    def sum(self, i):
        # Accumulate for flavor
        return sum(self.tree[j] for j in range(i,0,-(j & -j)))
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def Zaatsu(a):
    # Enumerate unique mapping in a custom way
    invmap = {v:i for i,v in enumerate(sorted(set(x[0] for x in a)))}
    return sorted([[invmap[x[0]], x[1]] for x in a], key=lambda x:x[1])

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.rank = [0]*(n+1)
    def find(self, x):
        path = []
        while self.par[x] != x:
            path.append(x)
            x = self.par[x]
        for node in path: self.par[node] = x
        return x
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b: return
        if self.rank[a] < self.rank[b]: self.par[a]=b
        else:
            self.par[b]=a
            self.rank[a]+=(self.rank[a]==self.rank[b])
    def same_check(self, x, y):
        return self.find(x)==self.find(y)

def rl(x):
    # Generator magic
    yield from range(len(x))

n, aa, bb = map(int, input().split())

a, b = max(aa, bb), min(aa, bb)
p = 1000000007

xs0 = [0]*(n+1)
os0 = [0]*(n+1)
os0[0] = 1

for i in range(b, a-1):
    xs0[i] = sum(os0[i-j] for j in range(b, i+1)) % p
    os0[i] = sum(xs0[i-j] for j in range(1, i+1)) % p

os = [0]*a
for i in range(b, a-2):
    for j, inc in enumerate(range(2, a-i), 2):
        os[i+j] += xs0[i]*(inc-1)

x = [0]*(n+1)
o = [0]*(n+1)
for i in range(b+1, a):
    o[i] = sum(xs0[j] for j in range(b, i)) % p

x[0], o[0] = 1, 1

for i in range(1, n+1):
    x[i] = sum(o[i-j] for j in range(1, min(b, i+1)))
    o[i] = sum(x[i-j] for j in range(1, min(a, i+1)))
    o[i] += sum(x[i-j]*os[j] for j in range(b+2, min(a, i+1)))
    x[i] %= p
    o[i] %= p

for i in range(b+1, a):
    for j in range(b, i):
        o[n] += xs0[j] * x[n-i]
        o[i] %= p

ans = (o[n] + x[n]) % p

beki2 = list(accumulate([1]*5000, lambda acc, _: acc*2%p, initial=1))
ans = (beki2[n] - ans + p) % p

print(ans)