def get_vals():
    return [int(x) for x in input().split()]
vals = get_vals()
now = 0
used = [0] * 60
while 1:
    st = now + vals[0]
    nm = now % 60; sm = st % 60
    if nm < sm:
        if nm <= vals[2] <= sm:
            r = now // 60 * 60 + vals[2]
            print(r)
            break
        now = st + vals[1]
    else:
        if nm <= vals[2] < 60 or 0 < vals[2] <= sm:
            print(now // 60 * 60 + vals[2]); break
        now = st + vals[1]
    if (now % 60) == 0:
        print(-1)
        exit()