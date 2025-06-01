while True:
    try:
        c = int(raw_input())
    except EOFError:
        break
    if c%39 ==0:
        print '3C39'
    else:
        print '3C' + str(c%39).zfill(2)