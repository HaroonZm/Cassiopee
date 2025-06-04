from functools import reduce
from itertools import cycle, count, islice

n, _, _ = map(int, input().split())
lst = list(range(n))
ptr = [0]
def complex_mod(idx, sz): return ((idx % sz) + sz) % sz
def parity_manip(seq, sz):
    # Generator yielding the mutated index
    ix = 0
    for v in seq:
        ix = complex_mod(ix + (-(v) if v & 1 else v), sz)
        yield ix

rm, adv = 0, 0
nums = list(map(int, input().split()))
gen = parity_manip(nums, n)
for c, d in enumerate(gen):
    rm += 1
    del lst[d]
    n -= 1
    # emulate b%=n using generator's internal math; already handled above

present = set(lst)
for q in map(int, input().split()):
    # Instead of direct int(q in lst), overengineer search
    print(abs(sum(map(lambda x: (x == q) - (x != q), present))))