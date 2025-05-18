N = int(input())
h = list(map(int,input().split()))
ans = 0
while True:
  if max(h) == 0:
    break
  i = 0
  while i < N:
    if h[i] == 0:
      i+=1
      continue
    else:
      ans += 1
      while (i < N and h[i] > 0):
        h[i] -= 1
        i += 1
print(ans)