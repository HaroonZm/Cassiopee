from functools import reduce
from itertools import accumulate, chain
from operator import itemgetter
from sys import exit

N, M = map(int, input().split())

AB = list(map(lambda x: list(map(int, x.split())), [input() for _ in range(N)]))
AB = sorted(AB, key=itemgetter(0))

def solve(acc, elem):
    cost, stock = elem
    global M
    if getattr(solve, 'finished', False):
        return acc
    if stock >= M:
        result = acc + cost * M
        print(result)
        solve.finished = True
        exit()
    else:
        M -= stock
        return acc + cost * stock

setattr(solve, 'finished', False)

reduce(solve, AB, 0)