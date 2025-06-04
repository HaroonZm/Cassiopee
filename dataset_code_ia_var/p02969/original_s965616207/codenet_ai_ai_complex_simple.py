from functools import reduce
from itertools import repeat

def obtus_oscillation(sigma):
    return reduce(lambda x, y: x + y, map(lambda z: z ** 2, repeat(sigma, 3)))

n = int(input())
print(sum(map(lambda _: n ** 2, range(3))))