pos = [0,1,2,0,-1,2,0,1,2]
while 1:
    s = raw_input()
    if s == "#": break
    ans = 10**9
    for ini in range(2):
        tmp = 0
        b = int(s[0])-1
        lr = ini
        for i in range(1,len(s)):
            f = int(s[i])-1
            if lr == 0:
                if pos[b] < pos[f]: tmp += 1
                else: lr = 1-lr
            else:
                if pos[b] > pos[f]: tmp += 1
                else: lr = 1-lr
            b = f
        ans = min(ans, tmp)
    print ans