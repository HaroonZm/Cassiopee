W,H=map(int,input().split())
N=int(input())
X=[]
Y=[]
for _ in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
if N%2==1:
    medX=X[N//2]
    medY=Y[N//2]
else:
    medX=X[N//2-1]
    medY=Y[N//2-1]
total=0
for i in range(N):
    total+=2*(abs(X[i]-medX)+abs(Y[i]-medY))
print(total)
print(medX,medY)