def f(n):
    dp = [0] * (n * 10 ** 4 + 1)
    bs = [list(map(int, input().split())) for _ in range(n)]
    bs.sort(key=lambda x: x[0] + x[1])
    for w, s, v in bs:
        for i in range(w + s, w - 1, -1):
            dpw = dp[i - w] + v
            if dpw > dp[i]:
                dp[i] = dpw
    print(max(dp))

n = int(input())
f(n)