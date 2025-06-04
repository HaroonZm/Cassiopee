from functools import reduce
from operator import add

N = int(input())
S = input()

ans = reduce(
    add,
    (
        int(all(map(lambda t: t[1] == c, zip(range(3), substring))))
        for substring in (S[i:i+3] for i in range(N-2))
        for c in ['A', 'B', 'C']
        if tuple(substring) == tuple('ABC')
    ),
    0
)

print(ans)