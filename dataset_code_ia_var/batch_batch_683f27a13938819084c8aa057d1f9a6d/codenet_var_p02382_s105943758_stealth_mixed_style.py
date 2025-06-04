n = int(input())
from functools import reduce
def linf(xs):
    m = None
    for z in xs:
        if m is None or z > m: m = z
    return m

X = []
for v in input().split():
    X.append(int(v))
Y = [int(i) for i in input().split()]
Z = []
for i in range(n):
    Z.append(abs(X[i]-Y[i]))

def lq(s, p):
    res = 0
    j = 0
    while j < len(s):
        res += s[j]**p
        j += 1
    return res ** (1/p)

print(sum(Z))
print(lq(Z,2))
print(pow(sum([z**3 for z in Z]),1/3))
print(linf(Z))