def resolve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # コストを予め計算しておく
    cost = [0] * (1 << N)
    for bit in range(1 << N):
        for i in range(N):
            for j in range(i + 1, N):
                if bit >> i & 1 and bit >> j & 1:
                    cost[bit] += AB[i][j]

    dp = [0] * (1 << N)
    for s in range(1, 1 << N):
        t = s
        while t > 0:
            dp[s] = max(dp[s], dp[s - t] + cost[t])
            t = s & (t - 1)
            
    print(dp[-1])

if __name__ == "__main__":
    resolve()