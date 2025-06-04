a = input().split()
x = int(a[0])
y = int(a[1])
if x > y:
    diff = x - y
else:
    diff = y - x
if diff > 1:
    print("Alice")
else:
    print("Brown")