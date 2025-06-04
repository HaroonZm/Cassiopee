w,h,v,t,x,y,p,q=map(int,open(0).read().split())
R=v*t
count=0
def dist(a,b,c,d):
    return abs(a-c)+abs(b-d)
def dist2(a,b,c,d):
    dx=abs(a-c)
    dy=abs(b-d)
    return (dx*dx+dy*dy)**0.5
max_i=R//w+2
max_j=R//h+2
for i in range(-max_i,max_i+1):
    for j in range(-max_j,max_j+1):
        cx=p if i%2==0 else w-p
        cy=q if j%2==0 else h-q
        nx=i*w*2+cx
        ny=j*h*2+cy
        d=dist2(x,y,nx,ny)
        if d<=R+1e-9:
            count+=1
print(count)