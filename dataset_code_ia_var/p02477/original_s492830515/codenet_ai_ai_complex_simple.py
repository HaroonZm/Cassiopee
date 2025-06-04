import sys
from functools import reduce
from operator import mul

exec("λ=lambda:map(int,sys.stdin.readline().split())")
print(reduce(mul, tuple(map(int,tuple(λ())))))