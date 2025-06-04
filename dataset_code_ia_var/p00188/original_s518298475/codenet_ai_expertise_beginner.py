while True:
    n = input()
    n = int(n)
    if n == 0:
        break
    L = []
    for i in range(n):
        L.append(input())
    v = input()
    l = 0
    r = len(L) - 1
    cnt = 0
    found = False
    while l <= r:
        m = (l + r) // 2
        if L[m] == v:
            print(cnt + 1)
            found = True
            break
        elif L[m] < v:
            l = m + 1
        else:
            r = m - 1
        cnt = cnt + 1
    if not found:
        print(cnt)