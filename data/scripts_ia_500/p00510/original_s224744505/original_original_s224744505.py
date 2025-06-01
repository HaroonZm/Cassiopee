n=int(input())
m=int(input())
ans=c=m
for i in range(n):
    a,b=[int(a) for a in input().split()]
    if c<0:
        continue
    c+=a-b
    if ans<c:
        ans=c
    if c<0:
        ans=0
print(ans)