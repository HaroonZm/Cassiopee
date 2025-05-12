while True:
    R, N = map(int, input().split())
    if not (R | N):
        break
    geta = 20
    buildings = [0] * (geta * 2)
    for _ in range(N):
        xl, xr, h = map(int, input().split())
        for i in range(xl + geta, xr + geta):
            buildings[i] = max(buildings[i], h)

    ans = 20
    for i in range(-R + geta, R + geta):
        if i < geta:
            buildings[i] -= pow(R * R - (i - geta + 1) * (i - geta + 1), 0.5) - R
        else:
            buildings[i] -= pow(R * R - (i - geta) * (i - geta), 0.5) - R
        ans = min(ans, buildings[i])
    print(ans)