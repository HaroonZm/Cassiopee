from math import gcd

n,m = map(int,input().split())
s = input()
t = input()

l = n * m // gcd(n,m)

cnt = (l // m) * (l // n)
a = [i * l // m for i in range(l // cnt)]
b = [i * l // n for i in range(l // cnt)]

for i in range(l // cnt):
    a1 = a[i]
    b1 = b[i]
    if s[a1] == t[b1]:
        pass
    else:
        print(-1)
        exit()

print(l)