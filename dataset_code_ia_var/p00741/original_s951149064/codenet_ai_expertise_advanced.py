import sys
from itertools import product
from collections import deque

sys.setrecursionlimit(1 << 25)

DIRECTIONS = [ (x, y) for x, y in product([-1,0,1], repeat=2) if (x != 0 or y != 0) ]

def dfs_iterative(C, seen, sh, sw, H, W):
    stack = [(sh, sw)]
    while stack:
        h, w = stack.pop()
        for dh, dw in DIRECTIONS:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and C[nh][nw] and not seen[nh][nw]:
                seen[nh][nw] = True
                stack.append((nh, nw))

def main():
    input_iter = iter(sys.stdin.read().split())
    next_int = lambda: int(next(input_iter))
    while True:
        W, H = next_int(), next_int()
        if W == 0 and H == 0:
            break
        C = [ [next_int() for _ in range(W)] for _ in range(H) ]
        seen = [ [False] * W for _ in range(H) ]
        count = 0
        for h, w in product(range(H), range(W)):
            if C[h][w] and not seen[h][w]:
                seen[h][w] = True
                dfs_iterative(C, seen, h, w, H, W)
                count += 1
        print(count)

if __name__ == "__main__":
    main()