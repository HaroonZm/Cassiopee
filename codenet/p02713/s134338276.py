k=int(input())
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)
ans=0
i=0

for a in range(1,k+1):
    for b in range(a+1,k+1):
        for c in range(b+1,k+1):
            ans+=gcd(a, b, c) * 6
            i+=6
for a in range(1,k+1):
    for b in range(a+1,k+1):#2,3
        ans+=gcd(a, b) * 6
        i+=6
for a in range(1,k+1):
    ans+=a
    i+=1
print(ans)