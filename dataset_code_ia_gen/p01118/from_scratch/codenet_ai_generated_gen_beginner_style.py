while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    osk = []
    for _ in range(h):
        osk.append(input())
    s = input()
    pos = {}
    for i in range(h):
        for j in range(w):
            c = osk[i][j]
            if c != '_':
                pos[c] = (i,j)
    cur = (0,0)
    presses = 0
    for ch in s:
        target = pos[ch]
        presses += abs(target[0]-cur[0]) + abs(target[1]-cur[1]) + 1
        cur = target
    print(presses)