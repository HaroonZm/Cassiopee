N,M = map(int,input().split())
XY = []
for _ in range(M):
    x,y = map(int,input().split())
    xy = (x,y)
    XY.append(xy)
XY.sort(key = lambda x:x[0]) # x sort

*minY, = range(N)
*maxY, = range(N)

for _,y in XY:
    y0,y1 = y-1, y
    minY[y1] = minY[y0]
    maxY[y0] = maxY[y1]

ans = [maxY[i] - minY[i]+1 for i in range(N)]
print(*ans)