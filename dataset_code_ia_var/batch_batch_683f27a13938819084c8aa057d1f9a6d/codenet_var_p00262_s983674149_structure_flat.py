while True:
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
        i = 0
        while i < len(b):
            b[i] -= 1
            i += 1
        b.append(len(b))
        while b.count(0):
            idx = 0
            while idx < len(b):
                if b[idx] == 0:
                    del b[idx]
                    break
                idx += 1
        count += 1
    else:
        print -1