import math

def isprime(n):
    if n == 1: return 0
    
    for k in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % k == 0:
            return 0
    
    return 1

while True:
    a,d,n = map(int,input().split())
    
    if a==d==n==0:
        break
    
    kazu=0
    num=0
    for i in range(10**6):
        kazu = a + i*d
        
        if isprime(kazu) == 1:
            num+=1
        
        if num == n:
            print(kazu)
            break