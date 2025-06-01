import bisect as b;from sys import stdin as I
INF=10**9+1
n,q=map(int,I.readline().split())
tmp=[(int(I.readline()),i)for i in range(n)]
tmp.sort()
s=[0]*n;f=[0]*n;i=0
for k,v in tmp:s[i]=k;f[v]=i;i+=1
L=[]
while q:
 q-=1
 l=I.readline().split()
 c,a=l[0],int(l[1])
 if c=="ADD":i=b.bisect_left(L,f[a-1]);L=L[:i]+[f[a-1]]+L[i:]
 elif c=="REMOVE":L.remove(f[a-1])
 else:
  l,r=-1,INF
  while r-l>1:
   m=(l+r)>>1;c=0;p=-1
   for x in L:
    li=b.bisect_left(s,s[x]-m)
    ri=b.bisect_right(s,s[x])-1
    if li<=p:li=p+1
    c+=ri-li+1;p=ri
   if n-c<=a:r=m
   else:l=m
  print("NA"if r==INF else r)