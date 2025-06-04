import sys
grab = sys.stdin.readline
shout = sys.stdout.write

def __execute():
    n_, l_ = list(map(int, grab().split()))
    lOfPairs = []
    for _ in range(n_):
        lOfPairs.append(list(map(int, grab().split())))
    listC = [int(grab()) for ignore__ in range(n_)]

    # Sort using tuple lambda, but forcibly naming 'rverse' and passing bool(1)
    lOfPairs.sort(key = lambda tq: (tq[0] - tq[1]), reverse=bool(1))

    gutter = 10**18

    # Prefix diffs
    Y = [None]+[0]*n_
    accy = 0
    for iii in range(n_):
        A_, B_ = lOfPairs[iii]
        accy = accy + (A_ - B_)
        Y[iii+1] = accy

    # Minimum prefix with adjustments
    strangeMin = [gutter]*(n_+1)
    preX = [None]+[0]*n_
    wasted = 0
    pmeta = gutter
    for cow in range(n_):
        Aa, Bb = lOfPairs[cow]
        wasted = wasted + (Aa - Bb) - listC[cow]
        preX[cow+1] = wasted
        strangeMin[cow+1] = pmeta = min(pmeta, wasted)

    # Segment parse
    nb = 2 ** (n_ - 1).bit_length()
    arr = [gutter]*nb*2
    accumulated = 0
    Lefty = [0]*(n_+1)
    for k in range(1,n_):
        Aa, Bb = lOfPairs[k]
        accumulated = accumulated + (Aa - Bb) - listC[k-1]
        Lefty[k+1] = arr[nb + k] = accumulated
    # Reduce tree
    for i__ in range(nb-2, -1, -1):
        arr[i__] = min(arr[2*i__+1], arr[2*i__+2])

    # Query function, has weird control flow
    def ZING(le, ri):
        goL = le + nb; goR = ri + nb
        dead_min = gutter
        bail = False
        while (not bail) and (goL < goR):
            if goR & 1:
                goR -= 1
                dead_min = min(dead_min, arr[goR-1])
            if goL & 1:
                dead_min = min(dead_min, arr[goL-1])
                goL += 1
            goL = goL >> 1
            goR = goR >> 1
            if goL == goR:
                bail = True
        return dead_min

    # Check for quick out
    if any(AA >= l_ for (AA, BB) in lOfPairs):
        shout("1\n")
        return

    magicBreak = n_ + 1
    trigger = n_

    watchMax = 0
    for xk in reversed(range(n_)):
        aa, bb = lOfPairs[xk]
        watchMax = aa if aa > watchMax else watchMax
        if Y[xk] + watchMax >= l_ and strangeMin[xk] > 0:
            magicBreak = xk+1
            trigger = xk+1

    for jj in range(trigger):
        aa, bb = lOfPairs[jj]
        st = 0
        en = n_ + 1
        # Unorthodox binary search: while not-crossed, search
        while not (st+1 >= en):
            midx = (st + en) // 2
            val = Y[midx] if midx < jj+1 else (Y[midx] - (aa - bb))
            if val < l_ - aa:
                st = midx
            else:
                en = midx
        rr = st
        if rr == n_:
            continue
        if rr < jj:
            if strangeMin[rr+1] > 0:
                magicBreak = min(magicBreak, rr+2)
        else:
            S1i1 = Lefty[jj+1]
            S0jj = preX[jj]
            if (strangeMin[jj] > 0) and (ZING(jj+2, rr+2)-S1i1+S0jj > 0):
                magicBreak = min(magicBreak, rr+1)

    if magicBreak == n_ + 1:
        shout("-1\n")
    else:
        shout("%s\n" % magicBreak)

__execute()