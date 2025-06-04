a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if b >= a * c:
    print(c)
else:
    print(b // a)