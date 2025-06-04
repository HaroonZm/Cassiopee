def time_to_add(x, y):
    c = 0
    total = 0
    while x > 0 or y > 0 or c > 0:
        xi = x % 10
        yi = y % 10
        total += xi * yi + c
        s = xi + yi + c
        c = 0 if s < 10 else 1
        x //= 10
        y //= 10
    return total

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    a = list(map(int, input().split()))
    dp = [[(float('inf'), 0) for _ in range(N)] for __ in range(N)]
    for i in range(N):
        dp[i][i] = (0, a[i])
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost_left, val_left = dp[i][k]
                cost_right, val_right = dp[k + 1][j]
                cost_add = time_to_add(val_left, val_right)
                total_cost = cost_left + cost_right + cost_add
                if total_cost < dp[i][j][0]:
                    dp[i][j] = (total_cost, val_left + val_right)
    print(dp[0][N - 1][0])
if __name__ == "__main__":
    main()