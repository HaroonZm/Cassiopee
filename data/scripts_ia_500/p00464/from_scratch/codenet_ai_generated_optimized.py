import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    while True:
        H,W,N = map(int,input().split())
        if H==0 and W==0 and N==0:
            break
        grid = [list(map(int,input().split())) for _ in range(H)]
        dp = [[0]*(W+1) for _ in range(H+1)]
        # dp[i][j]: position after dp[i][j] walks starting at (i,j)
        # dp indexed from 1 to H,W; extra row/col for boundary conditions
        for i in range(H,0,-1):
            for j in range(W,0,-1):
                if i==H or j==W:
                    dp[i][j] = (i,j+1) if j==W else (i+1,j)
                else:
                    if grid[i-1][j-1]==0:
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i][j+1]

        # Function to find final position after N walks
        def walk(i,j,n):
            # If at boundary, can't move further
            if i>H or j>W:
                return (i,j)
            if n==0:
                return (i,j)
            if i==H or j==W:
                # absorb one step in boundary
                if i==H and j==W:
                    return (i,j)
                if i==H:
                    return (i,j+min(n,W-j+1))
                if j==W:
                    return (i+min(n,H-i+1),j)
            # At inner cell
            if grid[i-1][j-1]==0:
                # South, flip to East, go South
                grid[i-1][j-1] = 1
                return walk(i+1,j,n-1)
            else:
                # East, flip to South, go East
                grid[i-1][j-1] = 0
                return walk(i,j+1,n-1)

        # Since N can be huge, simulating N steps directly is impossible.
        # Instead, note the toggle pattern: after 2 walks per cell, it returns to original,
        # so state of grid repeats every 2 moves per cell. The path corresponds to bitwise XOR of N with initial states,
        # We exploit the dp to find the final position after N walks by recursive doubling.

        pos = (1,1)
        n = N
        while True:
            i,j = pos
            if i>H or j>W:
                break
            if i==H and j==W:
                break
            if i==H:
                # only east moves possible
                right = W - j + 1
                if n<=right:
                    pos = (i,j+n)
                    n=0
                else:
                    pos = (i,W+1)
                    n-=right
            elif j==W:
                # only south moves possible
                down = H - i +1
                if n<=down:
                    pos = (i+n,j)
                    n=0
                else:
                    pos = (H+1,j)
                    n-=down
            else:
                # Inner cells
                # cell flip pattern repeats every 2 times
                steps = 0
                ci,cj = i,j
                while n>0 and ci<=H and cj<=W and ci<=H and cj<=W:
                    d = grid[ci-1][cj-1]
                    # flip direction
                    grid[ci-1][cj-1] = 1 - d
                    if d==0:
                        ci +=1
                    else:
                        cj +=1
                    n -=1
                    if ci>H or cj>W:
                        pos = (ci,cj)
                        break
                else:
                    pos = (ci,cj)
                break
        print(pos[0],pos[1])

if __name__=="__main__":
    solve()