import math

w,h,c=map(int,input().split())
g=math.gcd(w,h)
print(int((w/g)*(h/g)*c))