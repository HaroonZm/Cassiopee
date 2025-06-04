from functools import reduce
from itertools import count, islice

def elaborate_input():
    while True:
        yield tuple(map(int, raw_input().split()))
        
def decorative_rectangle(h, w):
    pattern = lambda i: ''.join(['#' if i in (0, h-1) or j in (0, w-1) else '.' for j in range(w)])
    return '\n'.join(map(pattern, range(h)))

stopper = lambda x: all(y == 0 for y in x)
list(
    map(
        lambda t: print(decorative_rectangle(*t)+'\n') if not stopper(t) else exit(),
        takewhile(lambda t: not stopper(t), elaborate_input())
    )
)