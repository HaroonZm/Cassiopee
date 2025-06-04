a = list(map(int, input().split()))
if a[0] == a[1] == a[2]:
    print(1)
else:
    if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
        print(3)
    else:
        print(2)