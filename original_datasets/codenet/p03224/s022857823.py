n = int(input())
for i in range(1,100000):
  if n == i*(i+1)//2:
    k = i+1
    break
else:
  print("No")
  exit()
print("Yes")
print(k)
a = [[] for i in range(k)]
moto = list(range(1,n+1))
moto = moto[::-1]
for i in range(k):
  for j in range(i):
    a[i].append(a[j][i-1])
  while len(a[i]) != k-1:
    a[i].append(moto.pop())
for i in a:
  print(k-1,*i)