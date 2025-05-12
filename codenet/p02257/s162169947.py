def IsPrime(x):
    if x == 1:
        return False
    p = int(pow(x, 0.5)) + 1
    i = 2
    while i <= p and i < x:
        if x % i == 0:
            return False
        else:
            i += 1
    return True

n = int(input())
c = 0
i = 0
while i < n:
    x = int(input())
    if IsPrime(x) == True:
        c += 1
    i += 1
print(c)