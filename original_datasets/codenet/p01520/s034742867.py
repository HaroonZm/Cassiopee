n,t,e=map(int,input().split())
a=list(map(int,input().split()))
tmp=0
for i in range(n):
    x=(t-e-1)//a[i]
    if (x+1)*a[i]<=t+e:
        print(i+1)
        break
else :
    print(-1)