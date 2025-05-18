N = int(input())

F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]
ans = -10**9

for i in range(1,2**10):
  tmp = 0
  c = [0] * N
  for j in range(10):
    if (i >> j)& 1:
      for k in range(N):
        if F[k][j] == 1:
          c[k] += 1
  for l in range(N):
    tmp += P[l][c[l]] 
  ans = max(tmp, ans)
print(ans)