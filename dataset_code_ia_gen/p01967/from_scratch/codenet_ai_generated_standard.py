n=int(input())
c=list(map(int,input().split()))
q=int(input())
a=[0]*n
for i in range(q):
    t,x,d=map(int,input().split())
    x-=1
    if t==1:
        if a[x]+d>c[x]:
            print(x+1)
            exit()
        a[x]+=d
    else:
        if a[x]<d:
            print(x+1)
            exit()
        a[x]-=d
print(0)