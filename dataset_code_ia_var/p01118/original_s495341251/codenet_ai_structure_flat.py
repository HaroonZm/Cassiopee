while 1:
    h_w = input().split()
    h = int(h_w[0])
    w = int(h_w[1])
    if h == 0:
        break
    d = {}
    for i in range(h):
        s = input()
        j = 0
        while j < w:
            if s[j] != '_':
                d[s[j]] = [j, i]
            j += 1
    s = input()
    cnt = 0
    i = 0
    while i < len(s):
        if i == 0:
            cnt += d[s[i]][0] + d[s[i]][1] + 1
        else:
            cnt += abs(d[s[i]][0] - d[s[i-1]][0]) + abs(d[s[i]][1] - d[s[i-1]][1]) + 1
        i += 1
    print(cnt)