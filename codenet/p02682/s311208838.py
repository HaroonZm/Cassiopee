a,b,c,k=map(int,input().split())
ans=0
if k>a+b:
    ans+=a
    k-=(a+b)
    if k<=c:
        print(ans-k)
    else:
        print(ans-c)
    
else:
    if k>=a:
        print(a)
    else:
        print(k)