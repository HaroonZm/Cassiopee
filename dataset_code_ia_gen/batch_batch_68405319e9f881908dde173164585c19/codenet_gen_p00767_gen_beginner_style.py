while True:
    line = input()
    if line == "0 0":
        break
    h, w = map(int, line.split())
    d_sq = h*h + w*w
    found = False
    for d2 in range(d_sq+1, 150*150*2+1):
        for nh in range(1, 151):
            for nw in range(nh+1, 151):
                if nh*nh + nw*nw == d2:
                    if nh < h or (nh == h and nw <= w):
                        continue
                    print(nh, nw)
                    found = True
                    break
            if found:
                break
        if found:
            break