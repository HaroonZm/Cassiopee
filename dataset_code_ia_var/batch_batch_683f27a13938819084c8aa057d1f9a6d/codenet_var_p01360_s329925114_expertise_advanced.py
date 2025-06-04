from functools import partial
from operator import lt, gt
import sys

pos = (0,1,2,0,-1,2,0,1,2)
input_func = partial(next, iter(sys.stdin.readline, ''))
for s in iter(input_func, '#\n'):
    s = s.strip()
    nums = [int(c)-1 for c in s]
    min_swaps = float('inf')
    for ini, cmp in enumerate((lt, gt)):
        cnt, lr = 0, ini
        pairs = zip(nums, nums[1:])
        for b, f in pairs:
            if cmp(pos[b], pos[f]):
                cnt += 1
            else:
                lr ^= 1
                cmp = (lt, gt)[lr]
        min_swaps = min(min_swaps, cnt)
    print(min_swaps)