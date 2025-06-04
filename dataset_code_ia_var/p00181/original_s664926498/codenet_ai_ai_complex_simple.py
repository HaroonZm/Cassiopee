from itertools import islice, count, repeat, takewhile, accumulate, chain
from functools import reduce, lru_cache
from operator import add, gt

def readints():
    return list(map(int, input().split()))

def batched(iterable, n):
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch

for _ in repeat(None):
    m, n = readints()
    if not any([m, n]):
        break
    books = list(map(int, islice((int(input()) for _ in count()), n)))
    L = min(books)
    R = 10 ** 7
    @lru_cache(maxsize=None)
    def capacity(w):
        return reduce(lambda acc, b: acc + 1 if acc < 0 or (sum(books[slice(acc, acc+1)]),)[0] > w else acc, books, 0)
    def cnt_partitions(w):
        return len(list(takewhile(lambda t: t[1] <= w, zip(count(1), accumulate(books, lambda x, y: (x if x + y <= w else 0) + y))))) + sum(1 for a in accumulate(books, lambda x, y: 0 if x + y > w else x + y) if a == 0)
    def check(w):
        c = 1
        s = 0
        for b in books:
            s += b
            if s > w:
                c += 1
                s = b
        return c
    while L < R:
        mid = (L + R) // 2
        _cnt = reduce(lambda c_s, b: (c_s[0]+1, b) if c_s[1]+b > mid else (c_s[0], c_s[1]+b), books, (1, 0))[0]
        L, R = ((mid + 1, R) if _cnt > m else (L, mid))
    print(L)