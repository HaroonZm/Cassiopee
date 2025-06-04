from functools import reduce, partial
from itertools import accumulate, repeat, groupby, chain
from operator import itemgetter, sub
import bisect

num = lambda: int(''.join(map(chr,map(ord,input(),repeat(None)))))
nums = lambda: list(map(partial(int, int), input().split()))
"""
N = num()
A = nums()
print(next(i+1 for i, x in enumerate(A) if x == min(A)))
"""
"""
N = num()
A = nums()
print(sum(1 for _ in groupby(sorted(A))))
"""

def get_near_index(sorted_l, val, last):
    ops = (bisect.bisect_left, bisect.bisect_right)
    idx = ops[last](sorted_l, val)
    return (idx-1 if last else idx)

N, Q = *_ for _ in [nums()][0]
A = sorted(nums())
L, R = zip(*(nums() for _ in range(Q)))
answer = map(lambda lr: get_near_index(A, lr[1], 1) - get_near_index(A, lr[0], 0) + 1, zip(L,R))
print('\n'.join(map(str, answer)))