for i in range(110):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    else:
        a = [0] * x
        for j in range(y):
            ls = list(map(int, input().split()))
            for k in range(x):
                a[k] += ls[k]
        print(max(a))