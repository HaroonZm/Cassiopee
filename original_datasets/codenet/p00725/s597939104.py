from collections import deque
import sys
input = sys.stdin.readline

def main():
    while True:
        w, h = map(int, input().split())
        if w == 0:
            break
        # 読み込み
        board = [list(map(int, input().split())) for i in range(h)]
        # 地図を整形
        # wall : ID( 1~ )
        # air: 0
        s_x, s_y, g_x, g_y = 0, 0, 0, 0; id = 1;
        for y in range(h):
            for x in range(w):
                if board[y][x] == 1:
                    board[y][x] = id
                    id += 1
                elif board[y][x] == 2:
                    s_x = x; s_y = y;
                    board[y][x] = 0
                elif board[y][x] == 3:
                    g_x = x; g_y = y;
                    board[y][x] = 0
        # スタートから幅優先探索
        search_list = deque()
        search_list.append([s_x, s_y, 0, 0, 0, [0], 1])
        ans = -1
        check = []
        while len(search_list) > 0:
            # print(search_list)
            x, y, step, dx, dy, through, count = search_list.popleft()
            if x == g_x and y == g_y:
                ans = step
                break
            if dx == 0 and dy == 0:# 動き始めの処理
                if step+1 < 11:
                    for next_x, next_y in [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]:
                        if 0 <= next_x and next_x < w and 0 <= next_y and next_y < h:
                            tmp = board[next_y][next_x]
                            if tmp in through[:count]:
                                search_list.append([next_x, next_y, step+1, next_x-x, next_y-y, through[:count], count])
            else:# 壁にぶつかるまで滑る
                t_x = x; t_y = y;
                drop = False
                goal = False
                while True:
                    n_x = t_x + dx; n_y = t_y + dy;
                    if n_x == g_x and n_y == g_y:
                        ans = step
                        goal = True
                        break
                    if 0 <= n_x and n_x < w and 0 <= n_y and n_y < h:
                        if board[n_y][n_x] not in through[:count]:
                            break
                    else:
                        drop = True
                        break
                    t_x += dx; t_y += dy;
                if goal:
                    break
                if not drop:
                    tmp = board[t_y+dy][t_x+dx]
                    through = through[:count] + [tmp]
                    search_list.append([t_x, t_y, step, 0, 0, through, count+1])
        print(ans)

if __name__ == "__main__":
    main()