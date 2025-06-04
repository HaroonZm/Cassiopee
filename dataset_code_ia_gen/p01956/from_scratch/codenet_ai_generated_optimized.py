N,H,W=map(int,input().split())
x=list(map(int,input().split()))
l,r=0,W*N
for i in range(N):
 if i%2==0:r=min(r,W*(i)+x[i])
 else:l=max(l,W*(i+1)-x[i])
print(max(0,r-l)*H)