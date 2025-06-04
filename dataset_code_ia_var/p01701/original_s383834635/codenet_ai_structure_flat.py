while 1:
    s = raw_input()
    s = s.replace("north","0")
    s = s.replace("west","1")
    s = s[::-1]
    if s == "#":
        break
    u = 90 * int(s[0])
    d = len(s) - 1
    for i in s[1:]:
        if i == "1":
            u = 2 * u + 90
        else:
            u = 2 * u - 90
    while (u + 1) % (2 * d):
        u = u / 2
        d = d - 1
    if d == 0:
        print u
    else:
        print "%d/%d" % (u, 2 ** d)