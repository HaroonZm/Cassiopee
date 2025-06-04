N,D=[int(x)for x in input().split()]
res=val=tm=fl=1
cnt=0
i=0
while i<N:
 t1,f1=[int(x)for x in input().split()]
 step=f1-fl
 wait=t1-tm
 if fl-1+f1-1<=wait:
  res+=cnt*(fl-1)
  cnt=1
 elif abs(step)<=wait and cnt<D:
  res+=cnt*abs(wait)
  cnt+=1
 else:
  print(-1)
  break
 tm,f1=t1,f1
 fl=f1
 i+=1
else:
 res+=cnt*(fl-1)
 print(res)