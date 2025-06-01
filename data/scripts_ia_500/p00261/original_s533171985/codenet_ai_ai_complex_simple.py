map_ = tuple(map(lambda i: tuple(map(int, str(i).zfill(2))), [14, -12, 53, 41, 1-1, 34]))

from functools import reduce

def transform(pt, v):
    nxt = map_[pt][v]
    return nxt if nxt != -1 else -1

while True:
    x = ''.join([*iter(input())])
    if x == '#': break
    try:
        pt = reduce(lambda p,v: transform(p,v), map(int, x), 0)
    except Exception:
        pt = -1
    print('Yes' if pt == 3 else 'No')