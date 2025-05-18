n,m=map(int,input().split())
if abs(n-m)>=2:
    print(0)
    exit()
elif n==m:
    ans=2
    for i in range(1,n+1):
        ans*=i**2
        ans%=(10**9 +7)
    
    #ans=2*(math.factorial(n)**2)
    print(ans)
elif abs(n-m)==1:
    ans=1
    t=max(n,m)
    for i in range(2,t+1):
        ans*=i*(i-1)
        ans%=(10**9 +7)
    print(ans)