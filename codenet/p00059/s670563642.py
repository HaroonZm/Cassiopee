try:
    while True:
        a = map(float, raw_input().split())
        if (a[0] < a[4] > a[2] or a[0] > a[6] < a[2] or
                a[1] < a[5] > a[3] or a[1] > a[7] < a[3]):
            print 'NO'
        else:
            print 'YES'
except EOFError:
    pass