n,a,b=[*map(int,input().split())]
s=input();X=a+b;Y=0;Z=0
for j,F in enumerate(s):
 if F>'a':
  if F<='b' and Y<X and Z<b:
   print(('Yes'));Y+=1;Z+=1
  else:print('No')
 else:
  if Y<X:print(('Yes'));Y+=1
  else:print('No')