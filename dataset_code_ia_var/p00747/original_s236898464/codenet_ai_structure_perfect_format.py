from collections import deque

while True:
    ans = 0
    vertical = []
    horizantal = []
    w, h = map(int, input().split())
    G = [[10**6 for _ in range(w)] for _ in range(h)]
    if (w, h) == (0, 0):
        break
    for i in range(2 * h - 1):
        if i % 2 == 0:
            vertical.append(list(map(int, input().split())))
        else:
            horizantal.append(list(map(int, input().split())))
    queue = deque([(0, 0)])
    G[0][0] = 0
    while len(queue) != 0:
        now = queue.popleft()
        dw = [(0, -1), (0, 1)]
        dh = [(1, 0), (-1, 0)]
        for move in dw:
            nexte = (now[0], now[1] + move[1])
            if nexte[1] < 0 or nexte[1] >= w:
                continue
            else:
                if move[1] == 1:
                    if vertical[now[0]][now[1]] == 0:
                        if G[nexte[0]][nexte[1]] > G[now[0]][now[1]] + 1:
                            G[nexte[0]][nexte[1]] = G[now[0]][now[1]] + 1
                            queue.append((nexte[0], nexte[1]))
                elif move[1] == -1:
                    if vertical[nexte[0]][nexte[1]] == 0:
                        if G[nexte[0]][nexte[1]] > G[now[0]][now[1]] + 1:
                            G[nexte[0]][nexte[1]] = G[now[0]][now[1]] + 1
                            queue.append((nexte[0], nexte[1]))
        for move in dh:
            nexte = (now[0] + move[0], now[1])
            if nexte[0] < 0 or nexte[0] >= h:
                continue
            else:
                if move[0] == 1:
                    if horizantal[now[0]][now[1]] == 0:
                        if G[nexte[0]][nexte[1]] > G[now[0]][now[1]] + 1:
                            G[nexte[0]][nexte[1]] = G[now[0]][now[1]] + 1
                            queue.append((nexte[0], nexte[1]))
                elif move[0] == -1:
                    if horizantal[nexte[0]][nexte[1]] == 0:
                        if G[nexte[0]][nexte[1]] > G[now[0]][now[1]] + 1:
                            G[nexte[0]][nexte[1]] = G[now[0]][now[1]] + 1
                            queue.append((nexte[0], nexte[1]))
    if G[h - 1][w - 1] == 10**6:
        print(0)
    else:
        print(G[h - 1][w - 1] + 1)