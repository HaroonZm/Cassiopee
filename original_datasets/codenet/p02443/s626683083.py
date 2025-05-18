n=int(input())
s=list(map(int,input().split()))
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    s[a:b]=reversed(s[a:b])
print(*s)