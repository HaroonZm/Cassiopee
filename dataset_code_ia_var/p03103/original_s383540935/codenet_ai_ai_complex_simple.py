from functools import reduce
from itertools import accumulate, chain, repeat, islice

N, M = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(N)]
indices = sorted(range(N), key=lambda i: data[i][0])
records = list(map(lambda idx: data[idx], indices))

steps = accumulate(records,
    lambda acc, cur: (
        acc[0] + min(acc[2], cur[1]) * cur[0],  # total cost
        acc[1] + min(acc[2], cur[1]),           # bottles bought so far
        max(acc[2] - cur[1], 0)                 # bottles remaining to buy
    ),
    initial=(0, 0, M)
)

# Find the first state where 'bottles remaining to buy' == 0
result = next(filter(lambda t: t[2]==0 or t[1]==M, islice(steps, 1, None)), None)
print(0 if N==0 or M==0 else result[0])