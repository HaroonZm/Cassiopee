H,W = map(int, input().split())
grid = [input() for _ in range(H)]
bs = [(i,j) for i in range(H) for j in range(W) if grid[i][j]=='B']
ans = 0
for i in range(len(bs)):
    for j in range(i+1,len(bs)):
        ans = max(ans, abs(bs[i][0]-bs[j][0]) + abs(bs[i][1]-bs[j][1]))
print(ans)