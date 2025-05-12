x,y,z=map(int,input().split())
w=y+2*z
ans=1
while w<=x-(y+z):
    w+=y+z
    ans+=1
print(ans)