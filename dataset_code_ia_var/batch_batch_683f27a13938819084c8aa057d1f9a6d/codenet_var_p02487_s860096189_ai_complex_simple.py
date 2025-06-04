from itertools import cycle, islice, repeat, chain
from functools import partial, reduce

def framed_rectangle(h, w):
    border = ''.join(islice(cycle('#'), w))
    middle = ''.join(chain(islice(cycle('#'), 1), islice(cycle('.'), w-2), islice(cycle('#'), 1)))
    lines = list(chain([border], islice(repeat(middle), max(0, h-2)), [border])) if h > 1 else [border]
    return '\n'.join(lines)

def get_input():
    while True:
        h, w = map(int, raw_input().split())
        if reduce(lambda x,y: x|y, (h == 0, w == 0)):
            break
        yield h, w

for h, w in get_input():
    print partial(framed_rectangle, h, w)()
    print