n,j = map(int,input().split())
l = []
for i in range(n):
  l.append(str(input()))
l.sort()
print(''.join(l))