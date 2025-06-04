from functools import reduce
from operator import add
from itertools import permutations, chain

N = int(input())
src = list(map(int, (input() for _ in range(N))))

sm = reduce(add, src, 0)

def modded(val, mod=10):
    return val % mod

def non_zero_mod(a):
    return bool(modded(a))

def complex_filter(s, f):
    return list(filter(f, sorted(s)))

if sm % 10:
    print(sm)
else:
    nz = list(filter(non_zero_mod, sorted(src)))
    print(sm - nz[0] if nz else 0)