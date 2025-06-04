N,K=map(int,input().split())
X1,Y1,D1,X2,Y2,D2=[],[],[],[],[],[]
for _ in range(N):
    a,b,c,d,e,f=map(int,input().split())
    X1.append(a); Y1.append(b); D1.append(c)
    X2.append(d); Y2.append(e); D2.append(f)
xs=set(X1+X2)
ys=set(Y1+Y2)
ds=set(D1+D2)
xs=sorted(xs)
ys=sorted(ys)
ds=sorted(ds)
x_idx={x:i for i,x in enumerate(xs)}
y_idx={y:i for i,y in enumerate(ys)}
d_idx={d:i for i,d in enumerate(ds)}
dx=len(xs)
dy=len(ys)
dd=len(ds)
grid=[[[0]*(dd) for _ in range(dy)] for __ in range(dx)]
for i in range(N):
    for xi in range(x_idx[X1[i]],x_idx[X2[i]]):
        for yi in range(y_idx[Y1[i]],y_idx[Y2[i]]):
            for di in range(d_idx[D1[i]],d_idx[D2[i]]):
                grid[xi][yi][di]+=1
ans=0
for xi in range(dx-1):
    for yi in range(dy-1):
        for di in range(dd-1):
            if grid[xi][yi][di]>=K:
                ans+=(xs[xi+1]-xs[xi])*(ys[yi+1]-ys[yi])*(ds[di+1]-ds[di])
print(ans)