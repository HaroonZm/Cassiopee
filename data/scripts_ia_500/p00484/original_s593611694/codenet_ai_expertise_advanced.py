from itertools import accumulate
from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**7)
n, k = map(int, input().split())
books = [[] for _ in range(10)]

for _ in range(n):
    c, g = map(int, input().split())
    books[g - 1].append(c)

books_acc = [list(accumulate([0] + sorted((c + 2*i for i, c in enumerate(reversed(genre))), reverse=True))) for genre in books]

@lru_cache(None)
def combi(g=0, remain=k):
    if g == 10:
        return 0
    acc = books_acc[g]
    max_i = min(remain, len(acc)-1)
    return max((acc[i] + combi(g + 1, remain - i) for i in range(max_i + 1)), default=0)

print(combi())