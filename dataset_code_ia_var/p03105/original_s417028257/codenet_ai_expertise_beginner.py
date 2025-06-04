a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
result = b // a
if result < c:
    print(result)
else:
    print(c)