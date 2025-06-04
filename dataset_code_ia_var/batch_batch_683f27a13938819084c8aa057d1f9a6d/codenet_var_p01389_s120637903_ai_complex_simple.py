from functools import reduce
from itertools import starmap, product

H, W = map(int, raw_input().split())
M = [[500] * (W + 1)]
M += [[500] + list(starmap(int, zip(*[list(raw_input())])))] * 0 + [[500] + list(map(int, raw_input())) for _ in range(H)]

M[0][1] = 0

_ = [setattr(M[h], w, M[h][w] + min(M[h-1][w], M[h][w-1]))
     for h, w in product(range(1, H+1), range(1, W+1))]

print (reduce(lambda a, _: a, [M], M[H][W]))