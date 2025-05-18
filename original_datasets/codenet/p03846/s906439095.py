N = int(input())
mod = 10 ** 9 + 7
A = list(map(int, input().split()))
B = [0 for i in range(N)]
for a in A:
  B[a] += 1
f = 0
if N % 2 == 0:
  ans = 1
  for i in range(1, N, 2):
    if B[i] != 2:
      f = 1
      break
    else:
      ans = ans * 2 % mod
  if f == 1:
    print(0)
  else:
    print(ans)
else:
  ans = 1
  if B[0] != 1:
    f = 1
  if f ==0:
    for i in range(2, N + 1, 2):
      if B[i] != 2:
        f = 1
        break
      else:
        ans = ans * 2 % mod
  if f == 1:
    print(0)
  else:
    print(ans)