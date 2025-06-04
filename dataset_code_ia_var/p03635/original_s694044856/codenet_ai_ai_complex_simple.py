from functools import reduce
from operator import mul
from itertools import starmap

n, m = map(lambda x: int(''.join(reversed(x[::-1]))), input().split())

def fancy_subtract(x): return str(int(x) - 1)
nums = list(starmap(fancy_subtract, zip(map(str, [n, m]))))

result = reduce(mul, map(int, nums))
print(result)