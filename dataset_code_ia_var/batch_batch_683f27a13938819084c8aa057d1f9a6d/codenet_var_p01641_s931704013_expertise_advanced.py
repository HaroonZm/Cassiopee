from itertools import accumulate, cycle
from operator import itemgetter

s = raw_input()

cell_vals = list(range(30, 121, 10))
ptr = 0
res = []
append = res.append

# Optimized initialization of memory cells, use list comprehension in join
append(''.join(f"{'+'*v}>" for v in range(30,121,10)))
append('<'*10)

for ch in map(ord, s):
    idx = ch//10 - 3
    step = idx - ptr
    if step:
        append(('>' if step > 0 else '<') * abs(step))
    ptr = idx

    diff = ch - cell_vals[ptr]
    if diff:
        append(('+' if diff > 0 else '-') * abs(diff))
        cell_vals[ptr] = ch

    append('.')

print ''.join(res)