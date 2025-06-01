while True:
    n = int(input())
    if n == 0:
        break
    total = [0] * (n + 1)
    for _ in range(n):
        a = [int(x) for x in input().split()]
        s = sum(a)
        a.append(s)
        for j in range(n + 1):
            print("%5d" % a[j], end="")
            total[j] += a[j]
        print()
    for j in range(n + 1):
        print("%5d" % total[j], end="")
    print()