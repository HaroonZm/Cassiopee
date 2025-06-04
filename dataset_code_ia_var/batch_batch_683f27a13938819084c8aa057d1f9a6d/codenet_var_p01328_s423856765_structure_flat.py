import bisect

while 1:
    inputs = raw_input().split()
    N = int(inputs[0])
    M = int(inputs[1])
    if M == 0:
        break
    Clist = []
    Eloc = []
    catinE = [0] * M
    idinE = [[] for _ in range(M)]
    for i in range(N):
        vals = raw_input().split()
        Clist.append([int(vals[0]), int(vals[1]), int(vals[2])])
    for j in range(M):
        x = int(raw_input())
        Eloc.append(x)
    Eloc.sort()
    ans = sum([Clist[i][2] for i in range(N)])
    for i in range(N):
        baitid = bisect.bisect_left(Eloc, Clist[i][0])
        if baitid == 0:
            leftclose = -1e10
            rightclose = Eloc[baitid]
        elif baitid == len(Eloc):
            leftclose = Eloc[baitid - 1]
            rightclose = 1e10
        else:
            leftclose = Eloc[baitid - 1]
            rightclose = Eloc[baitid]
        if abs(Clist[i][0] - leftclose) <= abs(Clist[i][0] - rightclose):
            catinE[baitid - 1] += Clist[i][2]
            idinE[baitid - 1].append(i)
        else:
            catinE[baitid] += Clist[i][2]
            idinE[baitid].append(i)
    for j in range(M - 1):
        ans = min(ans, max(catinE))
        btd = catinE.index(max(catinE))
        cattomove = idinE[btd][:]
        del Eloc[btd]
        del catinE[btd]
        del idinE[btd]
        for i in range(len(catinE)):
            catinE[i] = 0
            idinE[i] = []
        for idx in cattomove:
            baitid = bisect.bisect_left(Eloc, Clist[idx][0])
            if baitid == 0:
                leftclose = -1e10
                rightclose = Eloc[baitid]
            elif baitid == len(Eloc):
                leftclose = Eloc[baitid - 1]
                rightclose = 1e10
            else:
                leftclose = Eloc[baitid - 1]
                rightclose = Eloc[baitid]
            if abs(Clist[idx][0] - leftclose) <= abs(Clist[idx][0] - rightclose):
                catinE[baitid - 1] += Clist[idx][2]
                idinE[baitid - 1].append(idx)
            else:
                catinE[baitid] += Clist[idx][2]
                idinE[baitid].append(idx)
    print ans