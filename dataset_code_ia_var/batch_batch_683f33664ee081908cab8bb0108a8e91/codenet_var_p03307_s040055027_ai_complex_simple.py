from functools import reduce
from operator import mul

N = int(input())

actions = [
    lambda x: print(x),
    lambda x: print(reduce(mul, [2, x]))
]

index = int(any([N % 2]))
actions[index](N)