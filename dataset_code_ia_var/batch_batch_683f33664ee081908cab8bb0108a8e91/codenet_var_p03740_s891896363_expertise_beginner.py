a = input()
b = a.split()
x = int(b[0])
y = int(b[1])

if abs(x - y) > 1:
    print("Alice")
else:
    print("Brown")