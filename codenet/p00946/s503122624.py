n,m = [int(i) for i in input().split()]
INIT = True
table = [INIT] * n
lis = []
for i in range(m):
  num = int(input())
  lis.append(num)

for i in lis[::-1]:
  if table[i-1]:
    print(i)
  table[i-1] = False

for i in range(n):
  if table[i]:
    print(i+1)