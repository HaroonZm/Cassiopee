x,y=map(int,input().split())
from math import gcd
g=gcd(x,y)
print(x+y-g+1)