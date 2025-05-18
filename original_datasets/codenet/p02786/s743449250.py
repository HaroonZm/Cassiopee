import math
N=int(input())
n=math.floor(math.log2(N))

ans=1
for i in range(n):
    ans += (2**(i+1)) 
print(ans)