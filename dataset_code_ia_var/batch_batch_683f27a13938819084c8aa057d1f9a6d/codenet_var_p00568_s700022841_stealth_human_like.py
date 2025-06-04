# Ok, so first let's grab the dimensions from stdin
h_w = input().split()
H = int(h_w[0])
W = int(h_w[1])

# Build up the grid, line per line
A = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)

M = H * W # maximum possible path length, yeah ? it's not always used though

# create DP table - probably overkill but that's what it wants
dp = []
for i in range(H):
    dp.append([])
    for j in range(W):
        dp[i].append([float('inf')] * M)

dp[0][0][0] = 0  # Start tile is always zero cost

for l in range(1, M): # l is path length here
    flg = False
    for i in range(H):
        for j in range(W):
            # not really sure what this does but from original...
            if i + j > l:
                flg = True
                continue
            # neighbors...
            neighbors = []
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < H and 0 <= nj < W:
                    neighbors.append((ni, nj))
            # initial min value
            m = float('inf')
            for ni, nj in neighbors:
                temp = A[i][j]*(l-1)*2 + A[i][j] + dp[ni][nj][l-1]
                if temp < m:
                    m = temp
            dp[i][j][l] = m
        if flg:
            continue  # oh well, not my favorite, but ok

ans = min(dp[H-1][W-1]) # last cell, best on all valid pathlengths
print(ans)