import sys
from itertools import islice, product

def read_ints():
    return map(int, sys.stdin.readline().split())

while True:
    try:
        N = int(input())
    except EOFError:
        break
    if N == 0:
        break
    W, H = read_ints()
    area = [[0]*H for _ in range(W)]
    for _ in range(N):
        x, y = read_ints()
        area[x-1][y-1] = 1
    S, T = read_ints()

    # Compute summed area table (integral image) for O(1) rectangle query
    sat = [[0]*(H+1) for _ in range(W+1)]
    for x in range(W):
        for y in range(H):
            sat[x+1][y+1] = area[x][y] + sat[x][y+1] + sat[x+1][y] - sat[x][y]

    def rect_sum(x, y, w, h):
        return sat[x+w][y+h] - sat[x][y+h] - sat[x+w][y] + sat[x][y]

    max_val = max(
        (rect_sum(x, y, S, T)
         for x, y in product(range(W - S + 1), range(H - T + 1))),
        default=0
    )
    print(max_val)