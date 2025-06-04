from functools import reduce
from itertools import cycle, dropwhile
import operator

# Input and parsing with reduce magic
x, y = reduce(lambda acc, val: (acc[1], int(val)), raw_input().split(), (0, 0))[1], reduce(lambda acc, val: (int(val), acc[0]), raw_input().split(), (0, 0))[0]

# GCD with cycle, dropwhile, and tuple unpacking
gcd_iter = cycle(lambda: (_[1], _[0] % _[1]))
sequence = list(dropwhile(lambda t: t[1] != 0, ((x, y),)))
print sequence[-1][0] if sequence else x