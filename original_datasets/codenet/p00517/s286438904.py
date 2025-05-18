w,h,n=map(int,input().split())
x,y=map(int,input().split())
a=0
for _ in range(n-1):
    px,py=map(int,input().split())
    dx,dy=px-x,py-y
    if dx*dy<0:a+=sum(map(abs,[dx,dy]))
    else:a+=max(map(abs,[dx,dy]))
    x,y=px,py
print(a)