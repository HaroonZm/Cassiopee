while True:
    n = int(input())
    if n == 0:
        break
    input()
    pag = []
    dic = {}
    i = 0
    while i < n:
        s = input().split()
        nm = s[0]
        k = int(s[1])
        dic[nm] = i
        btn = []
        j = 0
        while j < k:
            s = input().split()
            x1 = int(s[0])
            y1 = int(s[1])
            x2 = int(s[2])
            y2 = int(s[3])
            bnm = s[4]
            btn.append((x1, y1, x2, y2, bnm))
            j += 1
        pag.append((nm, btn))
        i += 1
    buf = [0] * 2000
    now = 0
    sz = 1
    m = int(input())
    i = 0
    while i < m:
        a = input().split()
        if a[0] == "back":
            if now > 0:
                now -= 1
        elif a[0] == "forward":
            if now < sz - 1:
                now += 1
        elif a[0] == "show":
            print(pag[buf[now]][0])
        else:
            x = int(a[1])
            y = int(a[2])
            btn = pag[buf[now]][1]
            j = 0
            while j < len(btn):
                x1, y1, x2, y2, nm = btn[j]
                if x1 <= x <= x2 and y1 <= y <= y2:
                    now += 1
                    buf[now] = dic[nm]
                    sz = now + 1
                    break
                j += 1
        i += 1