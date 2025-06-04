from sys import stdin
from itertools import islice

def min_difference(H, W):
    candidates = []

    for h1 in range(1, H):
        rest = H - h1
        h2, h3 = divmod(rest, 2)
        h3 += h2
        w2, w3 = divmod(W, 2)
        w3 += w2

        a = [h1 * W, h2 * W, h3 * W]
        b = [h1 * W, rest * w2, rest * w3]
        candidates.extend([max(a)-min(a), max(b)-min(b)])

    for w1 in range(1, W):
        rest = W - w1
        w2, w3 = divmod(rest, 2)
        w3 += w2
        h2, h3 = divmod(H, 2)
        h3 += h2

        a = [H * w1, H * w2, H * w3]
        b = [H * w1, h2 * rest, h3 * rest]
        candidates.extend([max(a)-min(a), max(b)-min(b)])

    return min(candidates)

H, W = map(int, next(islice(stdin, 1)))
print(min_difference(H, W))