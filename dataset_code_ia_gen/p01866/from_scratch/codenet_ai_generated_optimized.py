N=int(input())
X=input()
D=int(input())
res=[]
diff=D
for i in range(N):
 if X[i]=='0':
  if diff>0:
   res.append('1')
   diff-=1
  else:
   res.append('0')
 else:
  if diff>0:
   res.append('0')
   diff-=1
  else:
   res.append('1')
print(''.join(res))