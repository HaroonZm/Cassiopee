from functools import reduce
from itertools import chain, repeat, islice, count as icount

def intlist(): return list(map(int, input().split()))
def fancy_index(cnt, p, c): return cnt - (p + c) + 1

while True:
    n, m = intlist()
    if not (n | m): break
    h = list(islice(icount(1), n))
    ops = (tuple(intlist()) for _ in range(m))
    def one_shuffle(deck, op):
        p, c = op
        idx = fancy_index(len(deck), p, c)
        mover = list(islice(deck, idx, idx + c))
        rest = list(islice(deck, 0, idx)) + list(islice(deck, idx + c, None))
        return rest + mover
    h = reduce(one_shuffle, ops, h)
    print(h[-1])