while True:
    n = int(raw_input())
    if n == 0:
        break
    top = None
    fault = [0]
    S = 0
    count = 0
    for i in xrange(n//2):
        s = int(raw_input())
        if top != s:
            fault.append(i)
            top = s
        s2 = int(raw_input())
        if top != s2:
            if fault:
                fault.pop()
            top = s2
        if not fault:
            fault = [0]
    i = len(fault) - 1
    while i > 0:
        S += (fault[i] - fault[i-1]) * 2
        i -= 2
    if not top:
        S = 2 * (n//2) - S
    if n % 2 == 1:
        s_extra = int(raw_input())
        S += 1 - s_extra
    print S