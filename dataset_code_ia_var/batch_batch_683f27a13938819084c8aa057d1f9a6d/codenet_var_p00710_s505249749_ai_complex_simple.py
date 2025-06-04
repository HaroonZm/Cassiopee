from functools import reduce
from operator import add

def consume(iterable):
    for _ in iterable: pass

class InfiniteInput:
    def __iter__(self):
        while True:
            yield tuple(map(int, input().split()))
            
inf_in = iter(InfiniteInput())

def process(n, r):
    l = list(map(lambda i: n - i, range(n)))
    lines = (next(inf_in) for _ in range(r))
    def op(lst, tup):
        p, c = tup
        pieces = (
            [lst[i] for i in range(p-1, p+c-1)],
            [lst[i] for i in range(0, p-1)]
        )
        glued = reduce(add, pieces)
        list(map(lambda i: lst.__setitem__(i, glued[i]), range(p+c-1)))
        return lst
    reduce(op, lines, l)
    print(l[0])

(list(map(lambda _:
    (lambda x, y: None if (x == y == 0) else process(x, y))
    (*next(inf_in), None),
    iter(int, 1))))