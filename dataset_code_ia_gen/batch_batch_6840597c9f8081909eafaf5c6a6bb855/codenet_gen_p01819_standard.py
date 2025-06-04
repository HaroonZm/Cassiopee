n,m=map(int,input().split())
data=[input() for _ in range(m)]
Wcount=[0]*(n+1)
Ecount=[0]*(n+1)
for i in range(m):
    for j in range(n):
        if data[i][j]=='W':
            Wcount[j+1]+=1
        else:
            Ecount[j+1]+=1
prefixW=[0]*(n+1)
prefixE=[0]*(n+1)
for i in range(1,n+1):
    prefixW[i]=prefixW[i-1]+Wcount[i]
    prefixE[i]=prefixE[i-1]+Ecount[i]
min_error=float('inf')
boundary=0
totalE=prefixE[n]
for i in range(n+1):
    # Errors = W on east (i+1 to n) + E on west (1 to i)
    errors = (prefixW[n]-prefixW[i]) + prefixE[i]
    if errors<min_error:
        min_error=errors
        boundary=i
if boundary==0:
    print("0 1")
elif boundary==n:
    print(n,n+1)
else:
    print(boundary,boundary+1)