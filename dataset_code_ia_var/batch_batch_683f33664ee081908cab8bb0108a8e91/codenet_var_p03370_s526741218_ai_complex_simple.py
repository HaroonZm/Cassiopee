from functools import reduce
from operator import add

n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]

sum_m = reduce(add, m)
min_m = min(sorted(m, key=lambda y: (y, -y)))
extra_needed = (x - sum_m)
additional = -(-extra_needed // min_m) if extra_needed > 0 else 0
print(n + additional - (1 if extra_needed % min_m == 0 and extra_needed != 0 else 0))