n = int(input())
sl = [int(input()) for i in range(n)]
c = sl[0] // 2
sl[0] %= 2
for i in range(1,n):
  if sl[i-1] and sl[i]:
    sl[i] -= 1
    c += 1
  c += sl[i] // 2
  sl[i] %= 2
print(c)