n, a, b, c, d = input().split()
n = int(n)
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if n % a == 0:
    na = (n // a) * b
else:
    na = (n // a + 1) * b

if n % c == 0:
    nc = (n // c) * d
else:
    nc = (n // c + 1) * d

if na < nc:
    print(na)
else:
    print(nc)