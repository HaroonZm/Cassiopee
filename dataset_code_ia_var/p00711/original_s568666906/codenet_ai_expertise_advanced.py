from collections import deque
from operator import add

def solve(dat):
    H, W = len(dat), len(dat[0])
    # Trouver la position de '@'
    si, sj = next((i, j) for i, row in enumerate(dat) for j, c in enumerate(row) if c == '@')
    visited = [[False]*W for _ in range(H)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    stack = deque([(si, sj)])
    visited[si][sj] = True
    reachable = 1

    while stack:
        i, j = stack.pop()
        for di, dj in directions:
            ni, nj = map(add, (i,j), (di,dj))
            if 0 <= ni < H and 0 <= nj < W and dat[ni][nj]=='.' and not visited[ni][nj]:
                visited[ni][nj] = True
                reachable += 1
                stack.append((ni, nj))
    return reachable

def main():
    import sys
    for line in sys.stdin:
        W_H = line.split()
        if not W_H: continue
        W, H = map(int, W_H)
        if not W and not H:
            break
        dat = [sys.stdin.readline().strip() for _ in range(H)]
        print(solve(dat))

if __name__ == "__main__":
    main()