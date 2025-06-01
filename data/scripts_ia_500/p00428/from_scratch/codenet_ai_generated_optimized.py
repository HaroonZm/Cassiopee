while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    counts=[0]*m
    for _ in range(n):
        votes=list(map(int,input().split()))
        for i,v in enumerate(votes):
            counts[i]+=v
    places=sorted(range(1,m+1),key=lambda x:(-counts[x-1],x))
    print(*places)