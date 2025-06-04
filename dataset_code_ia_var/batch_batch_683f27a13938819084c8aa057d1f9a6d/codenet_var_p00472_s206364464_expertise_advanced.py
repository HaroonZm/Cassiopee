from itertools import accumulate, islice, chain
from sys import stdin

MOD = 100000
read = stdin.readline

n, m = map(int, read().split())
lng = list(accumulate(chain([0], (int(read()) for _ in range(n-1)))))
indices = (int(read()) for _ in range(m))

from functools import reduce

def compute_sm(lng, indices):
    def step(acc, delta):
        i, s = acc
        j = i + delta
        s = (s + abs(lng[i] - lng[j])) % MOD
        return (j, s)
    return reduce(step, indices, (0, 0))[1]

print(compute_sm(lng, indices))