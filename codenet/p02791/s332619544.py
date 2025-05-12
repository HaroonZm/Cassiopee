n = int(input())
p = list(map(int,input().split()))
x = p[0]
ans = 1
for i in range(n):
  if p[i]<x:
    x = p[i]
    ans+=1
print(ans)