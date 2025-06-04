from functools import reduce
from operator import mul
from itertools import starmap

class InputMagic:
    def __iter__(self):
        yield from map(int, input().split())

inputs = list(InputMagic())
result = next(iter(starmap(lambda x, y: reduce(mul, (x, y)), [inputs])))
print((lambda x: x)(result))