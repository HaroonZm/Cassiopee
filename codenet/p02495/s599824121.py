while True:
    H, W = map(int,raw_input().split())
    if H==W==0:
        break
    for i in xrange(H):
        if W % 2 == 0:
            if i % 2 == 0:
                print '#' + '.#' * (W/2-1) + '.'
            else:
                print '.' + '#.' * (W/2-1) + '#'
        else:
            if i % 2 == 0:
                print '#' + '.#' * (W/2)
            else:
                print '.' + '#.' * (W/2)
    print