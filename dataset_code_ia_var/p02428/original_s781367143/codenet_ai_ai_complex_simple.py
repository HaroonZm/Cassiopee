from functools import reduce
from operator import or_

n = int(input())
k, *b_arr = map(int, input().split())

masks = list(map(lambda x: 1 << x, range(n)))
b_mask = reduce(or_, (1 << b for b in b_arr), 0)

def sub_from_i(i):
    return list(filter(lambda idx: i & (1 << idx), range(n)))

list(map(lambda i:
    print(f"{i}: {' '.join(map(str, sub_from_i(i))) if sub_from_i(i) else ''}")
    if (i & b_mask) == b_mask else None,
    range(1 << n)
))