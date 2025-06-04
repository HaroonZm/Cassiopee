h, r = [int(num) for num in input().split()]
if h == -r:
    print(0)
elif h > -r:
    print(1)
else:
    print(-1)