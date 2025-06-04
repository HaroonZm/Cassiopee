from collections import deque

M, N, K = map(int, input().split())
switch_rooms = set()
for _ in range(K):
    x, y = map(int, input().split())
    switch_rooms.add((x, y))

# 状態は (x, y, door_state)
# door_state: 0=初期状態(東西の扉閉, 南北の扉開)
#             1=スイッチ押して反転後の状態
# 移動方向は上下左右4方向
# 東西の扉は初期状態で閉じている → 通れるのは反転状態の時
# 南北の扉は初期状態で開いている → 通れるのは初期状態の時
# スイッチのある部屋で1分間押すと反転する(state切り替え、時間+1)
# 移動に1分

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[False]*2 for _ in range(N+1)] for __ in range(M+1)]
queue = deque()
queue.append((1,1,0,0))  # x, y, state, time
visited[1][1][0] = True

while queue:
    x, y, state, time = queue.popleft()
    if (x, y) == (M, N):
        print(time)
        break

    # スイッチがあるなら押して反転できる（状態変化のみ）
    if (x, y) in switch_rooms:
        new_state = 1 - state
        if not visited[x][y][new_state]:
            visited[x][y][new_state] = True
            queue.append((x, y, new_state, time+1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= M and 1 <= ny <= N:
            # 移動可能判定
            # 東西方向(左右)の扉はstate==1で開いている（通れる）
            if nx != x:
                if state == 1:
                    if not visited[nx][ny][state]:
                        visited[nx][ny][state] = True
                        queue.append((nx, ny, state, time+1))
            # 南北方向(上下)の扉はstate==0で開いている（通れる）
            else:
                if state == 0:
                    if not visited[nx][ny][state]:
                        visited[nx][ny][state] = True
                        queue.append((nx, ny, state, time+1))
else:
    print(-1)