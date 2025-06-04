n=int(input())
s=list(map(int,input().split()))
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    s[a:b]=s[a:b][::-1]
print(*s)