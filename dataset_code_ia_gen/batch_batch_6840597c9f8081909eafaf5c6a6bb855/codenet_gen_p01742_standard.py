MOD = 10**9 + 7

def count_ways(a, b):
    # Nombre de façons de remplacer '?' dans a et b pour a < b lex (strict)
    n = max(len(a), len(b))
    a = a.ljust(n, 'a')
    b = b.ljust(n, 'a')
    dp = [[0]*2 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for less in range(2):
            if dp[i][less] == 0:
                continue
            a_c = a[i]
            b_c = b[i]
            a_chars = [a_c] if a_c != '?' else [chr(c) for c in range(ord('a'), ord('z')+1)]
            b_chars = [b_c] if b_c != '?' else [chr(c) for c in range(ord('a'), ord('z')+1)]
            for x in a_chars:
                for y in b_chars:
                    if less == 1 or x < y:
                        dp[i+1][1] = (dp[i+1][1] + dp[i][0 if less == 0 else 1]) % MOD
                    elif x == y and less == 0:
                        dp[i+1][0] = (dp[i+1][0] + dp[i][0]) % MOD
    return dp[n][1]

n = int(input())
s = [input() for _ in range(n)]

# dp[i]: nombre de façons de remplir s[0..i] respectant s0 < s1 < ... < si
dp = [0]*(n)
dp[0] = 1
for i in range(1, n):
    ways = count_ways(s[i-1], s[i])
    dp[i] = (dp[i-1] * ways) % MOD

print(dp[n-1])