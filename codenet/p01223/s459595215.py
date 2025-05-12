n=int(input())
while n:
    input()
    n-=1
    a=list(map(int,input().split()))
    u,d=0,0
    for i in range(1,len(a)):
        if a[i]-a[i-1]>0:u=max(a[i]-a[i-1],u)
        elif a[i]-a[i-1]<0:d=max(a[i-1]-a[i],d)
    print(u,d)