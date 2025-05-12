while 1:
    a, b = map(int, raw_input().split())
    if not a and not b:
        break
    if a < b:
        print "%d %d" % (a, b)
    else:
        print "%d %d" % (b, a)