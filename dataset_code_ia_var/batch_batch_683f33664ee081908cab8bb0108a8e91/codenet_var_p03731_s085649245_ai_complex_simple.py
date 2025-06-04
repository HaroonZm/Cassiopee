from functools import reduce
from operator import add

n, t = map(int, input().split())
lst = list(map(int, input().split()))
lst.append(10 ** 12)
pairs = zip(lst, lst[1:])
increments = map(lambda ab: min(t, ab[1] - ab[0]), pairs)
print(reduce(add, increments, 0))