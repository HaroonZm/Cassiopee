while True:
    line = input()
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    x = a
    y = b
    steps = 0
    while y != 0:
        r = x % y
        x = y
        y = r
        steps += 1
    print(x, steps)