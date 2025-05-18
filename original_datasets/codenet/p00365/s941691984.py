a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
if b == e and c == f:
  print(abs(a-d))
  exit()
if a > d:
  num = 100 * b + c
  nu = 100 * e + f
elif a < d:
  num = 100 * e + f
  nu = 100 * b + c
else:
  print(1)
  exit()
if num > nu:
  print(abs(a-d)+1)
else:
  print(abs(a-d))