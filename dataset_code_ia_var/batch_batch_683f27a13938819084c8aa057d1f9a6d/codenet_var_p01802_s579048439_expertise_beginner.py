d_e = input().split()
while d_e:
    d = int(d_e[0])
    e = int(d_e[1])
    if d == 0:
        break
    ans = 100000
    for x in range(d + 1):
        y = d - x
        dist = (x * x + y * y) ** 0.5
        diff = abs(dist - e)
        if diff < ans:
            ans = diff
    print(ans)
    try:
        d_e = input().split()
    except:
        break