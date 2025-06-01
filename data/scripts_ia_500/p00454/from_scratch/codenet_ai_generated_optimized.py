import sys
sys.setrecursionlimit(10**7)

def solve():
    input = sys.stdin.readline
    while True:
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        n = int(input())
        xs = [0,w]
        ys = [0,h]
        rects = []
        for _ in range(n):
            x1,y1,x2,y2 = map(int,input().split())
            xs.extend([x1,x2])
            ys.extend([y1,y2])
            rects.append((x1,y1,x2,y2))
        xs = sorted(set(xs))
        ys = sorted(set(ys))

        # 座標を圧縮
        x_id = {x:i for i,x in enumerate(xs)}
        y_id = {y:i for i,y in enumerate(ys)}

        W = len(xs)-1
        H = len(ys)-1

        board = [[False]*W for _ in range(H)]
        # マスキングテープ部分＝Trueで塗る
        for x1,y1,x2,y2 in rects:
            xi1 = x_id[x1]
            xi2 = x_id[x2]
            yi1 = y_id[y1]
            yi2 = y_id[y2]
            for y in range(yi1,yi2):
                for x in range(xi1,xi2):
                    board[y][x] = True

        visited = [[False]*W for _ in range(H)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def in_board(y,x):
            return 0 <= y < H and 0 <= x < W

        def dfs(sy,sx):
            stack = [(sy,sx)]
            visited[sy][sx] = True
            while stack:
                y,x = stack.pop()
                for dy,dx in directions:
                    ny,nx = y+dy,x+dx
                    if in_board(ny,nx) and not visited[ny][nx] and not board[ny][nx]:
                        visited[ny][nx] = True
                        stack.append((ny,nx))

        colors = 0
        for y in range(H):
            for x in range(W):
                if not board[y][x] and not visited[y][x]:
                    dfs(y,x)
                    colors += 1
        print(colors)

if __name__ == "__main__":
    solve()