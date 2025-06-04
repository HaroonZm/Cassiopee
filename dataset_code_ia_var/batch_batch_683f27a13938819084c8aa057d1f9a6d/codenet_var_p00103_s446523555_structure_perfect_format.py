for unused in xrange(input()):
    out = 0
    stack = 0
    p = 0
    while out < 3:
        ev = raw_input()
        if ev == "OUT":
            out += 1
        if ev == "HIT":
            stack += 1
        if ev == "HOMERUN":
            p += stack + 1
            stack = 0
    if stack >= 4:
        p += stack - 3
    print p