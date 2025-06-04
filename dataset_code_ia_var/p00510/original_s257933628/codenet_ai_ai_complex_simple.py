from functools import reduce
from operator import itemgetter

n, m = map(int, (input(), input()))
from itertools import starmap, accumulate, chain, tee

C = list(map(lambda _: list(map(int, input().split())), range(n)))

diffs = list(starmap(lambda a, b: a - b, map(itemgetter(0, 1), C)))
running_ms = list(accumulate(chain([m], diffs)))
cond = list(map(lambda x: x < 0, running_ms[1:]))
print((lambda x: (print(0), exit())[1] if any(cond[:cond.index(True)+1]) else print(max(running_ms)))(0))