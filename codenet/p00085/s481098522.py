while 1:
    n, m = map(int, input().split())
    if n == 0:
        break

    s = [i for i in range(1, n + 1)]

    ind = n - 1
    while len(s) > 1:
        ind = (ind + m) % len(s)
        s.pop(ind)
        ind -= 1
    print(s[0])