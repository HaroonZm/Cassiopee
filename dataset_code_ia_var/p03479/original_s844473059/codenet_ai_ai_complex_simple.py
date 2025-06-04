from functools import reduce
from itertools import count, takewhile
x, y = map(int, input().split())
def double(n, k): return n * (2 ** k)
steps = [k for k in count(0) if double(x, k) <= y]
ans = max(steps)
print(ans)