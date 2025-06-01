n = int(input())
for i in range(n):
    x = int(input())
    print("Case " + str(i+1) + ":")
    for _ in range(10):
        x = x**2
        x = str(x)
        if len(x) < 8:
            x = "0"*(8 - len(x)) + x
        x = x[2:6]
        x = int(x)
        print(x)