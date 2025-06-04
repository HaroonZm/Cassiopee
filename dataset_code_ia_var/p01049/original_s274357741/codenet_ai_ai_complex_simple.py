from functools import reduce
from operator import xor
from collections import defaultdict

n = int(input())
a, d = map(int, input().split())

class FancyMem(defaultdict):
    def __missing__(self, key):
        return key
mem = FancyMem()

m = int(input())
for _ in range(m):
    x, y, z = map(int, input().split())
    ops = {
        0: lambda y, z: (mem.update({y: mem[z]}), mem.update({z: mem[y]})),
        1: lambda y, z: mem.update({y: mem[z]})
    }
    [None, ops.get(x, lambda *_: None)(y, z)][1]

ind = int(input())
k = reduce(lambda acc, _: mem[acc], [0], ind)
print((lambda first, step, idx: first + step * (idx - 1))(a, d, k))