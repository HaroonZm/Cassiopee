from functools import reduce
from itertools import product, chain

n = int(input())
B = list(map(int, input().split()))[1:]

T = reduce(lambda acc, b: acc | (1 << b), B, 0)

f = lambda i: f"{i}:" + ''.join(map(lambda j: f" {j}", filter(lambda j: i & (1 << j), range(n)))) + '\n'

indices = filter(lambda i: (i & T) == T, range(1 << n))

print(''.join(map(f, indices)), end='')