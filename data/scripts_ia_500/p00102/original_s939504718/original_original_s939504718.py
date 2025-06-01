while True:
    n = int(input())
    if n == 0:
        break
    total = [0] * (n + 1)
    for i in range(n):
        a = [int(i) for i in input().split()]
        a.append(sum(a))
        for j in range(n + 1):
            print("%5d" % (a[j]), end = "")
            total[j] += a[j]
        print()
    for i in range(n + 1):
        print("%5d" % (total[i]), end = "")
    print()