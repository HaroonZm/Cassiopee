s = [0] * 100100
dp = [0] * 100100
t = []
for i in range(10):
    t.append(10**i)

while True:
    a, b, p = map(int, raw_input().split())
    if a == 0 and b == 0 and p == 0:
        break
    ans = 0
    for i in range(b - a + 1):
        dp[i] = 1
        m = (a + i) // 10
        while m >= a and m <= b:
            dp[i] += s[m - a]
            dp[i] = dp[i] % p
            m = m // 10
        found = False
        for j in range(10):
            if a + i == t[j]:
                s[i] = dp[i]
                found = True
                break
        if not found:
            if i > 0:
                dp[i] += s[i - 1]
                dp[i] = dp[i] % p
                s[i] = s[i - 1] + dp[i]
                s[i] = s[i] % p
            else:
                s[i] = dp[i]
        ans += dp[i]
        ans = ans % p
    print ans