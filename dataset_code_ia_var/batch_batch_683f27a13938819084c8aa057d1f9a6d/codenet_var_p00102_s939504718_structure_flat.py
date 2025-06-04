while True:
    n = int(input())
    if n == 0:
        break
    total = []
    for i in range(n + 1):
        total.append(0)
    i = 0
    while i < n:
        a = input().split()
        for idx in range(len(a)):
            a[idx] = int(a[idx])
        s = 0
        j = 0
        while j < n:
            s += a[j]
            j += 1
        a.append(s)
        j = 0
        while j < n + 1:
            print("%5d" % a[j], end="")
            total[j] += a[j]
            j += 1
        print()
        i += 1
    i = 0
    while i < n + 1:
        print("%5d" % total[i], end="")
        i += 1
    print()