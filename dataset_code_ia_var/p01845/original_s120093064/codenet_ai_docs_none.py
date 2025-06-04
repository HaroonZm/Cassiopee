while True:
    r_0, w_0, c, r = map(int, input().split())
    if r_0 == w_0 == c == r:
        break
    if c <= r_0 / w_0:
        print(0)
    else:
        num = 0
        while True:
            num += 1
            r_0 += r
            if c <= r_0 / w_0:
                print(num)
                break