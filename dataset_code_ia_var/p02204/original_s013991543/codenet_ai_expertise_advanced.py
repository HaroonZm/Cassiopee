from itertools import starmap
from operator import xor

m, n = map(int, input().split())
a = list(map(int, input().split()))

if m == 2:
    parity = [i % 2 for i in range(n)]
    a_parity = [x % 2 for x in a]
    diff = list(starmap(xor, zip(parity, a_parity)))
    ans1 = sum(diff)
    ans2 = n - ans1
    print(min(ans1, ans2))
else:
    from itertools import islice
    ans = sum(x == y for x, y in zip(a, islice(a, 1, None)))
    print(ans)