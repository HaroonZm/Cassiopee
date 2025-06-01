import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        wh = input()
        if not wh:
            break
        w,h = map(int, wh.split())
        if w == 0 and h == 0:
            break
        xs, ys = map(int, input().split())
        xg, yg = map(int, input().split())
        n = int(input())
        board = [[0]*(w+1) for _ in range(h+1)]  # 1-based indexing
        color_map = [[0]*(w+1) for _ in range(h+1)]
        for _ in range(n):
            c,d,x,y = map(int, input().split())
            # place block c on board
            if d == 0:
                # horizontal 2 x 4
                for dy in range(2):
                    for dx in range(4):
                        xx = x + dx
                        yy = y + dy
                        board[yy][xx] = 1
                        color_map[yy][xx] = c
            else:
                # vertical 4 x 2
                for dy in range(4):
                    for dx in range(2):
                        xx = x + dx
                        yy = y + dy
                        board[yy][xx] = 1
                        color_map[yy][xx] = c

        # check start and goal are on a block
        if not (1 <= xs <= w and 1 <= ys <= h and 1 <= xg <= w and 1 <= yg <= h):
            print("NG")
            continue
        if board[ys][xs] == 0 or board[yg][xg] == 0:
            print("NG")
            continue
        start_color = color_map[ys][xs]
        if start_color != color_map[yg][xg]:
            print("NG")
            continue

        visited = [[False]*(w+1) for _ in range(h+1)]
        from collections import deque
        q = deque()
        q.append((xs,ys))
        visited[ys][xs] = True
        found = False
        while q:
            x,y = q.popleft()
            if x == xg and y == yg:
                found = True
                break
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 1 <= nx <= w and 1 <= ny <= h:
                    if not visited[ny][nx] and board[ny][nx]==1 and color_map[ny][nx]==start_color:
                        visited[ny][nx] = True
                        q.append((nx,ny))
        print("OK" if found else "NG")

if __name__ == "__main__":
    main()