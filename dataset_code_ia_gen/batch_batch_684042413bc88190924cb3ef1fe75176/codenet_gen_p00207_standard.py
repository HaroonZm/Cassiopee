from collections import deque

def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        xs, ys = map(int, input().split())
        xg, yg = map(int, input().split())
        n = int(input())
        board = [[0]*(w+1) for _ in range(h+1)]
        for _ in range(n):
            c, d, x, y = map(int, input().split())
            if d == 0:  # horizontal 2x4 block (width=4, height=2)
                for dy in range(2):
                    for dx in range(4):
                        board[y+dy][x+dx] = c
            else:  # vertical 4x2 block (width=2, height=4)
                for dy in range(4):
                    for dx in range(2):
                        board[y+dy][x+dx] = c
        start_color = board[ys][xs]
        if start_color == 0:
            print("NG")
            continue
        visited = [[False]*(w+1) for _ in range(h+1)]
        q = deque()
        q.append((xs, ys))
        visited[ys][xs] = True
        found = False
        while q:
            x, y = q.popleft()
            if x == xg and y == yg:
                found = True
                break
            for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 1 <= nx <= w and 1 <= ny <= h:
                    if not visited[ny][nx] and board[ny][nx] == start_color:
                        visited[ny][nx] = True
                        q.append((nx, ny))
        print("OK" if found else "NG")

main()