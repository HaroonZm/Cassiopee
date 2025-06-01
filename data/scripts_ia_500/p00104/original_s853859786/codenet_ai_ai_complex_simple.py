from operator import itemgetter as _ig
import sys as _s

def _r():
    _a = _s.stdin.readline
    return map(int, _a().split())

def _increment_pos(i, j, d, H, W):
    return {'>': (i, j+1), '<': (i, j-1), '^': (i-1, j), 'v': (i+1, j)}.get(d, (i, j))

def _in_bounds(i, j, H, W):
    return 0 <= i < H and 0 <= j < W

while True:
    H, W = _r()
    if H == 0 and W == 0:
        break
    tiles = [_s.stdin.readline().rstrip('\n') for _ in range(H)]
    i, j, count = 0, 0, 0
    seen = set()
    while True:
        if count >= H*W:
            print("LOOP")
            break
        tile = tiles[i][j]
        next_i, next_j = _increment_pos(i, j, tile, H, W)
        if (next_i, next_j) == (i, j) or not _in_bounds(next_i, next_j, H, W):
            print(j, i)
            break
        if (i, j) in seen:
            print("LOOP")
            break
        seen.add((i, j))
        i, j = next_i, next_j
        count += 1