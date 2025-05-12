import sys

sys.setrecursionlimit(10000)

n = int(input())
A = [int(input()) for i in range(n)] * 3
dp = [[-1 for i in range(n * 2)] for j in range(n * 2)]

def dfs(i,j):
  #if (j - i > n - 1):undefined
  if dp[i][j] != -1:
    pass
  elif (j - i == n - 1):
    dp[i][j] = 0
  elif (j - i) % 2 == 0:
    if A[i - 1] > A[j + 1]:
      dp[i][j] = dfs(i - 1, j)
    else:
      dp[i][j] = dfs(i, j + 1)
  else:
    dp[i][j] = max(dfs(i - 1, j) + A[i - 1], dfs(i, j + 1) + A[j + 1])
  return dp[i][j]
ans = 0
for i in range(n):
  ans = max(ans, dfs(i,i) + A[i])
print(ans)