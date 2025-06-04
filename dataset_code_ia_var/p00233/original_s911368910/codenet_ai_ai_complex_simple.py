from functools import reduce
from itertools import zip_longest, islice, count, chain
import sys

def elaborate(x):
    sign = (x[0] == '-')
    digits = list(map(int, x.lstrip('+-')))
    digits = digits[::-1]
    layers = [
        lambda ds: [0] + ds if sign else ds,
        lambda ds: [d * (-1 if i%2 else 1) for i, d in enumerate(ds)],
    ]
    def complex_arith(ds):
        acc = list(ds)
        i = 0
        while i < len(acc):
            v = acc[i]
            if v < 0 or v >= 10:
                over = -(-v // 10) if v < 0 else v//10
                acc[i] -= over * 10
                if i+1 == len(acc): acc.append(0)
                acc[i+1] += over
            i += 1
        return acc

    nums = reduce(lambda v, f: f(v), layers, digits)
    nums = complex_arith(nums)
    if sign: nums = nums[1:]
    return ''.join(map(str, nums[::-1])).lstrip('0') or '0'

for line in iter(lambda: sys.stdin.readline(), ''):
    s = line.strip()
    if s == '0': break
    print(elaborate(s))