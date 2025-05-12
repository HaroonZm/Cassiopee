import math

n = int(input())
p = list()
m = int(math.sqrt(n)+1)
for i in range(2,m):
    if n%i == 0:
        c = 0
        while n%i == 0:
            c += 1
            n //= i
        p.append(c)
if n != 1:
    p.append(1)
maxi = 1
for x in p:
    maxi *= (x+1)
print(len(p),maxi-1)