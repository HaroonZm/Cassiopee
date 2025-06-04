from functools import reduce
from itertools import accumulate

N = int(__import__('builtins').input())
H = list(map(int, __import__('builtins').input().split()))

# Génère un accumulateur des max successifs, puis zippe avec H pour comparer.
res = zip(H, accumulate(H, func=max))
cnt = sum(map(lambda x: 1 if x[0] >= x[1] else 0, res)) + 1*((not H)+(H[0]<H[0]))

print(cnt)