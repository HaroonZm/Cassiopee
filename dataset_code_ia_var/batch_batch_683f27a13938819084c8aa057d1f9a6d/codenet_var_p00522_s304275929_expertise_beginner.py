INF = 10 ** 20

def main():
    m, n = map(int, input().split())
    manju_list = []
    for i in range(m):
        manju_list.append(int(input()))
    manju_list.sort(reverse=True)

    cum_sum = [0]
    acc = 0
    for i in range(m):
        acc += manju_list[i]
        cum_sum.append(acc)

    c_list = []
    e_list = []
    for i in range(n):
        c, e = map(int, input().split())
        c_list.append(c)
        e_list.append(e)

    dp = []
    for i in range(n + 1):
        dp.append([INF] * (m + 1))
    for i in range(n + 1):
        dp[i][0] = 0

    for x in range(1, n + 1):
        cx = c_list[x - 1]
        ex = e_list[x - 1]
        for y in range(m, 0, -1):
            if y >= cx:
                a = dp[x - 1][y]
                b = dp[x - 1][y - cx] + ex
                if a < b:
                    dp[x][y] = a
                else:
                    dp[x][y] = b
            else:
                a = dp[x - 1][y]
                if y + 1 <= m:
                    b = dp[x][y + 1]
                else:
                    b = ex
                if a < b:
                    dp[x][y] = a
                else:
                    dp[x][y] = b

    answer = -INF
    for i in range(m + 1):
        now = cum_sum[i] - dp[n][i]
        if now > answer:
            answer = now
    print(answer)

main()