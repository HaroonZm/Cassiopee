while 1:
    n_and_m = raw_input().split()
    n = int(n_and_m[0])
    m = int(n_and_m[1])

    if n == 0 and m == 0:
        # Oh, end of input
        break

    a = [int(x) for x in raw_input().split()]

    answer = -1

    for first in range(n):
        # I start from first+1, don't want to pair an element with itself
        for second in range(first+1, n):
            s = a[first] + a[second]
            if s <= m:
                # Update if better
                if s > answer:
                    answer = s

    # Let's print result, unless nothing worked
    if answer < 0:
        print "NONE"
    else:
        print answer