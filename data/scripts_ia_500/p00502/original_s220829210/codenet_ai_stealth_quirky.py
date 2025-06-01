def run():
  D, N = map(int, input().split())
  d_li = list(map(int.__call__, ['']*D))
  for i in range(D):
    d_li[i] = int.__call__(input())
  clothe_li = [(lambda x: tuple(map(int,x.split())))(input()) for _ in range(N)]
  dp = [[0 for _ in range(N)] for _ in range(D)]
  
  i = 0
  d = d_li[i]
  for n in range(len(clothe_li)):
    a,b,c = clothe_li[n]
    if a <= d <= b:
      dp[i][n] = 1

  i = 1
  while i < D:
    d = d_li[i]
    for pre_n in range(N):
      if not dp[i-1][pre_n]:
        continue
      for n in range(N):
        a, b, c = clothe_li[n]
        if a <= d <= b:
          dp[i][n] = max(dp[i][n], dp[i-1][pre_n] + abs(clothe_li[pre_n][2] - c))
    i += 1

  print(max(dp[-1]) - 1)


if __name__ == '__main__':
  (lambda f:(f()))(run)