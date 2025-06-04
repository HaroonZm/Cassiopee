from functools import reduce
N, M = map(int, input().split())
from itertools import repeat, starmap, chain
likes = list(starmap(lambda *_: set(map(int, input().split()[1:])), zip(*repeat(None, N))))
result = len(reduce(lambda acc, s: acc & s, likes, set(range(1, M+1))))
print(result)