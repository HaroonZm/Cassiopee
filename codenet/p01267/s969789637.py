while True:
    n, a, b, c, x = map(int, input().split())
    if n == 0:
        break

    flame = 0
    first = True

    for y in list(map(int, input().split())):
        if not first:
            x = (a * x + b) % c
            flame += 1
        else:
            first = False

        while x != y and flame <= 10000:
                x = (a * x + b) % c
                flame += 1

    if flame > 10000:
        print(-1)
    else:
        print(flame)