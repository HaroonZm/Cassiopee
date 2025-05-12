m = int(input())
for _ in range(m):
  fund = int(input())
  year = int(input())
  n = int(input())
  ans = fund
  for i in range(n):
    t, rate, fee = map(float, input().split())
    if t:
      a = fund
      b = 0
      for j in range(year):
        b = int(a*rate)
        a = a+b-fee
      ans = max(ans, a)
    else:
      a = fund
      b = 0
      for j in range(year):
        b+= int(a*rate)
        a = a-fee
      ans = max(ans, a+b)
  print(int(ans))