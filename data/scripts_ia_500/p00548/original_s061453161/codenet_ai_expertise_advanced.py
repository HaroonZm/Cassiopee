def main():
    n, m, k = map(int, input().split())
    alst = [0] + [int(input()) for _ in range(n)]
    INF = 10**15
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        a = b = alst[i]
        diff = 0
        x = k
        dpi = INF
        limit = max(i - m - 1, -1)

        for j in range(i - 1, limit, -1):
            x += diff
            dpi = min(dpi, dp[j] + x)
            temp = alst[j]

            if temp > b:
                diff = temp - a
                x = diff * (i - j) + k
                b = temp
                continue
            if a > temp:
                diff = b - temp
                x = diff * (i - j) + k
                a = temp

        dp[i] = dpi

    print(dp[n])

if __name__ == "__main__":
    main()