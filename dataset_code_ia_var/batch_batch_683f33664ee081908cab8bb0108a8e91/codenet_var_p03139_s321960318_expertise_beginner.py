n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)

minimum = a
if b < a:
    minimum = b

maximum = a + b - n
if maximum < 0:
    maximum = 0

print(minimum, maximum)