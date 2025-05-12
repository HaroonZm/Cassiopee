def check(y,x):
    if 0<=y<=h-1 and 0<=x<=w-1:
        return True
    return False

h,w=map(int,raw_input().split())
g=[map(int,raw_input().split()) for _ in xrange(h)]
pos=[-1]*(h*w)
for i in xrange(h):
    for j in xrange(w):
        pos[g[i][j]-1]=[i,j]

dy=(1,0,-1,0)
dx=(0,1,0,-1)
stop=[set() for _ in xrange(h*w)]
ans=0
for i in xrange(h*w):
    y,x=pos[i]
    for j in xrange(4):
        ny=y+dy[j];nx=x+dx[j]
        if check(ny,nx):
            if g[ny][nx]<g[y][x]:
                for k in list(stop[g[ny][nx]-1]):
                    stop[i].add(k)
    cnt=len(stop[i])
    if cnt>=2:
        ans+=1
    elif cnt==0:
        stop[i].add(g[y][x])

print(ans)