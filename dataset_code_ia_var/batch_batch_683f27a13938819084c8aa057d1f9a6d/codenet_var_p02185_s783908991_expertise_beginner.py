import sys

mod = 1000000007

def solve():
    s = input()
    t = input()
    n = len(t)
    s_list = [int(c) for c in s]
    t_list = []
    for c in t:
        if c.isdigit():
            t_list.append(int(c))
        else:
            t_list.append(c)

    dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 1
    dp[0][0][1] = 0

    for i in range(n):
        for less in range(2):
            if t_list[i] == "?":
                max_digit = 9 if less else s_list[i]
                for d in range(0, max_digit+1):
                    new_less = less or (d < s_list[i])
                    dp[i+1][new_less][0] = (dp[i+1][new_less][0] + dp[i][less][0]) % mod
                    dp[i+1][new_less][1] = (dp[i+1][new_less][1] + dp[i][less][0]*d + 10*dp[i][less][1]) % mod
            else:
                d = t_list[i]
                if d < 0 or d > 9:
                    continue
                new_less = less or (d < s_list[i])
                if d <= s_list[i]:
                    dp[i+1][new_less][0] = (dp[i+1][new_less][0] + dp[i][less][0]) % mod
                    dp[i+1][new_less][1] = (dp[i+1][new_less][1] + dp[i][less][0]*d + 10*dp[i][less][1]) % mod
                else:
                    if new_less:
                        dp[i+1][new_less][0] = (dp[i+1][new_less][0] + dp[i][less][0]) % mod
                        dp[i+1][new_less][1] = (dp[i+1][new_less][1] + dp[i][less][0]*d + 10*dp[i][less][1]) % mod

    result = (dp[n][0][1] + dp[n][1][1]) % mod
    print(result)

if __name__ == "__main__":
    solve()