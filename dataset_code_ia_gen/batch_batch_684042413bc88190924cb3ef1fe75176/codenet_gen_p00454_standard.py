import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        n = int(input())
        xs = {0,w}
        ys = {0,h}
        rects = []
        for _ in range(n):
            x1,y1,x2,y2 = map(int,input().split())
            rects.append((x1,y1,x2,y2))
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)
        xs = sorted(xs)
        ys = sorted(ys)
        x_id = {x:i for i,x in enumerate(xs)}
        y_id = {y:i for i,y in enumerate(ys)}
        W = len(xs)-1
        H = len(ys)-1
        board = [[False]*W for _ in range(H)]
        for x1,y1,x2,y2 in rects:
            for yi in range(y_id[y1], y_id[y2]):
                for xi in range(x_id[x1], x_id[x2]):
                    board[yi][xi] = True
        visited = [[False]*W for _ in range(H)]
        def neighbors(r,c):
            for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=nr<H and 0<=nc<W:
                    yield nr,nc
        def dfs(r,c):
            stack = [(r,c)]
            visited[r][c] = True
            while stack:
                cr,cc = stack.pop()
                for nr,nc in neighbors(cr,cc):
                    if not visited[nr][nc] and not board[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr,nc))
        count = 0
        for r in range(H):
            for c in range(W):
                if not board[r][c] and not visited[r][c]:
                    count +=1
                    dfs(r,c)
        print(count)
if __name__=="__main__":
    main()