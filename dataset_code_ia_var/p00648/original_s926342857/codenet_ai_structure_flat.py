while True:
    n = int(input())
    if n == 0:
        break
    dic = {}
    tbl = []
    i = 0
    while i < n:
        parts = input().split()
        nm = parts[0]
        w = int(parts[1])
        s = int(parts[2])
        h = s // 100
        m = s % 100
        s = (1440 * w + h * 60 + m) % 10080
        e = s + 30
        tbl.append([s, e, 0, nm])
        dic[nm] = i
        i += 1
    m = int(input())
    j = 0
    while j < m:
        name = input()
        tbl[dic[name]][2] = 1
        j += 1
    if n == 1:
        print(1)
        continue
    tbl.sort(key=lambda x: (x[0], x[2]))
    idx = 0
    while idx < len(tbl):
        if tbl[idx][2]:
            k = idx
            break
        idx += 1
    ans = 1
    i = k
    j = k
    while True:
        j += 1
        if i >= n:
            i = 0
        if j >= n:
            j = 0
        if j == k:
            break
        e = tbl[i][1] - 10080 if tbl[i][1] >= 10080 else 0
        overlap1 = (tbl[i][0] <= tbl[j][0] and tbl[j][0] < tbl[i][1])
        overlap2 = tbl[j][0] < e
        if overlap1 or overlap2:
            if tbl[j][2] and tbl[i][2]:
                ans = -1
                break
            elif tbl[j][2]:
                i = j
        elif tbl[j][0] <= tbl[k][0] and tbl[k][0] < tbl[j][1]:
            pass
        else:
            ans += 1
            i = j
    print(ans)