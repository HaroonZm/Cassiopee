import math

n,m = map(int,input().split())
    
if abs(n-m) <= 1:
    if n == m:
        print((math.factorial(n)**2)*2% 1000000007)
    else:
        print(math.factorial(n)*math.factorial(m)% 1000000007)
        
else:
    print(0)