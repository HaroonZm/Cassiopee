from functools import reduce
from operator import xor

N, A, B = map(int, input().split())

out = ["Borys", "Alice"]
idx = reduce(lambda acc, x: acc ^ x, [B, -A]) & 1 ^ 1

print(out[idx])