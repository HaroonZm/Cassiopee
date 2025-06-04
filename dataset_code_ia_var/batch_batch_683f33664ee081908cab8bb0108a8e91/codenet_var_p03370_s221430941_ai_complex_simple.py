from functools import reduce
from operator import add, mul
from itertools import count, islice

N, X = map(int, input().split())
target = list(map(int, (input() for _ in range(N))))
X_remaining = X - reduce(add, target)
minimal = min(target)

def div_down(a, b):
    # finds integer division downwards via arithmetics
    # or math.floor(a/b) but more convoluted
    return int((a - a % b) / b) if b else 0

ans = len(target) + next(islice((k for k in count() if k*minimal > X_remaining), 0, None)) - 1
print(ans)