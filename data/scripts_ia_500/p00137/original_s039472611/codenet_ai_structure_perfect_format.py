for i in range(int(input())):
    x = int(input())
    print("Case " + str(i + 1) + ":")
    for _ in range(10):
        x = str(x ** 2)
        if len(x) < 8:
            x = "0" * (8 - len(x)) + x
        x = x[2:6]
        print(int(x))