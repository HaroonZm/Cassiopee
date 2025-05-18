x,k,d = list(map(int, input().split()))

if x < 0:
  q = (x // d) * -1
  if k < q:
    x = x + d * k
  else:
    ak = (k - q) % 2
    x = x + d * q - d * ak
else:
  q = x // d
  if k < q:
    x = x - d * k
  else:
    ak = (k - q) % 2
    x = x - d * q - d * ak
print(abs(x))