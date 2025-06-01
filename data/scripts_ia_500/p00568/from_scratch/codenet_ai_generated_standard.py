from collections import deque
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def bfs(start_i, start_j):
    dist = [[-1]*W for _ in range(H)]
    dist[start_i][start_j] = 0
    queue = deque([(start_i, start_j)])
    while queue:
        i, j = queue.popleft()
        for ni, nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0 <= ni < H and 0 <= nj < W and dist[ni][nj] == -1 and A[ni][nj] == 0:
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))
    return dist

dist_from_start = bfs(0,0)
if dist_from_start[H-1][W-1] != -1:
    print(0)
else:
    total = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                dist_to_tree = [[-1]*W for _ in range(H)]
                q = deque()
                for si in range(H):
                    for sj in range(W):
                        if A[si][sj] == 0:
                            dist_to_tree[si][sj] = abs(si - i) + abs(sj - j)
                # minimal path from start(0,0) to adjacent no trees cell of this tree
                min_to_tree = -1
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= ni < H and 0 <= nj < W and A[ni][nj] == 0:
                        if dist_from_start[ni][nj] != -1:
                            d = dist_from_start[ni][nj]+1
                            if min_to_tree == -1 or d < min_to_tree:
                                min_to_tree = d
                # minimal path from tree to start(0,0)
                min_from_tree = -1
                for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= ni < H and 0 <= nj < W and A[ni][nj] == 0:
                        if dist_from_start[ni][nj] != -1:
                            d = dist_from_start[ni][nj]+1
                            if min_from_tree == -1 or d < min_from_tree:
                                min_from_tree = d
                dist = min_to_tree + min_from_tree - 2
                total += dist * A[i][j]
    print(total)