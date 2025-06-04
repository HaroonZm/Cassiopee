import sys
from itertools import accumulate

readline = sys.stdin.readline

N, D = map(int, readline().split())
A = list(map(int, readline().split())) + [0]

# Compute reach using accumulate with custom function
reach = [D]
for a in A:
    prev = reach[-1]
    reach.append(min(prev, abs(prev - a)))

# Compute putter in reverse
putter = [0]
for a in reversed(A):
    p = putter[-1]
    putter.append(p + a if 2 * p + 1 >= a else p)
putter.reverse()

res = ['YES' if reach[i] > putter[i + 1] else 'NO' for i in range(N)]

Q = int(readline())
indices = map(lambda x: int(x) - 1, readline().split())
print('\n'.join(res[i] for i in indices))