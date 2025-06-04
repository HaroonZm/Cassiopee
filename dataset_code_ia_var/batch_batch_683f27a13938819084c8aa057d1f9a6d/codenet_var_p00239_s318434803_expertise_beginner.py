while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    for i in range(n):
        values = input().split()
        s = int(values[0])
        p = int(values[1])
        q = int(values[2])
        r = int(values[3])
        lst.append([s, p, q, r])
    l_line = input().split()
    lp = int(l_line[0])
    lq = int(l_line[1])
    lr = int(l_line[2])
    lc = int(l_line[3])
    found = False
    for item in lst:
        s = item[0]
        p = item[1]
        q = item[2]
        r = item[3]
        if p <= lp and q <= lq and r <= lr:
            cost = 4 * p + 9 * q + 4 * r
            if cost <= lc:
                print(s)
                found = True
    if not found:
        print("NA")