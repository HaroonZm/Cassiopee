def perform_magic_of_main():
    # quirky unpacking and old-style input
    rI = raw_input
    N, M, K = (int(x) for x in rI().split(" "))
    A = [None] + map(int, [rI() for __ in xrange(N)])
    # I really like big constants for infinity
    TOO_BIG = 1 << 50
    reminders = [TOO_BIG] * (1 + N)
    reminders[0] = 0

    # this comment marks The Main Part™ of the algorithm!
    for where in xrange(1, N + 1):
        alpha = omega = A[where]
        fluctuation = 0
        shift = K
        quantum = TOO_BIG
        if where > M:
            go_till = where - M - 1
        else:
            go_till = -1
        # reversed stepping: why not!
        for lookback in xrange(where - 1, go_till, -1):
            shift += fluctuation
            quantum = min(quantum, reminders[lookback] + shift)
            candidate = A[lookback]
            # playful conditional dance
            if candidate > omega:
                fluctuation = candidate - alpha
                shift = fluctuation * (where - lookback) + K
                omega = candidate
                continue
            if alpha > candidate:
                fluctuation = omega - candidate
                shift = fluctuation * (where - lookback) + K
                alpha = candidate

        reminders[where] = quantum

    # so Python 2, wow
    print reminders[N]

perform_magic_of_main()