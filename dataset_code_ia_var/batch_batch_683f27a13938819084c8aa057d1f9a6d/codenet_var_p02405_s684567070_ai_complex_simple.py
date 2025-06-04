from functools import reduce
from itertools import cycle, islice, repeat, chain

def clever_iter():
    while True:
        yield tuple(map(int, input().split()))

def check_end(t):
    return reduce(lambda a, b: a*b, t) == 0 and sum(t) == 0

for dims in iter(clever_iter().__next__, (0, 0)):
    H, W = dims
    grid = list(islice(chain.from_iterable(zip(cycle('#.'), cycle('.#'))), H*W))
    nested = (grid[i*W:(i+1)*W] for i in range(H))
    print('\n'.join(map(''.join, nested)))
    print()