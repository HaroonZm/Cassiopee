n = int(input())
ID = input()[::-1]
m = int(input())
a_lst = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    c = ID[i]
    mag = 1
    if i % 2 == 1:
        mag = 2
    for j in range(10):
        if c == "*":
            for a_ in a_lst:
                a = a_ * mag
                if a < 10:
                    a_fixed = a
                else:
                    a_fixed = a % 10 + a // 10
                idx = (j + a_fixed) % 10
                dp[i + 1][idx] += dp[i][j]
        else:
            a = int(c) * mag
            if a < 10:
                a_fixed = a
            else:
                a_fixed = a % 10 + a // 10
            idx = (j + a_fixed) % 10
            dp[i + 1][idx] += dp[i][j]
print(dp[n][0])