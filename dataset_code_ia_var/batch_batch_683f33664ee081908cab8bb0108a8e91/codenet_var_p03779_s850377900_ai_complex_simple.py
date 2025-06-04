from functools import reduce
from itertools import count, takewhile

x = int(input())

def accumulate_until(cond, func, start):
    return next(reduce(lambda acc, _: acc+[func(acc[-1])], 
                       takewhile(lambda _, acc=[start]: not cond(acc[-1]), count()), [start]))

n = len(list(takewhile(lambda k: k*(k+1) < 2*x, count())))
print(n)