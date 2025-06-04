mv = [[-1,-1,-1],[-1,-1,0],[-1,-1,1],[-1,0,-1],[-1,0,0],[-1,0,1],[-1,1,-1],[-1,1,0],[-1,1,1],
      [0,-1,-1],[0,-1,0],[0,-1,1],[0,0,-1],[0,0,1],[0,1,-1],[0,1,0],[0,1,1],
      [1,-1,-1],[1,-1,0],[1,-1,1],[1,0,-1],[1,0,0],[1,0,1],[1,1,-1],[1,1,0],[1,1,1]]

cno = 0
arr = [[[[0 for x in range(5)] for y in range(5)] for z in range(5)] for k in range(2)]
while True:
    n = int(input())
    if n == 0: break
    for z in range(5):
        if z > 0:
            input()
        for y in range(5):
            s = input()
            arr[0][z][y] = list(map(int, s))
    a = [0]*27
    b = [0]*27
    ts = input()
    if len(ts) == 0:
        ts = input()
    ts = list(map(int, ts.split()))
    for t in ts[1:]:
        a[t] = 1
    ts2 = input()
    while len(ts2.strip()) == 0:
        ts2 = input()
    ts2 = list(map(int, ts2.strip().split()))
    for t in ts2[1:]:
        b[t] = 1
    for j in range(n):
        for z in range(5):
            for y in range(5):
                for x in range(5):
                    s = 0
                    for i in range(26):
                        xx = x + mv[i][0]
                        yy = y + mv[i][1]
                        zz = z + mv[i][2]
                        if 0 <= xx < 5 and 0 <= yy < 5 and 0 <= zz < 5:
                            s += arr[j&1][zz][yy][xx] & 1
                    if arr[j&1][z][y][x] & 1:
                        arr[1-(j&1)][z][y][x] = b[s]
                    else:
                        arr[1-(j&1)][z][y][x] = a[s]
    if cno:
        print()
    cno += 1
    print("Case ", cno, ":", sep='')
    for z in range(5):
        if z > 0:
            print()
        for y in range(5):
            print(*arr[n&1][z][y], sep='')