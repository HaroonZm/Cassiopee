def doStuff():
    x = y = z = 0
    n = int(input())
    idx = 0
    while idx < n:
        parts = input().split()
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
        X = a + max(y, z)
        Y = b + max(x, z)
        temp = c + max(x, y)
        x, y, z = X, Y, temp
        idx += 1
    array = [x, y, z]
    print(max(array))
doStuff()