import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        
        rects = []
        xs = set()
        ys = set()
        for _ in range(n):
            l,t,r,b = map(int, input().split())
            # note: input gives top-left (l,t), bottom-right (r,b) with b < t
            rects.append((l,t,r,b))
            xs.add(l)
            xs.add(r)
            ys.add(t)
            ys.add(b)
        
        xs = sorted(xs)
        ys = sorted(ys)

        # coordinate compression mapping coordinate to index
        x_id = {x:i for i,x in enumerate(xs)}
        y_id = {y:i for i,y in enumerate(ys)}

        w = len(xs)
        h = len(ys)

        # mark grid cells covered by any rectangle
        # cells correspond to intervals between coordinates
        covered = [[False]*(h-1) for _ in range(w-1)]
        for (l,t,r,b) in rects:
            x_start = x_id[l]
            x_end = x_id[r]
            y_start = y_id[b]
            y_end = y_id[t]
            for i in range(x_start, x_end):
                for j in range(y_start, y_end):
                    covered[i][j] = True

        # use flood fill to find number of regions not enclosed by rectangles
        visited = [[False]*(h-1) for _ in range(w-1)]

        def neighbors(x,y):
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w-1 and 0 <= ny < h-1:
                    yield nx, ny

        def dfs(sx, sy):
            stack = [(sx,sy)]
            visited[sx][sy] = True
            while stack:
                x,y = stack.pop()
                for nx,ny in neighbors(x,y):
                    if not visited[nx][ny] and covered[nx][ny] == covered[x][y]:
                        visited[nx][ny] = True
                        stack.append((nx,ny))

        regions = 0
        for i in range(w-1):
            for j in range(h-1):
                if not visited[i][j]:
                    dfs(i,j)
                    regions += 1

        print(regions)

if __name__=="__main__":
    main()