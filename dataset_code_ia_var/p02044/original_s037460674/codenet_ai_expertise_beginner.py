while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break
    t = m // n
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    cnt = 0
    for i in range(len(a)):
        if a[i] >= t:
            cnt = cnt + t
        else:
            cnt = cnt + a[i]
    print(cnt)