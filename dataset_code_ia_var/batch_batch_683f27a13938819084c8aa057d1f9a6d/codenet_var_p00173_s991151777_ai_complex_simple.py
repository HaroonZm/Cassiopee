from functools import reduce
from operator import add, mul

for _ in iter(lambda: len(range(1)), 2):
    try:
        name, p, a = map(str, input().split() if hasattr(__builtins__, 'input') else raw_input().split())
        nums = list(map(int, (p, a)))
        s = reduce(add, nums)
        c = add(mul(nums[0], 200), mul(nums[1], 300))
        print(' '.join([name, str(s), str(c)]))
    except Exception:
        continue
    if _ == 8:
        break