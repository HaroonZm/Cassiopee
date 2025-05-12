Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

while 1:
    try:
        roman = raw_input()
    except EOFError:
        break
    phase = 1000
    ret = 0
    cnt = 0
    for x in roman:
        cur = Roman[x]
        if cur < phase:
            ret += phase * cnt
            phase = cur
            cnt = 1
        elif cur == phase:
            cnt += 1
        elif cur > phase:
            ret += cur - cnt * phase
            phase = cur
            cnt = 0
    else:
        ret += phase * cnt
    print ret