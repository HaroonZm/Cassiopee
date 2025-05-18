inf=100000000

def calc(uth,dis,c):
    fare=0
    if dis>=inf:
        return inf
    if unchin[c]==1:
        return uth[c][1][0]*dis
    ddis=uth[c][0]
    dcost=uth[c][1]
    i=1
    while(i<unchin[c] and dis>ddis[i]):
        fare+=(ddis[i]-ddis[i-1])*dcost[i-1]
        i+=1
    fare+=(dis-ddis[i-1])*dcost[i-1]
    return fare

def floyd(bigmap,n):
    res=bigmap
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if res[i][j]>res[i][k]+res[k][j]:
                    res[i][j]=res[i][k]+res[k][j]
    return res

def init2d(bigmap,n):
    for i in range(n+1):
        bigmap.append([])
    for map1 in bigmap:
        for j in range(n+1):
            map1.append(inf)
    for i in range(1,n+1):
        bigmap[i][i]=0
    return bigmap

while(1):
    n,m,c,s,g=map(int,raw_input().split())
    if(n==m==0): break
    rosen=[]
    for i in range(c+1):
        map0=[]
        rosen.append(init2d(map0,n))

    for i in range(m):
        x,y,d,c0=map(int,raw_input().split())
        rosen[c0][x][y]=min(rosen[c0][x][y],d)
        rosen[c0][y][x]=min(rosen[c0][x][y],d)

    unchin=list(map(int,raw_input().split()))
    unchin.insert(0,0)
    uth=[]
    uth.append([])
    for i in range(1,c+1):
        ddis=list(map(int,raw_input().split()))
        ddis.insert(0,0)
        dcost=list(map(int,raw_input().split()))
        uth.append([ddis,dcost])

    bigmap=[]
    bigmap=init2d(bigmap,n)

    for c0,cmap in enumerate(rosen[1:]):
        tmp=floyd(cmap,n)
        for i in range(1,n+1):
            for j in range(1,n+1):
                bigmap[i][j]=min(bigmap[i][j],calc(uth,tmp[i][j],c0+1))

    bigmap=floyd(bigmap,n)

    ans=bigmap[s][g]
    if ans < inf:
        print(ans)
    else:
        print(-1)