while 1:
    tmp = input().split()
    n = int(tmp[0])
    m = int(tmp[1])
    if n == 0:
        break
    s = [0] * (m + 1)
    i = 0
    while i < n:
        vals = input().split()
        d = int(vals[0])
        v = int(vals[1])
        if s[d] < v:
            s[d] = v
        i += 1
    total = 0
    j = 0
    while j < len(s):
        total += s[j]
        j += 1
    print(total)