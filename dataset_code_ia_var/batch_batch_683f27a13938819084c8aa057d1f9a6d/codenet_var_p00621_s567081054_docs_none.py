while 1:
    W, Q = map(int, raw_input().split())
    if W == 0 and Q == 0: break
    se = [(0, 0), (W, W)]
    idq = [10000, 100001]
    for i in range(Q):
        S = raw_input().split()
        Sn = [int(x) for x in S[1:]]
        if S[0] == 's':
            for i in range(len(se) - 1):
                if se[i + 1][0] - se[i][1] >= Sn[1]:
                    print se[i][1]
                    se.insert(i + 1, (se[i][1], se[i][1] + Sn[1]))
                    idq.insert(i + 1, Sn[0])
                    break
            else:
                print 'impossible'
        if S[0] == 'w':
            i = idq.index(Sn[0])
            del se[i]
            del idq[i]
    print 'END'