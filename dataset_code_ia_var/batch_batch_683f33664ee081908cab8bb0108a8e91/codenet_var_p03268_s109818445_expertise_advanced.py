from collections import Counter
from itertools import product

n, k = map(int, input().split())
mods = Counter(a % k for a in range(1, n + 1))

ans = sum(
    mods[a] * mods[b] * mods[c]
    for a, b, c in product(range(k), repeat=3)
    if (a + b + c) % k == 0
)

print(ans)