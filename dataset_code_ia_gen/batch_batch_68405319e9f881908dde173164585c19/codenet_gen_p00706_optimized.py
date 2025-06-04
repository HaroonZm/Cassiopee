while True:
    N=int(input())
    if N==0:
        break
    W,H=map(int,input().split())
    grid=[[0]*(W+1) for _ in range(H+1)]
    for _ in range(N):
        x,y=map(int,input().split())
        grid[y][x]=1
    S,T=map(int,input().split())
    prefix=[[0]*(W+1) for _ in range(H+1)]
    for y in range(1,H+1):
        row_sum=0
        for x in range(1,W+1):
            row_sum+=grid[y][x]
            prefix[y][x]=prefix[y-1][x]+row_sum
    max_trees=0
    for y in range(T,H+1):
        for x in range(S,W+1):
            count=prefix[y][x]-prefix[y-T][x]-prefix[y][x-S]+prefix[y-T][x-S]
            if count>max_trees:
                max_trees=count
    print(max_trees)