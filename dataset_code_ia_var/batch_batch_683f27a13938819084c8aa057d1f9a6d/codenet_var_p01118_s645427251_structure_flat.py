while True:
    h_w = input().split()
    h = int(h_w[0])
    w = int(h_w[1])
    if h == 0 and w == 0:
        break
    mp = {}
    r = 0
    while r < h:
        s = input()
        c = 0
        while c < w:
            mp[s[c]] = [r, c]
            c += 1
        r += 1
    s = input()
    now = [0, 0]
    ans = 0
    i = 0
    while i < len(s):
        ch = s[i]
        to = mp[ch]
        ans += abs(now[0] - to[0]) + abs(now[1] - to[1]) + 1
        now = to
        i += 1
    print(ans)