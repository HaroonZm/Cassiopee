from functools import reduce
from operator import xor

n = int(input())
arr = list(map(int, input().split()))

parities = list(map(lambda x: x % 2, arr))
counts = [parities.count(0), parities.count(1)]

result = (lambda z: 0 if 0 in (counts[0], counts[1]) else n - 2 + xor(1, counts[1] % 2))(0)
print(result)