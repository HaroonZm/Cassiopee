a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if b >= c:
    print(b + c)
else:
    if a + b >= c:
        print(b + c)
    else:
        print(a + 2 * b + 1)