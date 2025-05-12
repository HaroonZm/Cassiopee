from collections import defaultdict
N=int(input())
src=list(map(int,input().split()))
ans=0
d=defaultdict(int)
e=[]
for i,s in enumerate(src,1):
  l=i+s
  r=i-s
  d[l]+=1
  ans+=d[r]

print(ans)