while True:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break
    p = [1] * n
    pn = n
    count = 0
    flag = 1
    while flag == 1:
        for i in range(n):
            if p[i] == 1:
                count += 1
                if count == m:
                    p[i] = 0
                    count = 0
                    pn -= 1
                    if pn == 1:
                        flag = 0
                        break
    for i in range(n):
        if p[i] == 1:
            print i + 1
            break