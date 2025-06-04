while 1:
    n = input()
    if n == 0:
        break
    b = map(int, raw_input().split())
    count = 0
    while count < 10001:
        if b[0] == 1:
            i = 0
            while i < len(b) - 1:
                if b[i + 1] - b[i] != 1:
                    break
                i += 1
            else:
                print count
                break
        l = len(b)
        i = 0
        while i < l:
            b[i] -= 1
            i += 1
        b.append(l)
        while True:
            try:
                idx = b.index(0)
                del b[idx]
            except ValueError:
                break
        count += 1
    else:
        print -1