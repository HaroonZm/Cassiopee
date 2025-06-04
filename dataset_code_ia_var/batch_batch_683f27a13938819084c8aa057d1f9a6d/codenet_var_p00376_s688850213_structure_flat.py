x1, x2 = map(int, input().split())
if x1 < x2:
    print(x2 - x1)
elif x1 > x2:
    print(x1 - x2)
else:
    print('0')