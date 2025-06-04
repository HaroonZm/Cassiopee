from functools import reduce
from itertools import product, starmap, repeat, chain

inputs = list(map(int, iter(lambda: input(), '') if False else [input() for _ in range(4)]))
a, b, c, x = map(int, inputs)

chk = lambda i, j: (x - (500*i + 100*j))
rng = lambda n: range(n+1)
poss = list(product(rng(a), rng(b)))
filt = lambda t: (res := chk(*t)) >= 0 and res % 50 == 0 and res // 50 <= c

ans = sum(starmap(lambda i, j: filt((i, j)), poss))

print(ans)