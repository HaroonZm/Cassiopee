def val(x):
 _sum = 0
 while True:
  if x == 0:
   break
  _sum = _sum + (x % 10)
  x = x // 10
 return _sum

a,n,m = [*map(int, input().split())]
cnt = 0
y = 1
while y < 73:
 x = 1
 t = 1
 while t <= n:
  x *= y + a
  t += 1
 if x <= m:
  if val(x) == y:
   cnt = cnt + 1
 y += 1

print((cnt))