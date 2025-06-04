a = input().split()
b = []
for i in a:
    b.append(int(i))
total = 0
for nombre in b:
    total = total + nombre
print(15 - total)