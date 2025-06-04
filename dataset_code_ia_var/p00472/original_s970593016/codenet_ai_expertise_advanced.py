from itertools import accumulate, islice, chain
from sys import stdin

MOD = 10**5
read = map(int, islice(stdin, None))
n, m, *rest = read
prefix = list(chain((0,), accumulate(rest[:n-1])))
steps = rest[n-1:]
from operator import add, abs as abs_
from functools import reduce

num = 0
ans = 0
for a in steps:
    nxt = num + a
    ans = (ans + abs_(prefix[num] - prefix[nxt])) % MOD
    num = nxt
print(ans)