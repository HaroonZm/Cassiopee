from functools import reduce
from operator import add
from itertools import product, combinations
n = int(input())
stash = [float("-inf")]*4
def ins(l, x):
    l.append(-x)
    l.sort()
    l.pop()
list(map(lambda _:ins(stash, int(input())), range(n)))
converted = list(map(lambda x: str(-x), stash))
possible = list(map(lambda ij: int(ij[0]+ij[1]), filter(lambda pair: pair[0]!=pair[1], product(converted, repeat=2))))
print(sorted(possible)[2])