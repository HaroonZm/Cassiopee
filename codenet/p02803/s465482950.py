import sys
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

H, W = rl()
M = []
for i in range(H):
    row = rs()
    M.append(row)

import collections
def get_dist(i, j):
    visited = {}
    queue = collections.deque()
    queue.append((i,j,0)) 
    max_l = 0
    while queue:
        i, j, l = queue.popleft()
        if (i,j) in visited: continue
        max_l = max(max_l, l)
        visited[(i,j)] = 1
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < H and 0 <= nj < W and M[ni][nj] != '#':
                queue.append((ni,nj,l+1))
    return max_l

max_move = 0
for i in range(H):
    for j in range(W):
        if M[i][j] == '#': continue
        d = get_dist(i, j)
        max_move = max(max_move, d)
print(max_move)