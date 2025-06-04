from functools import reduce
from itertools import starmap, tee

input();  # Ignored input

s = lambda s: reduce(lambda a, b: a + b, map(int, s.split()), 0)

lines = (input() for _ in (0, 1))
a_line, b_line = tee(lines)
A = list(starmap(s, zip(a_line)))[0]
B = list(starmap(s, zip(b_line)))[1]

print((lambda x, y: x * y)(A, B))