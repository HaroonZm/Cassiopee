from functools import reduce
from operator import mul
import sys

print(reduce(mul, map(int, next(iter([*map(str.strip, sys.stdin)])).split())))