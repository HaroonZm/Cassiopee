w=int(input())
res=[]
while w>0:
 r=w%3
 w//=3
 if r==0:
  res.append('0')
 elif r==1:
  res.append('+')
 elif r==2:
  res.append('-')
  w+=1
print(''.join(res[::-1]))