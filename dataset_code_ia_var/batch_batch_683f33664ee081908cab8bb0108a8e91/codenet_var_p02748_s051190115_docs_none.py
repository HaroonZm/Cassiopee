A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
X=[]
Y=[]
C=[]
for _ in range(M):
    x,y,c=map(int,input().split())
    X.append(x)
    Y.append(y)
    C.append(c)
no_coupon=min(a)+min(b)
total=[]
for i in range(M):
    total.append(a[X[i]-1]+b[Y[i]-1]-C[i])
with_coupon=min(total)
print(min(no_coupon,with_coupon))