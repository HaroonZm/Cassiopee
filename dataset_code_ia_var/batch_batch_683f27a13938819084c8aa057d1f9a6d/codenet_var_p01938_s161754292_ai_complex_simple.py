from sys import stdin
from functools import reduce
from operator import add

AZ = {char: idx for idx, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
s = "A" + stdin.readline().rstrip()

def cmp(a, b):
    return AZ[a] - AZ[b]

pairs = zip(s, s[1:])
increments = map(lambda ab: 1 if cmp(ab[1], ab[0]) <= 0 else 0, pairs)
ans = reduce(add, increments, 0)
print(ans)