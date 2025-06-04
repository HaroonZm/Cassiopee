import heapq

INFINITE = float('inf')

def BFS(matrix, visited, queue, width, height):
    curr = heapq.heappop(queue)
    value = curr[0]; y = curr[1]; x = curr[2]

    def try_move(ny, nx, lv):
        if not visited[ny][nx]:
            heapq.heappush(queue, (lv, ny, nx))
            visited[ny][nx] = True

    # Up, Down, Left, Right
    if not visited[y-1][x]:
        try_move(y-1, x, matrix[y-2][x-1])
    if not visited[y+1][x]:
        try_move(y+1, x, matrix[y][x-1])
    if not visited[y][x-1]:
        try_move(y, x-1, matrix[y-1][x-2])
    if not visited[y][x+1]:
        try_move(y, x+1, matrix[y-1][x])
    return value

def mk_dict(mat, w, h, px, py):
    q = [(1, py, px)]
    us = [ [True]+[False]*w+[True] for k in range(h) ]
    us.insert(0, [True]*(w+2))
    us.append([True]*(w+2))
    us[py][px] = True
    acc = 0; mx = 0
    d = [[0,0]]
    def a(x): d.append(x)
    while q:
        v = BFS(mat, us, q, w, h)
        acc += 1
        if v > mx:
            a([v, acc])
            mx = v
        else:
            d[-1][1] += 1
    return d

def run():
    while 1:
        R = int(input())
        if R==0: break
        W1,H1,X1,Y1 = map(int, input().split())
        M1 = [ [*map(int,input().split())] for _ in range(H1) ]
        W2,H2,X2,Y2 = map(int, input().split())
        M2 = [ list(map(int, input().split())) for _ in range(H2)]
        D1 = mk_dict(M1, W1,H1,X1,Y1)
        D2 = mk_dict(M2, W2,H2,X2,Y2)
        n, m = len(D1), len(D2)
        i, j = 0, m-1
        res = INFINITE
        while i<n and j>0:
            s1, cnt1 = D1[i]
            s2, cnt2 = D2[j]
            if cnt1+cnt2 < R: i+=1; continue
            while j>0 and cnt1+cnt2 >= R:
                j -= 1
                s2,cnt2 = D2[j]
            if j==0 and cnt1+cnt2>=R:
                s = s1+s2
                res = min(res, s)
                break
            else:
                j += 1
                s2 = D2[j][0]
                s = s1+s2
                if s<res: res = s
            i+=1
        print(res)
run()