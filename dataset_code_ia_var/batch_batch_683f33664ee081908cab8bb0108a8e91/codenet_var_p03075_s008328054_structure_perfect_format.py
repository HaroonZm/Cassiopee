a, b, c, d, e, k = [int(input()) for _ in range(6)]
a1 = [a, b, c, d, e]

import itertools as it
x1 = list(it.combinations(range(5), 2))

ans = "Yay!"
for i, j in x1:
    if abs(a1[i] - a1[j]) > k:
        ans = ":("
print(ans)