from functools import reduce
from operator import add

A, B, C = map(int, input().split())
parities = list(map(lambda x: x & 1, [A, B, C]))
ANS = reduce(add, parities)

print((lambda k: ["Tem", "Hom"][k >= 2])(ANS))