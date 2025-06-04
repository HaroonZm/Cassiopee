h, r = map(int, input().split())
if h >= 0:
    print(1)
elif h + r == 0:
    print(0)
else:
    print(-1)