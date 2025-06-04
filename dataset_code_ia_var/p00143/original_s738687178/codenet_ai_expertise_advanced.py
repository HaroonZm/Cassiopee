from operator import sub
from functools import partial

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def vector_diff(a, b):
    return [tuple(map(sub, aa, bb)) for aa, bb in zip(a, b)]

def all_same_sign(seq):
    return all(x < 0 for x in seq) or all(x > 0 for x in seq)

input_func = raw_input if 'raw_input' in globals() else input

for _ in range(int(input_func())):
    nums = list(map(int, input_func().split()))
    pts = [tuple(nums[i:i+2]) for i in range(0, 6, 2)]
    v = vector_diff(pts[1:] + pts[:1], pts)
    m = vector_diff([tuple(nums[6:8])] * 3, pts)
    f = vector_diff([tuple(nums[8:10])] * 3, pts)
    crosses_m = list(map(cross, m, v))
    crosses_f = list(map(cross, f, v))
    if all_same_sign(crosses_m) != all_same_sign(crosses_f):
        print("OK")
    else:
        print("NG")