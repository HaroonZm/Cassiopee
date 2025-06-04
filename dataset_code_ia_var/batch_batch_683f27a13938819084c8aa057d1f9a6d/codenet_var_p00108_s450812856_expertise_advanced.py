from typing import Tuple, List
from itertools import count
from sys import stdin

def f(x: List[int]) -> Tuple[int, str]:
    a = x
    for c in count():
        b = [a.count(e) for e in a]
        if a == b:
            return c, ' '.join(map(str, a))
        a = b

lines = iter(stdin)
next_line = next(lines)
while True:
    if next_line.strip() == '0':
        break
    x = list(map(int, next(lines).split()))
    c, s = f(x)
    print(c)
    print(s)
    next_line = next(lines, '0')