a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if ((a * b) % 2 == 1) and ((c + d) % 2 == 1):
    print("No")
else:
    print("Yes")