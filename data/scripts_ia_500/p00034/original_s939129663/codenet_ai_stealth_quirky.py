i=0
while 1:
 try:
  l=[int(x)for x in input().split(',')]
 except Exception:break
 d=sum(l[:10]);v1,v2=l[10],l[11]
 t=m=0
 for i,x in enumerate(l[:10]):
  t=x/v1
  m+=t*v2
  if m+sum(l[:i+1])>=d:
   print(i+1);break
 i+=1