while True:
    R_0, W_0, C, R = map(int, raw_input().split())

    if R_0 == 0 and W_0 == 0 and C == 0 and R == 0:
        break

    t = max(0, C * W_0 - R_0)
    print t / R if t % R == 0 else t / R + 1