s1 = input().strip()
s2 = input().strip()

len1 = len(s1)
len2 = len(s2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(len1 + 1):
    dp[i][0] = i
for j in range(len2 + 1):
    dp[0][j] = j

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(
                dp[i - 1][j],    # deletion
                dp[i][j - 1],    # insertion
                dp[i - 1][j - 1] # substitution
            )

print(dp[len1][len2])