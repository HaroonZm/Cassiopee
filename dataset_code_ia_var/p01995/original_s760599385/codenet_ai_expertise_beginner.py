def main():
    import bisect
    s = input()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    l = len(s)
    alpha2 = {}
    for i in range(len(alpha)):
        alpha2[alpha[i]] = i
    memo = []
    for i in range(26):
        memo.append([])
    mod = 10 ** 9 + 7
    for i in range(l):
        ch = s[i]
        idx = alpha2[ch]
        memo[idx].append(i)
    dp = []
    for i in range(l + 1):
        dp.append([0] * (l + 1))
    dp[0][l] = 1
    ans = 0
    for i in range(l):
        for j in range(i + 1, l + 1):
            p = dp[i][j]
            if p == 0:
                continue
            for k in range(26):
                # Get the next position of character k on the left and right
                left_list = memo[k]
                x = bisect.bisect_left(left_list, i)
                y = bisect.bisect_right(left_list, j - 1) - 1
                if x > y:
                    continue
                ans += p
                if x < y:
                    mx = left_list[x]
                    my = left_list[y]
                    dp[mx + 1][my] = (dp[mx + 1][my] + p) % mod
            ans = ans % mod
    total = 0
    for row in dp:
        for val in row:
            total += val
        total = total % mod
    ans = (ans + total + mod - 1) % mod
    print(ans)

if __name__ == '__main__':
    main()