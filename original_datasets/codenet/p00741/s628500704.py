import sys
sys.setrecursionlimit(10000)

while(True):
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    c = [0] * h
    for i in range(h):
        c[i] = list(map(int,input().split()))

    checked = [[0] * w for _ in range(h)]
    def dfs(x,y):
        global checked,c
        checked[y][x] = 1
        c[y][x] = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if 0 <= x + i < w and 0 <= y + j < h:
                    if checked[y + j][x + i] == 0 and c[y + j][x + i] == 1:
                        dfs(x + i,y + j)

    cnt = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                dfs(j,i)
                cnt += 1

    print(cnt)