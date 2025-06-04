from functools import reduce
from itertools import islice, repeat
from operator import add

def powered_input(_):
    return int(input())

print(reduce(add, map(powered_input, islice(repeat(None), 10))))