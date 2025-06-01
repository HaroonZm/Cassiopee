H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# dp[h][w][l] = minimal time to cut all trees on some path of length l ending at (h,w)
# path length can be at most H*W (visiting all cells)
dp = [[[float('inf')] * (H*W) for _ in range(W)] for __ in range(H)]
dp[0][0][0] = 0  # starting point, path length 0, no cost yet

for length in range(1, H*W):
    skip_rest = False
    for row in range(H):
        for col in range(W):
            if row + col > length:  # can't reach this cell in 'length' steps from (0,0)
                skip_rest = True
                continue
            
            neighbors = []
            for nr, nc in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                if 0 <= nr < H and 0 <= nc < W:
                    neighbors.append((nr,nc))

            best = float('inf')
            for nr, nc in neighbors:
                # The cost formula is a bit weird - might be simulating some timing based on step number?
                cost = grid[row][col]*(length-1)*2 + grid[row][col] + dp[nr][nc][length-1]
                if cost < best:
                    best = cost
            
            dp[row][col][length] = best
        
        if skip_rest:
            continue  # idk if this actually helps, maybe a micro optimization?

# Among all path lengths, find the minimal cost to reach bottom-right corner
print(min(dp[H-1][W-1]))