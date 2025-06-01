N=int(input())
for i in range(N):
    s,d=map(int,input().split())
    s+=2**30
    d+=2**30
    ans=0
    while s+(s&-s)<=d:
        s+=s&-s
        ans+=1
    d-=s
    while d:
        d-=d&-d
        ans+=1
    print(ans)