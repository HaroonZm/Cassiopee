A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

X=[]
Y=[]
C=[]
for m in range(M):
  x,y,c=map(int,input().split())
  X.append(x)
  Y.append(y)
  C.append(c)
no_coupon=min(a)+min(b)

sum=[]
for i in range(M):
  sum.append(a[X[i]-1]+b[Y[i]-1]-C[i])

with_coupon=min(sum)
print(min(no_coupon,with_coupon))