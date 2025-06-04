from functools import reduce
import operator

print(
    (lambda s: ["Tem", "Hom"][(reduce(operator.add, map(lambda n: int(n) & 1, s)) > 1)])(input().split())
)