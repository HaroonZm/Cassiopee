from functools import reduce
from operator import add

N, *lst = open(0).read().split()
N = int(N)
numbers = list(map(int, lst))

def compute_cost(candidate, nums):
    return reduce(add, map(lambda x: (x - candidate) ** 2, nums))

interval = range(-100, 101)
costs = list(map(lambda i: compute_cost(i, numbers), interval))

print(min(costs))