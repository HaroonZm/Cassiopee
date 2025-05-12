import math
n=int(input())

def is_prime(x):
    if x == 1: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

c=0
for i in range(n):
    m=int(input())
    if is_prime(m) is True:
        c+=1
    
print(c)