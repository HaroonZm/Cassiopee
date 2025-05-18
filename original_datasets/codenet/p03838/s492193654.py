#agc008-a
x,y=map(int,input().split())
ans=float('inf')

#反転させるかどうか決めた後のx,yの上下関係を考える
#0,0
if y-x>0:
    ans=min(ans,y-x)
#1,0
if -x<=y:
    ans=min(ans,1+y+x)
#0,1
if x<=-y:
    ans=min(ans,1+-y-x)
#1,1
if -x<=-y:
    ans=min(ans,2+-y+x)
print(ans)