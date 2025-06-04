n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)

total = a * n

if total >= b:
    print(b)
else:
    print(total)