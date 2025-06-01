W,H,N = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(N):
    if i == 0:
        sx,sy = XY[0]
    else:
        gx,gy = XY[i]
        dx = gx-sx
        dy = gy-sy
        if dx*dy >= 0:
            ans+=max(abs(dx),abs(dy))
        else:
            ans+=(abs(dx)+abs(dy))
        sx,sy = gx,gy
print(ans)