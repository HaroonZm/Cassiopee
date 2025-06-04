while True:
    d_e = input().split()
    d = int(d_e[0])
    e = int(d_e[1])
    if d == 0:
        break

    ans = abs(d - e)
    for x in range(1, d):
        y = d - x
        distance = (x * x + y * y) ** 0.5
        if abs(distance - e) < ans:
            ans = abs(distance - e)
    print("%.4f" % ans)