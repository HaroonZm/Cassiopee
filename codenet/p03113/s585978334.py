S=sorted
n,k,*a=map(int,open(i:=0).read().split())
l=S([-a,i:=i+1]for a in a)
_,r=zip(*l)
while k:
 *_,b=r;k-=1
 for t in S(l):
  if t[1]-b:t[t[0]>-2<exit(print(-1))]+=1;r+=t[1],
print(len(r),*r)