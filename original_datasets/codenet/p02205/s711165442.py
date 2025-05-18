n=int(input())
a,b=map(int,input().split())
ab=[[a,b]]
for i in range(11):
  a,b=ab[-1]
  if i%2==0:ab.append([a-b,b])
  else:ab.append([a,a+b])
print(*ab[n%12])