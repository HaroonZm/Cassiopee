n = int(input())
if n == 0:
  ans = 0
elif n % 2 == 1:
  ans = 0
else:
  pwr = 10
  ans = 0
  while pwr <= n:
    ans += n // pwr
    pwr *= 5
print(ans)