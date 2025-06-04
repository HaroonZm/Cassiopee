from functools import partial
from itertools import cycle, islice, count, starmap, repeat, chain
from operator import add

def infinite_input():
    while True:
        yield tuple(map(int, input().split()))

def fancy_print(h, w):
    symbol = ('#', '.')
    row_gen = lambda r: ''.join(starmap(lambda a,b: symbol[(a+b)%2], zip(repeat(r,w), range(w))))
    print('\n'.join(starmap(row_gen, range(h))), end="\n\n")

breaker = lambda pair: not any(pair)
for dims in filter(lambda x: not breaker(x), infinite_input()):
    fancy_print(*dims)