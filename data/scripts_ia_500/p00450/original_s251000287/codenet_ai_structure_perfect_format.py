while True:
    n = int(raw_input())
    if n == 0:
        break
    else:
        top = -1
        fault = [0]
        S = 0
        for i in range(n // 2):
            s = int(raw_input())
            if top != s:
                fault.append(i)
                top = s
            s = int(raw_input())
            if top != s:
                fault.pop()
                top = s
            if not fault:
                fault = [0]
        i = len(fault) - 1
        while i > 0:
            S += (fault[i] - fault[i - 1]) * 2
            i -= 2
        if not top:
            S = 2 * (n // 2) - S
        if n % 2 == 1:
            s = int(raw_input())
            S += (1 - s)
        print S