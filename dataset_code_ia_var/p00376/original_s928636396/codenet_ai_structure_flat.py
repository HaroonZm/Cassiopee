x = input().split()
x_1 = int(x[0])
x_2 = int(x[1])
d = x_2 - x_1
if d < 0:
    d = -d
print(d)