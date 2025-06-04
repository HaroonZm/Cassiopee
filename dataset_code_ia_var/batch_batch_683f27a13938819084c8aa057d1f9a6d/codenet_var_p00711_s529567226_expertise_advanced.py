from sys import stdin

def sarch(i, j, visited):
    h, w = len(visited), len(visited[0])
    stack = [(i, j)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while stack:
        ci, cj = stack.pop()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                stack.append((ni, nj))
    return visited

def process():
    anslist = []
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            w_h = next(lines)
            w, h = map(int, w_h.split())
            if w == 0 and h == 0:
                break
            grid = [list(next(lines)) for _ in range(h)]
            visited = [[-1 if cell == '#' else (1 if cell == '@' else 0) for cell in row] for row in grid]
            start = next(((i,j) for i,row in enumerate(grid) for j,cell in enumerate(row) if cell == '@'), None)
            if start:
                sarch(*start, visited)
            ans = sum(cell == 1 for row in visited for cell in row)
            anslist.append(ans)
        except StopIteration:
            break
    print('\n'.join(map(str, anslist)))

if __name__ == "__main__":
    process()