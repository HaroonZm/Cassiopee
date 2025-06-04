a = list(map(int, input().split()))
if a[0] * a[1] * a[2] % 2 == 0:
    print(0)
else:
    if a[0] <= a[1] and a[0] <= a[2]:
        x = a[0]
        if a[1] <= a[2]:
            y = a[1]
        else:
            y = a[2]
    elif a[1] <= a[0] and a[1] <= a[2]:
        x = a[1]
        if a[0] <= a[2]:
            y = a[0]
        else:
            y = a[2]
    else:
        x = a[2]
        if a[0] <= a[1]:
            y = a[0]
        else:
            y = a[1]
    print(x * y)