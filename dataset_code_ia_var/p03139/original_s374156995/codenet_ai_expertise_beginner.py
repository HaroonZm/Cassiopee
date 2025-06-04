n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)

if a < b:
    mx = a
else:
    mx = b

if a + b > n:
    mn = (a + b) - n
else:
    mn = 0

print(mx, mn)