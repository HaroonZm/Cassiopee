while True:
    d, e = map(int, input().split())
    if d == 0:
        break

    ans = abs(d - e)
    for x in range(1, d):
        y = d - x
        ans = min(ans, abs((x ** 2 + y ** 2) ** 0.5 - e))
    print("{:.4f}".format(ans))