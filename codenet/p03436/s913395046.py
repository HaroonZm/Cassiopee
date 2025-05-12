from collections import deque
H, W = map(int,input().split())
grid = [list(input()) for _ in range(H)]
w_cnt = 0
for i in range(H):
    w_cnt += grid[i].count('.')

inf = float('inf')
d = [[inf]*W for _ in range(H)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

d[0][0] = 0
que = deque()
que.append([0,0])
while len(que) != 0:
    p = que.popleft()
    if p[0] == W-1 and p[1] == H-1:break
    for i in range(4):
        nx = p[0] + dx[i]
        ny = p[1] + dy[i]
        #print(nx,ny)
        if 0 <= nx <= W-1 and 0 <= ny <= H-1 and grid[ny][nx] == '.' and d[ny][nx] == inf:
            que.append([nx,ny])
            d[ny][nx] = d[p[1]][p[0]] + 1

# print(d)
# print(d[H-1][W-1])
if d[H-1][W-1] == inf:
    print(-1)
else:
    print(w_cnt-d[H-1][W-1]-1)