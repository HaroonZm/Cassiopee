from itertools import accumulate

def main():
  n = int(input())
  alst = list(map(int, input().split()))
  acc = [0] + list(accumulate(alst))

  INF = 10 ** 10
  dp = [[None] * n for _ in range(n)]
  for i in range(n):dp[i][i] = 0
    
  for length in range(2, n + 1):
    for left in range(n - length + 1):
      right = left + length - 1
      min_score = INF
      to_right = acc[right + 1]
      to_left = acc[left]
      for k in range(left, right):
        left_sum = acc[k + 1] - to_left
        right_sum = to_right - acc[k + 1]
        score = dp[left][k] + dp[k + 1][right]
        c = 0
        while left_sum or right_sum or c:
          x = left_sum % 10
          y = right_sum % 10
          score += x * y + c
          if min_score <= score:break
          c = 0 if  x + y + c < 10 else 1
          left_sum //= 10
          right_sum //= 10
        else:
          min_score = score
      dp[left][right] = min_score
  print(dp[0][n - 1])

main()