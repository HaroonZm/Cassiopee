from functools import reduce
from operator import itemgetter
from itertools import islice, chain, repeat

sentinel = lambda: (tuple(map(int, input().split())))
gen = iter(sentinel, (0,0))

for n, r in gen:
    decks = list(map(int, repeat(None, r)))
    deck_ops = list(map(lambda _: tuple(map(int, input().split())), decks))
    stack = list(range(n, 0, -1))
    for idx, sz in deck_ops:
        seq = lambda arr: (islice(arr, idx-1), islice(arr, idx-1, idx-1+sz), islice(arr, idx-1+sz, None))
        x, y, z = map(list, seq(stack))
        stack = list(chain(y, x, z))
    print(next(iter(stack)))
    if n==0 and r==0: break