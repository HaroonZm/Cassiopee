import sys
input=sys.stdin.readline

x1,y1,x2,y2=map(int,input().split())
q=int(input())
dx,dy=x2 - x1, y2 - y1
den=dx*dx+dy*dy

for _ in range(q):
    px,py=map(int,input().split())
    vx,vy=px - x1, py - y1
    t=(vx*dx + vy*dy)/den
    projx,projy = x1 + t*dx, y1 + t*dy
    rx,ry = 2*projx - px, 2*projy - py
    print(f"{rx:.10f} {ry:.10f}")