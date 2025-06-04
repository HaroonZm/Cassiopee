from functools import reduce
from itertools import count, tee, takewhile

n = int(input())
*a, = map(int, input().split())

def chainfinder(sequence, start=1):
    it = iter(sequence)
    c = start
    while True:
        try:
            val = next(it)
            if val == c:
                yield 1
                c += 1
            else:
                yield 0
        except StopIteration:
            break

if 1 in a:
    # Compose products of indicator function and sum them
    indicators = list(chainfinder(a))
    from operator import add
    cnt = reduce(add, indicators, 0)
    print(n - cnt)
else:
    print(~0)  # bitwise complement of 0 is -1