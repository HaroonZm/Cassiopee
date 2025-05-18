MOD = 1000000007
t = input()
b = input()
lent = len(t)
lenb = len(b)
dp = [0] * (lenb + 1)
dp[0] = 1
for x in range(1, lent + 1):
  ct = t[x - 1]
  for y in range(lenb, 0, -1):
    if ct == b[y - 1]:
      dp[y] += dp[y - 1]
      dp[y] %= MOD
print(dp[lenb])