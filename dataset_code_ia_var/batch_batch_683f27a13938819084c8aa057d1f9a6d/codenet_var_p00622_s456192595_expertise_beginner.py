while True:
    s = input()
    if s[0] == '-':
        break
    t = input()
    p = input()
    s = list(s)
    t = list(t)
    p = list(p)
    if len(t) == 0:
        print("")
        continue
    k = t.pop(0)
    ans = ""
    ok = True
    while len(s) > 0 or len(t) > 0:
        if len(p) > 0 and p[0] == k:
            if len(s) > 0:
                k = s.pop(0)
            p.pop(0)
        else:
            ans += k
            if len(t) > 0:
                k = t.pop(0)
            else:
                ok = False
                break
    if ok:
        ans += k
    print(ans)