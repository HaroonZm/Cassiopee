from functools import reduce
from operator import mul
import sys

*[lambda x: sys.stdout.write(f"{reduce(mul, [int(x), int(x)], 1)*3}\n")],eval("input()")][0][0]([*(lambda a: (a,))[0](eval("input()")))]