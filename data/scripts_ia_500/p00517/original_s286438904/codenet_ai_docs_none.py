w,h,n=map(int,input().split())
x,y=map(int,input().split())
a=0
for _ in range(n-1):
    px,py=map(int,input().split())
    dx,dy=px-x,py-y
    if dx*dy<0:
        a+=abs(dx)+abs(dy)
    else:
        a+=max(abs(dx),abs(dy))
    x,y=px,py
print(a)