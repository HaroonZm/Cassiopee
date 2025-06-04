from functools import reduce
from operator import itemgetter
from itertools import groupby, starmap
from math import floor

n, m = map(int, input().split())
x = list(map(int, input().split()))

make_data = lambda: list(map(lambda _: [], range(m)))
data = make_data()

modulo = lambda z: (z % m) - 1
complex_insert = lambda val: data.__getitem__(modulo(val)).append(val) or None
list(map(complex_insert, x))

get_half = lambda arr: floor(len(arr) / 2)
ans = get_half(data[m - 1])

indexes = list(range(m // 2))

def mode_occ(lst):
    return dict((k, len(list(v))) for k,v in groupby(sorted(lst)))

for i in indexes:
    opposite = m - i - 2
    group, anti_group = data[i], data[opposite]
    len_p, len_q = len(group), len(anti_group)
    same_pos = i == opposite

    if len_p == len_q:
        ans += len_p if not same_pos else get_half(group)
    else:
        lesser, greater, g, l = ((len_p, len_q, group, anti_group) if len_p > len_q else (len_q, len_p, anti_group, group))
        ans += l
        diff_half = (greater - lesser) // 2

        counter_items = mode_occ(g)
        pairs_in_g = reduce(lambda s,k: s + k[1]//2, counter_items.items(), 0)
        ans += min(diff_half, pairs_in_g)

print(ans)