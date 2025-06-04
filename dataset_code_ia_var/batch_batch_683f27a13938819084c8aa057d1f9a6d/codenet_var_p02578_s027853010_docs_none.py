n=int(input())
a=map(int,input().split())

ans=0
cur_max=0

for x in a:
    if cur_max>x:
        ans+=cur_max-x
    cur_max=max(cur_max,x)

print(ans)