import math
a,b=map(int,input().split())
g=math.gcd(a,b)
a1,b1=a/g,b/g
print(int((a1-1+b1)*g+1))