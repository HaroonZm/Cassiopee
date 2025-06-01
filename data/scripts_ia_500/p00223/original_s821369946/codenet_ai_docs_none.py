direc = ((1,0),(-1,0),(0,1),(0,-1))

while 1:
    X, Y = list(map(int,input().split()))
    if X == 0: break
    ftx, fty = list(map(lambda x: x-1, map(int, input().split())))
    fkx, fky = list(map(lambda x: x-1, map(int, input().split())))
    m = [list(map(int, input().split())) for i in range(Y)]
    d = {(ftx, fty, fkx, fky): 0}
    s = [[0, (ftx, fty, fkx, fky)]]
    res = 'NA'
    while len(s) > 0:
        spm = s.pop(0)
        cnt = spm[0] + 1
        if cnt > 100:
            break
        def search_move():
            for i in range(4):
                tx = spm[1][0]+direc[i][0]
                ty = spm[1][1]+direc[i][1]
                kx = spm[1][2]-direc[i][0]
                ky = spm[1][3]-direc[i][1]
                hm = 0
                if tx < 0 or tx >= X or ty < 0 or ty >= Y or m[ty][tx] == 1:
                    tx = spm[1][0]
                    ty = spm[1][1]
                    hm += 1
                if kx < 0 or kx >= X or ky < 0 or ky >= Y or m[ky][kx] == 1:
                    kx = spm[1][2]
                    ky = spm[1][3]
                    hm += 1
                if hm == 2: continue
                tpl = (tx,ty,kx,ky)
                if tpl in d and d[tpl] <= cnt:
                    continue
                if tx == kx and ty == ky:
                    return True
                else:
                    s.append([cnt,tpl])
                    d[tpl] = cnt
            return False
        if search_move():
            res = str(cnt)
            break
    print(res)