n = int(raw_input())
for _ in range(n):
    a = map(int, raw_input().split())
    b = 0
    c = 0
    ok = 1
    for i in a:
        if i > b:
            b = i
        elif i > c:
            c = i
        else:
            ok = 0
            break
    if ok:
        print "YES"
    else:
        print "NO"