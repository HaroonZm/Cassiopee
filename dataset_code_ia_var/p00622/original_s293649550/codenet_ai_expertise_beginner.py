while True:
    up = raw_input()
    if up == '-':
        break
    left = raw_input()
    down = raw_input()

    cen = left[0]
    idu = 0
    idd = 0
    idl = 0
    ans = ''
    i = 0
    n = len(up) + len(left) - 1
    while i < n:
        if down[idd] == cen:
            cen = up[idu]
            idu = idu + 1
            idd = idd + 1
            if idd >= len(down):
                idd = len(down) - 1
        else:
            ans = ans + cen
            idl = idl + 1
            cen = left[idl]
        i = i + 1
    ans = ans + cen
    print ans