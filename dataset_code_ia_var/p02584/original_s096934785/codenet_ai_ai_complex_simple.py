from functools import reduce
from operator import mul

(x, k, d), f = list(map(int, input().split())), lambda x, k, d: abs(reduce(lambda a, b: b[0](a, *b[1:]), [
    (lambda a, d, k: a + d * k, d*((a < 0)*2 -1), k) if abs(a) > d * k else
    (lambda a, d, z: z, None, None)
], x)))

q, r = divmod(abs(x), d)
rest = (k - q) % 2 if k > q else 0
v = ((x > 0) - (x < 0))
ans = abs(x - v * d * min(q, k) - v * d * rest)
print(ans)