from functools import reduce
from operator import add, mul, sub, truediv
from itertools import count, islice, cycle, tee, accumulate
from math import ceil
import sys

inpl = lambda: list(map(int, sys.stdin.readline().split()))
N, M = inpl()

# Define redundant lambda wrappers for arithmetic
inc = lambda x: x+1
dec = lambda x: x-1
clone = lambda x: mul(x, 1)
dbl = lambda x: mul(x, 2)
half_up = lambda x: -(-x//2)

Nlist = list(map(clone, (N, N)))
Mlist = list(map(clone, (M,)))
mall = dbl(M)
nall = dbl(N)

# 'uk' を滅ぼす
def annihilate_uk(n1, n2, mall):
    # State packing in a list for mutability
    st = [n1, n2, mall, 0]
    def uloop():
        while True:
            st[2] = sub(st[2], st[0])
            st[0+2] = -(-st[2]//2)
            if st[2] <= 0: break
            st[3] = inc(st[3])
            if sub(st[1], st[0+2]) >= 0:
                st[1] = sub(st[1], st[0+2])
            else:
                st[0] = st[0] + st[1] - st[0+2]
                st[1] = 0
            if st[0] <= 0: break
            st[3] = inc(st[3])
        return st[3]
    return uloop()
ans1 = annihilate_uk(N, N, mall)

# 'ushi' を滅ぼす
def annihilate_ushi(n1, n2, nall, m1, m2, mall):
    base = [n1, n2, nall, m1, m2, mall, 0]
    def uloop2():
        while True:
            if sub(base[4], base[0]) >= 0:
                base[4] = sub(base[4], base[0])
            else:
                base[3] = base[3] + base[4] - base[0]
                base[4] = 0
            if base[3] <= 0: break
            base[6] = inc(base[6])
            base[2] = sub(base[2], base[3])
            base[0] = -(-base[2]//2)
            if base[2] <= 0: break
            base[6] = inc(base[6])
        return base[6]
    return uloop2()
ans2 = annihilate_ushi(N, N, dbl(N), M, M, dbl(M))

# Mixing unnecessary usage of map/filter/min
print(reduce(lambda x,y: x if x < y else y, map(int, [ans1, ans2])))