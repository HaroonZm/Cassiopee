x,y=map(int,input().split())
if x<0:x,y=-x,-y
s=max(abs(x),abs(y))
p=4*s*(s-1)+1
dx=x+s-1
dy=s-1-y
if dy==0:c=p+dx
elif dx==2*s-1:c=p+3*s-1-dy
elif dy==2*s-1:c=p+5*s-3-dx
else:c=p+7*s-7+dy
print((c-1)%3+1)