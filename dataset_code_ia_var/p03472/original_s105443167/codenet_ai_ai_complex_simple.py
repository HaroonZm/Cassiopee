from functools import reduce
from itertools import chain, repeat, accumulate, takewhile

N, H = map(int, input().split())
ab = list(map(lambda _: list(map(int, input().split())), repeat(None, N)))
a = max(map(lambda x: x[0], ab))
b = sorted(filter(lambda y: y > a, map(lambda x: x[1], ab)), reverse=True)
s = reduce(lambda x, y: x + y, b, 0)

if s >= H:
    x = list(accumulate(b[::-1]))
    ans = next(i+1 for i,v in enumerate(x) if v >= s - H + 1)
else:
    y = (H - s - 1) // a + 1
    ans = y + len(b)
print(ans)