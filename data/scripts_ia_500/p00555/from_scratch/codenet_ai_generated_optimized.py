N,M,D=map(int,input().split())
grid=[input() for _ in range(N)]
res=0
if D==1:
    for row in grid:
        res+=row.count('.')
else:
    for r in range(N):
        cnt=0
        for c in range(M):
            if grid[r][c]=='.':
                cnt+=1
                if cnt>=D:
                    res+=1
            else:
                cnt=0
    for c in range(M):
        cnt=0
        for r in range(N):
            if grid[r][c]=='.':
                cnt+=1
                if cnt>=D:
                    res+=1
            else:
                cnt=0
print(res)