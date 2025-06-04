n,m=map(int,input().split())
for _ in range(m):
    a=int(input())
    while a:
        n,a=a,n%a
print(['No','Yes'][n==1])