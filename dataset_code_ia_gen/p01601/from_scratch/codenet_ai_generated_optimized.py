n=int(input())
def is_pal(x):return str(x)==str(x)[::-1]
if is_pal(n):print(n)
else:
 res=[]
 for i in range(max(0,n-200),n+201):
  if is_pal(i):res.append(i)
 d=min(abs(x-n)for x in res)
 print(min(x for x in res if abs(x-n)==d))