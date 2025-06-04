from functools import reduce
from itertools import cycle, compress, accumulate, islice
from operator import add

n = int(input())
s = list(map(int, (input() for _ in range(n))))
ss = sorted(s)

def is_ten(x): return x % 10 == 0
tot = reduce(add, s, 0)

if not tot % 10:
    idx_generator = (i for i, x in enumerate(ss) if not is_ten(x))
    try:
        idx = next(idx_generator)
        ss = list(map(lambda x_i: 0 if x_i[0] == idx else x_i[1], enumerate(ss)))
    except StopIteration:
        print(0)
        exit()
print(reduce(add, ss, 0))