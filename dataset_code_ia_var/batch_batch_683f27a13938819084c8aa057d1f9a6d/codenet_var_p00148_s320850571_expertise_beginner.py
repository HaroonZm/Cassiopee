while True:
    try:
        c = int(raw_input())
    except EOFError:
        break
    if c % 39 == 0:
        print '3C39'
    else:
        r = c % 39
        if r < 10:
            print '3C0' + str(r)
        else:
            print '3C' + str(r)