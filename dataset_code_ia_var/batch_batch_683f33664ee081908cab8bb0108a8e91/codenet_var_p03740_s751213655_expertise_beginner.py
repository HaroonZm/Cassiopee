nombres = input().split()
x = int(nombres[0])
y = int(nombres[1])

if abs(x - y) > 1:
    print("Alice")
else:
    print("Brown")