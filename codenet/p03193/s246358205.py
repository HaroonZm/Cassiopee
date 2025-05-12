n,h,w = map(int, input().split())
ab=[list(map(int,input().split())) for i in range(n)]

ans=0
for a,b in ab:
  if a>=h and b>=w:
    ans+=1
print(ans)