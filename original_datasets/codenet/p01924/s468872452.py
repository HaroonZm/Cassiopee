while True:
    T,D,L=map(int,input().split())
    if T==0 and D==0 and L==0:
        break
    rem,ans=0,0
    for _ in [0]*T:
        x=int(input())
        if x >= L:
            rem=D
        if rem:
            ans+=1
            rem-=1
    if ans:
        ans-=1
    print(ans)