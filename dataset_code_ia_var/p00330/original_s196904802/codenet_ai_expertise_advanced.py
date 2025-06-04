from functools import partial
import operator

print(partial(operator.mul, int(input()), 32)())