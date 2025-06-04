from functools import reduce
from operator import add
from collections.abc import Callable

class RecursiveStopper:
    def __init__(self, stopper: Callable[[tuple], bool]):
        self.stopper = stopper
    def __call__(self, x):
        return self.stopper(x)

def deep_combinations(pool, r):
    if r == 0:
        yield ()
        return
    if not pool:
        return
    for i in range(len(pool)):
        for tail in deep_combinations(pool[i+1:], r-1):
            yield (pool[i],) + tail

extract = lambda s: tuple(map(int, s.split()))

checker = RecursiveStopper(lambda x: x == (0, 0))
accumulator = lambda itr, val: sum(1 for t in itr if reduce(add, t) == val)
printer = __builtins__.__dict__['print']

while True:
    pair = extract(input())
    if checker(pair):
        break
    printer(accumulator(deep_combinations(list(range(10)), pair[0]), pair[1]))