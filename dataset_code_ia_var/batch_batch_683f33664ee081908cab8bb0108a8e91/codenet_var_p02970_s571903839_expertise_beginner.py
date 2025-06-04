a, b = input().split()
a = int(a)
b = int(b)

d = 2 * b + 1
if a % d == 0:
    result = a // d
else:
    result = a // d + 1

print(result)