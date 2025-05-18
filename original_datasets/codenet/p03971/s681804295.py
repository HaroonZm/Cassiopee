n,a,b=map(int,input().split())
s=input()
c=a+b
t=0
f=0
for i in range(n):
  if s[i]=='a':
    if t<c:
      print('Yes')
      t+=1
    else:
      print('No')
  elif s[i]=='b':
    if t<c and f<b:
      t+=1
      f+=1
      print('Yes')
    else:
      print('No')
  else:
    print('No')