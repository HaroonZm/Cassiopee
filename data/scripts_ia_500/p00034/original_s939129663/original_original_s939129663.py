while True:
    try:
        l = list(map(int, input().split(',')))
    except:
        break
    d, v1, v2 = sum(l[:10]), l[10], l[11]
    t = 0
    m = 0
    for i, x in enumerate(l[:10]):
        t = x / v1
        m += t * v2
        if m + sum(l[:i+1]) >= d:
            print(i+1)
            break