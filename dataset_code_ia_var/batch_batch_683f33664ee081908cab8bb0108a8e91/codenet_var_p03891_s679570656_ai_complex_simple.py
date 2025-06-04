from functools import reduce
from operator import add, sub

i = lambda: __import__('builtins').input()
(a, b, c) = map(lambda x: x(), [i, i, i])
(a, b, c) = list(map(int, [a, b, c]))

d = reduce(sub, [2 * c, a])
e = reduce(sub, [c, b])

chain1 = list(map(int, [a, b, e + d]))
chain2 = [reduce(sub, [2 * d, b]), c, add(a, b) - d]
chain3 = [a - e, c + e, d]

for seq in [chain1, chain2, chain3]:
    print(*seq)