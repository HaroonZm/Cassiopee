def bfs(start_y,start_x,goal_y,goal_x):
    bfs_map = [[-1 for x in range(w)] for y in range(h)]
    move_y = [1,-1,0,0]
    move_x = [0,0,1,-1]
    data_y = [start_y]
    data_x = [start_x]
    bfs_map[start_y][start_x] = 1
    while len(data_x) != 0:
        y = data_y.pop(0)
        x = data_x.pop(0)
        for i in range(4):
            y += move_y[i]
            x += move_x[i]
            if y >= 0 and y < h and x >= 0 and x < w:
                if y == goal_y and x == goal_x:
                    return "Yes"
                if bfs_map[y][x] == -1 and stage[y][x] == ".":
                    bfs_map[y][x] = 1
                    data_y.append(y)
                    data_x.append(x)
            y -= move_y[i]
            x -= move_x[i]
    return "No"
h,w,d,n = map(int, input().split())
stage = [input() for i in range(h)]
r = list(map(int, input().split()))
da = [list(map(int, input().split())) for i in range(n)]
ma = [[0 for x in range(w)] for y in range(h)]
for x,y,s in da:
    if s == d:
        for i in range(h):
            for j in range(w):
                ma[i][j] += 1
    if s < d:
        for i in range(y-r[s], y+r[s]+1):
            for j in range(x-r[s], x+r[s]+1):
                if i >= 0 and i < h and j >= 0 and j < w:
                    ma[i][j] += 1
    if s != 0:
        for i in range(y-r[s-1], y+r[s-1]+1):
            for j in range(x-r[s-1], x+r[s-1]+1):
                if i >= 0 and i < h and j >= 0 and j < w:
                    ma[i][j] -= 1
ans = []
for i in range(h):
    for j in range(w):
        if stage[i][j] == "D":
            o = i
            l = j
        if ma[i][j] == n and stage[i][j] != "#":
            ans.append([i,j])
if len(ans) == 0:
    print("Broken")
    quit()
key = ["Broken" for i in range(len(ans))]
for i in range(len(ans)):
    key[i] = bfs(o,l,ans[i][0],ans[i][1])
    if o == ans[i][0] and l == ans[i][1]:
        key[i] = "Yes"
for i in range(1,len(key)):
    if key[i] != key[i-1]:
        print("Unknown")
        quit()
print(key[0])