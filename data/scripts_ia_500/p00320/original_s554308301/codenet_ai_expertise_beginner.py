a = []
for i in range(6):
    line = input()
    numbers = line.split()
    numbers_int = []
    for num in numbers:
        numbers_int.append(int(num))
    numbers_int.sort()
    a.append(numbers_int)

a.sort(key=lambda x: x[1])
a.sort(key=lambda x: x[0])

if a[0] == a[1] and a[2] == a[3] and a[4] == a[5] and a[0][0] == a[2][0] and a[0][1] == a[4][0] and a[2][1] == a[4][1]:
    print("yes")
else:
    print("no")