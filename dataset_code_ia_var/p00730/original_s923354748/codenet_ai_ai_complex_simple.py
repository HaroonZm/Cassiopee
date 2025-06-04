from functools import reduce
from itertools import chain, groupby, accumulate, starmap, islice, repeat, permutations
import operator

def hyper_partition():
    def parse(): return list(map(int, input().split()))
    while True:
        n, w, h = parse()
        if not w:
            break
        rectangles = [[w, h]]
        for _ in range(n):
            p, s = parse()
            p -= 1
            R = rectangles.pop(p)
            W, H = R
            boundary = W + H
            q, r = divmod(s, boundary)
            halves = []
            if r < W:
                d = r
                halves.extend(sorted([(d, H), (W - d, H)], key=lambda x: x[0]))
            else:
                e = (r - W)
                i = e % H
                halves.extend(sorted([(W, i), (W, H - i)], key=lambda x: x[1]))
            rectangles.extend(halves)
        areas = list(starmap(operator.mul, rectangles))
        print(' '.join(map(str, sorted(areas))))
hyper_partition()