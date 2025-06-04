n,m=map(int,input().split())
if n==1:
 print(m//2)
else:
 if n%2==1:
  res=[0]*((n-1)//2)+[m]+[0]*((n-1)//2)
 else:
  res=[0]*(n//2)+[m]*(n//2)
 print(*res)