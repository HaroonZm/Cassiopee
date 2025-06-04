while True:
    h, w = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    s1 = '#' * w
    s2 = '#' + '.' * (w - 2) + '#'
    print s1
    for j in range(1, h - 1):
        print s2
    if h > 1:
        print s1
    print