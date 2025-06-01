a = [tuple(map(int,input().split())) for _ in [0,0]]
a.sort()
if a[1][1] > a[0][1]:
    print(a[1][0] - a[0][0] + 1)
elif a[1][1] == a[0][1] and a[1][2] > a[0][2]:
    print(a[1][0] - a[0][0] + 1)
else:
    print(a[1][0] - a[0][0])