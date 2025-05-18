n,C,*H=map(int,open(0).read().split());
dp=[0];
P=[0];
def f(I,h):
    return dp[I]+H[I]*(H[I]-2*h)
def c(x,y,z):
    return (H[y]-H[x])*(f(y,0)-f(z,0))>(H[z]-H[y])*(f(x,0)-f(y,0))
for i in range(1,n):
    while len(P)>1 and f(P[0],H[i])>f(P[1],H[i]):P.pop(0)
    dp+=[f(P[0],H[i])+H[i]**2+C]
    while len(P)>1 and c(P[-2],P[-1],i):P.pop()
    P+=[i]
print(dp[-1])