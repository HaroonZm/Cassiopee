x1, x2 = input().split()
x1 = int(x1)
x2 = int(x2)
distance = x1 - x2
if distance < 0:
    distance = -distance
print(distance)