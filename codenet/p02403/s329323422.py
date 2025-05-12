while True:
    try:
        (h,w)=map(int,raw_input().split())
        if h==0 and w==0: break
        for i in xrange(h):
            print ''.join(['#' for j in xrange(w)])
        print
    except EOFError: break