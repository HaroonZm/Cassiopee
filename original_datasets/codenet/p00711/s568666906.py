def solve(dat):
    H = len(dat)
    W = len(dat[0])

    for i in range(H):
        for j in range(W):
            if dat[i][j] == "@":
                si, sj = i, j

    tmp = [[0 for _ in range(W)] for _ in range(H)]
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    pool = [(si, sj)]

    while len(pool) > 0:
        # print pool, i, j
        i, j = pool.pop()
        tmp[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(H) and nj in range(W) and dat[ni][nj] == "." and tmp[ni][nj] == 0:
                pool.append((ni, nj))
    cnt = sum([sum(tmp[i]) for i in range(H)])
    return cnt

while True:
    W, H = map(int, raw_input().split(" "))
    if W == H == 0:
        break
    dat = [raw_input() for _ in range(H)]
    print solve(dat)