a = []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))
x = a[0] * a[4]
if a[4] - a[2] > 0:
    y = a[1] + (a[4] - a[2]) * a[3]
else:
    y = a[1]
if x < y:
    print(x)
else:
    print(y)