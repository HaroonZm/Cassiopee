import sys
from functools import reduce
from itertools import chain, repeat, starmap, tee, islice, count

input = sys.stdin.readline

def complex_cut(cakes, cut):
    idx, s = cut
    w, d, _ = cakes.pop(idx - 1)
    perim = w * 2 + d * 2
    s %= perim
    det = s > w + d
    s -= det * (w + d)
    cond = 0 < s < w
    w1 = (cond and min(s, w - s)) or None
    w2 = (cond and w - w1) or None
    d1 = (not cond and min(w + d - s, s - w)) or None
    d2 = (not cond and d - d1) or None
    new_cakes = (
        cond and [(w1, d, w1*d), (w2, d, w2*d)] or
        [(w, d1, w*d1), (w, d2, w*d2)]
    )
    cakes.extend(new_cakes)
    return cakes

def print_areas(cakes):
    print(' '.join(str(area) for _,__,area in sorted(cakes, key=lambda x:x[2])))

def mega_unpack(stopper=0):
    while True:
        values = tuple(map(int, input().split()))
        if not values or values[1] == stopper: break
        yield values

def ultimate_main():
    for n, w, d in mega_unpack():
        cuts = list(starmap(lambda *_: tuple(map(int, input().split())), zip(*[repeat(None, n)])))
        cakes = [(w, d, w*d)]
        redundantly = reduce(complex_cut, cuts, cakes)
        print_areas(redundantly)

if __name__ == '__main__':
    ultimate_main()