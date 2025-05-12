import math
W,H,C=map(int,input().split())

sikaku=math.gcd(W,H)
print(C*(W*H)//(sikaku*sikaku))