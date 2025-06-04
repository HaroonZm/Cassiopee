while True:
    n = input()
    if n == 0:
        break
    mi = 501
    ma = 0
    for i in range(n):
        s = sum(map(int, raw_input().split()))
        mi = min(s, mi)
        ma = max(s, ma)
    print "%d %d" % (ma, mi)