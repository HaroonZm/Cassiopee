n = int(input())
a = list(map(int,input().split()))
xor = 0
if n == 2:
  a,b = a
  if a >= b and (a+b)%2 == 0:
    print((a+b)//2-b)
  else:
    print(-1)
  exit()
for i in range(2,n):
  xor ^= a[i]
a,b = a[0],a[1]
sm = a+b
ls = []
smt = 0
for i in range(50)[::-1]:
  if xor&1<<i:
    ls.append(1)
    smt += 1<<i
  else:
    if smt+(2<<i) > sm:
      ls.append(0)
    else:
      ls.append(2)
      smt += 2<<i
if smt != sm:
  print(-1)
  exit()
mn = 0
mx = 0
for i in range(50):
  if ls[49-i] == 1:
    mx += 1<<i
  elif ls[49-i] == 2:
    mn += 1<<i
    mx += 1<<i
if not mn <= a:
  print(-1)
  exit()
ans = mn
for i in range(50):
  if ls[i] == 1:
    if ans+(1<<(49-i)) > a:
      continue
    else:
      ans += 1<<(49-i)
if ans == 0:
  print(-1)
else:
  print(a-ans)