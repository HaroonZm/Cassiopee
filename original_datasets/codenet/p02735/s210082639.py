def solve():
    H, W = map(int, input().split())
    field = [list(input()) for i in range(H)]

    dp = [[0] * W for i in range(H)]
    for h in range(1,H):
        if field[h-1][0] == '.' and field[h][0] == '#':
            dp[h][0] = dp[h-1][0] + 1
        else:
            dp[h][0] = dp[h-1][0]

    for w in range(1,W):
        if field[0][w-1] == '.' and field[0][w] == '#':
            dp[0][w] = dp[0][w-1] + 1
        else:
            dp[0][w] = dp[0][w-1]
    
    for w in range(1,W):
        for h in range(1,H):
            fromUpward = dp[h-1][w]
            if field[h-1][w] == '.' and field[h][w] == '#':
                fromUpward += 1

            fromLeft = dp[h][w-1]
            if field[h][w-1] == '.' and field[h][w] == '#':
                fromLeft += 1
            
            dp[h][w] = min(fromUpward, fromLeft)
    
    ans = dp[H-1][W-1]
    if field[0][0] == '#':
        ans += 1

    print(ans)

if __name__ == '__main__':
    solve()