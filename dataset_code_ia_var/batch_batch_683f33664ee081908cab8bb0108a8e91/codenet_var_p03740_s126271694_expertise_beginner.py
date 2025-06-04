x_y = input().split()
x = int(x_y[0])
y = int(x_y[1])

if x > y:
    diff = x - y
else:
    diff = y - x

if diff <= 1:
    print("Brown")
else:
    print("Alice")