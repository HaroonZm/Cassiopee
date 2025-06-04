q=int(input())
for _ in range(q):
    x0,y0,x1,y1,x2,y2,x3,y3=map(int,input().split())
    dx1,dy1=x1-x0,y1-y0
    dx2,dy2=x3-x2,y3-y2
    denom=dx1*dy2 - dy1*dx2
    t=((x2 - x0)*dy2 - (y2 - y0)*dx2)/denom
    x=x0 + t*dx1
    y=y0 + t*dy1
    print(f"{x:.10f} {y:.10f}")