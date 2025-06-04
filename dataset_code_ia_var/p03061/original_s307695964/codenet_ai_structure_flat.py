import math

n = int(input())
a = [int(t) for t in input().split()]

a_gcd = a[0]
for x in a[1:]:
    a_gcd = math.gcd(a_gcd, x)

for i in range(len(a)):
    a[i] //= a_gcd

a_rev = a[::-1]

lgcd = [0]
rgcd = [0]
for i in range(n):
    l = math.gcd(a[i], lgcd[i])
    r = math.gcd(a_rev[i], rgcd[i])
    lgcd.append(l)
    rgcd.append(r)

rgcd = rgcd[::-1]
g = []
for i in range(n):
    g.append(math.gcd(lgcd[i], rgcd[i+1]))

print(max(g) * a_gcd)