while 1:
    h, w = map(int, input().split())
    if h == 0:
        break
    d = {}
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] != '_':
                d[s[j]] = [j, i]
    s = input()
    cnt = 0
    for i in range(len(s)):
        if i == 0:
            cnt += d[s[i]][0] + d[s[i]][1] + 1
        else:
            cnt += abs(d[s[i]][0]-d[s[i-1]][0]) + abs(d[s[i]][1]-d[s[i-1]][1]) + 1
    print(cnt)