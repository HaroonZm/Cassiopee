while True:
    n = int(raw_input())
    if n == 0:
        break
    a = [0]
    i = 0
    while i < n:
        a.append(int(raw_input()) + a[-1])
        i += 1
    mx = -100000
    i = 0
    while i < n:
        j = i + 1
        while j < n + 1:
            if a[j] - a[i] > mx:
                mx = a[j] - a[i]
            j += 1
        i += 1
    print mx