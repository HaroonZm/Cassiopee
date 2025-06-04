import sys
from functools import reduce
from itertools import accumulate, starmap, islice, repeat, chain

stdin = sys.stdin

sys.setrecursionlimit(10**5)

li  = lambda: starmap(int, zip(stdin.readline().split(), repeat(1)))
li_ = lambda: starmap(lambda x: int(x)-1, zip(stdin.readline().split()))
lf  = lambda: starmap(float, zip(stdin.readline().split(), repeat(1)))
ls  = lambda: stdin.readline().split()
ns  = lambda: stdin.readline().rstrip()
lc  = lambda: list(ns())
ni  = lambda: int(stdin.readline())
nf  = lambda: float(stdin.readline())

s, t, q = (ns(), ns(), ni())

trA = lambda iterable: list(accumulate((c == 'A') for c in iterable))
trB = lambda iterable: list(accumulate((c == 'B') for c in iterable))

sa, sb = (list(chain([0], trA(s))), list(chain([0], trB(s))))
ta, tb = (list(chain([0], trA(t))), list(chain([0], trB(t))))

to_interval = lambda arr, l, r: arr[r] - arr[l-1]

calc_num = lambda a, b, arrA, arrB: arrA[b] - arrA[a-1] + 2 * (arrB[b] - arrB[a-1])

for _ in range(q):
    a, b, c, d = list(map(int, stdin.readline().split()))
    sn, tn = calc_num(a, b, sa, sb), calc_num(c, d, ta, tb)
    print(['NO','YES'][(sn%3)==(tn%3)])