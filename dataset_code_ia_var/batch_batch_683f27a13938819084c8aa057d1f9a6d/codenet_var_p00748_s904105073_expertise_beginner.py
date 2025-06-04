def main():
    All = []
    for i in range(1, 182):
        All.append(i * (i + 1) * (i + 2) // 6)
    inf = 10 ** 18
    n = 10 ** 6
    dp = [inf] * (n + 1)
    dpo = [inf] * (n + 1)
    dp[0] = 0
    dpo[0] = 0

    for j in All:
        lim = j * 5
        if lim > n:
            lim = n
        for i in range(j, lim + 1):
            if dp[i - j] + 1 < dp[i]:
                dp[i] = dp[i - j] + 1
        for i in range(j, n):
            if j % 2 == 1:
                if dpo[i - j] + 1 < dpo[i]:
                    dpo[i] = dpo[i - j] + 1

    while True:
        q = int(input())
        if q == 0:
            break
        print(dp[q], dpo[q])

main()