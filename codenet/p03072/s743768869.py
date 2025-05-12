n=int(input())
H=list(map(int,input().split()))
ans=1
bar=H[0]
for i in range(1,n):
  if H[i]>=bar:
    ans+=1
    bar=max(bar,H[i])
print(ans)