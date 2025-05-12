pos = [0,1,2,0,-1,2,0,1,2]
while 1:
    s = raw_input()
    if s == "#": break
    ans = 10**9
    for ini in range(2):
        tmp = 0
        b = pos[int(s[0])-1]
        lr = ini
        for i in s[1:]:
            f = pos[int(i)-1]
            if [b<f, b>f][lr]: tmp += 1
            else: lr = 1-lr
            b = f
        ans = min(ans, tmp)
    print ans