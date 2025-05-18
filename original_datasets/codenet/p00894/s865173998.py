while 1:
    n = input()
    if n == 0:
        break
    status = {}
    god_st = -1
    res = {}
    for i in xrange(n):
        s = raw_input().split()
        #M, D = map(int, s[0].split("/"))
        h, m = map(int, s[1].split(":"))
        mi = 60*h + m
        st = s[2] == 'I'
        ID = s[3]

        if ID == '000':
            # goddness
            if st == 1:
                god_st = mi
            else:
                for k in status:
                    if k != ID and status[k] != -1:
                        res[k] = res.get(k, 0) + (mi - max(god_st, status[k]))
                god_st = -1
        else:
            if st == 1:
                status[ID] = mi
            else:
                if god_st != -1:
                    res[ID] = res.get(ID, 0) + (mi - max(god_st, status[ID]))
                status[ID] = -1
    print max(res.values()) if res else 0