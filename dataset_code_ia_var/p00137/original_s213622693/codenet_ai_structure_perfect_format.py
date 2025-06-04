for i in range(input()):
    s = int(raw_input())
    print 'Case %s:' % str(i + 1)
    for j in range(10):
        n_s = str(s ** 2).zfill(8)[2:-2]
        s = int(n_s)
        print s