from functools import partial
from itertools import count, starmap

input_int = partial(map, int, iter(input, '0'))
for n in input_int():
    s = sum(n // 5 ** i for i in range(1, 7))
    print(s)