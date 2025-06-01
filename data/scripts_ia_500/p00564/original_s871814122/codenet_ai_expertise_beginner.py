n, a, b, c, d = input().split()
n = int(n)
a = int(a)
b = int(b)
c = int(c)
d = int(d)

cost1 = (n // a) * b
if n % a != 0:
    cost1 = (n // a + 1) * b

cost2 = (n // c) * d
if n % c != 0:
    cost2 = (n // c + 1) * d

if cost1 < cost2:
    print(cost1)
else:
    print(cost2)