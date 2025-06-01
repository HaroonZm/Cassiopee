h = int(input().split()[0])
r = int(input().split()[1])

if h < 0:
    if h + r < 0:
        print(-1)
    elif h + r == 0:
        print(0)
    else:
        print(1)
else:
    print(1)