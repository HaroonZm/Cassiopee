n=int(input())
h=list(map(int,input().split()))+[0]
ans=0
while sum(h):
  for i in range(n):
    if h[i]>0 and h[i+1]==0:ans+=1
    h[i]=max(0,h[i]-1)
print(ans)