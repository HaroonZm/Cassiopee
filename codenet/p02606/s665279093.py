l,r,d = map(int,input().split())
cnt=0
for num in range(l,r+1):
  if num%d==0:
    cnt+=1
print(cnt)