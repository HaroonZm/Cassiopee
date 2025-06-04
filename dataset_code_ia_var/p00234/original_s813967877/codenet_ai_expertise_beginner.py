import queue

# Directions: right, down, left, up
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
    # Read grid width and height
    w, h = map(int, input().split())
    if w == 0:
        break
    
    # Read f, m, o
    f, m, o = map(int, input().split())
    
    # Read grid
    c = []
    for _ in range(h):
        c.append(list(map(int, input().split())))
    
    # Create distance array
    d = []
    for ox in range(m+1):
        temp = []
        for _ in range(h):
            temp.append([1e9]*w)
        d.append(temp)
    
    # Use priority queue for BFS
    q = queue.PriorityQueue()
    for j in range(w):
        val = -min(0, c[0][j])
        d[o-1][0][j] = val
        q.put((val, o-1, 0, j))
    
    while not q.empty():
        p = q.get()
        ox = p[1]
        i = p[2]
        j = p[3]
        if d[ox][i][j] < p[0] or ox <= 1:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if c[ni][nj] < 0:
                if d[ox-1][ni][nj] > d[ox][i][j] - c[ni][nj]:
                    d[ox-1][ni][nj] = d[ox][i][j] - c[ni][nj]
                    q.put((d[ox-1][ni][nj], ox-1, ni, nj))
            else:
                nox = ox-1 + c[ni][nj]
                if nox > m:
                    nox = m
                if d[nox][ni][nj] > d[ox][i][j]:
                    d[nox][ni][nj] = d[ox][i][j]
                    q.put((d[nox][ni][nj], nox, ni, nj))
    
    ans = 1e9
    for j in range(w):
        for ox in range(1, m+1):
            if d[ox][h-1][j] < ans:
                ans = d[ox][h-1][j]
    if ans <= f:
        print(int(ans))
    else:
        print("NA")