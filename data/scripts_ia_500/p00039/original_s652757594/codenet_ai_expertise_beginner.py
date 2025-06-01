Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

while True:
    try:
        roman = input()
    except EOFError:
        break

    phase = 1000
    ret = 0
    cnt = 0

    for x in roman:
        cur = Roman[x]
        if cur < phase:
            ret = ret + phase * cnt
            phase = cur
            cnt = 1
        elif cur == phase:
            cnt = cnt + 1
        else:  # cur > phase
            ret = ret + cur - cnt * phase
            phase = cur
            cnt = 0

    ret = ret + phase * cnt
    print(ret)