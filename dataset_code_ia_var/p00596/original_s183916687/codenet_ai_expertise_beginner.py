import sys

sys.setrecursionlimit(10000000)

while True:
    try:
        n = input()
    except:
        break
    A = raw_input().split()
    E = []
    for i in range(7):
        E.append([])
    for s in A:
        u = int(s[0])
        v = int(s[1])
        E[u].append(v)
        E[v].append(u)
    cnt = 0
    for i in range(7):
        if len(E[i]) % 2 == 1:
            cnt += 1
    if cnt > 2:
        print "No"
        continue
    used = []
    for i in range(7):
        if len(E[i]) == 0:
            used.append(True)
        else:
            used.append(False)
    def func(num):
        if used[num]:
            return
        used[num] = True
        for u in E[num]:
            func(u)
    started = False
    for i in range(7):
        if len(E[i]) > 0 and not started:
            func(i)
            started = True
    ok = True
    for i in range(7):
        if not used[i]:
            ok = False
    if ok:
        print "Yes"
    else:
        print "No"