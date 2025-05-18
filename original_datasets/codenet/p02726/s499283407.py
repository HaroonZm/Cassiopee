n,x,y = map(int,input().split())
a = [0]*n
for i in range(n):
  for j in range(i+1,n):
    a[min(j-i,abs(i-x+1)+abs(j-y+1)+1)] += 1
for b in a[1:]:
  print(b)