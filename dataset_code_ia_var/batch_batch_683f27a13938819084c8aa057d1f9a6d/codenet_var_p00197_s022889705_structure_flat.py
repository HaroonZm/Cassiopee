while True:
    inputs = input()
    xys = inputs.split()
    x = int(xys[0])
    y = int(xys[1])
    if x == 0 and y == 0:
        break
    ans = 0
    while True:
        if y == 0:
            break
        if x < y:
            tmp = x
            x = y
            y = tmp
        x = x % y
        tmp = x
        x = y
        y = tmp
        ans = ans + 1
    print(x, ans)