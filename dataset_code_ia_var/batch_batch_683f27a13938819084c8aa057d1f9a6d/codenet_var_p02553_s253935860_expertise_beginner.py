a, b, c, d = map(int, input().split())
t = -1000000000
if 0 >= a and 0 <= b:
    t = 0
if 0 >= c and 0 <= d:
    t = 0
x1 = a * c
x2 = b * d
x3 = a * d
x4 = b * c
print(max(x1, x2, x3, x4, t))