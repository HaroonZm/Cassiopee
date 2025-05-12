#! /usr/bin/python

(t, p, r) = map(int, raw_input().split())
while t!=0:
    pena = [0]*t
    pub = [[False]*p for i in range(t)]
    mis = [[0]*p for i in range(t)]
    num = [0]*t
    for i in range(r):
        (tid, pid, time, mes) = raw_input().split()
        tid = int(tid)-1
        pid = int(pid)-1
        time = int(time)
        if pub == True:
            continue
        if mes == "CORRECT":
            pub[tid][pid] = True
            pena[tid] += mis[tid][pid]*1200+time
            num[tid] += 1
        else:
            mis[tid][pid] += 1
    order = []
    for i in range(t):
        order.append([-num[i], pena[i], i])
    order.sort()
    for i in range(t):
        print order[i][2]+1, -order[i][0], order[i][1]

    (t, p, r) = map(int, raw_input().split())