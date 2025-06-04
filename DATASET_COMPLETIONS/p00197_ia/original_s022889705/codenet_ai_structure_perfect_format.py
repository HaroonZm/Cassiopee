while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    ans = 0
    while True:
        if y == 0:
            break
        if x < y:
            x, y = y, x
        x = x % y
        x, y = y, x
        ans += 1
    print(x, ans)