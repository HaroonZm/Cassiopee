h, w = map(int, raw_input().split())
grid = [raw_input() for r in range(h)]
result = True
for r in range(h):
    for c in range(w):
        if grid[r][c] == '#':
            cnt = 0
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < h) and (0 <= nc < w) and (grid[nr][nc] == '#'):
                    cnt += 1
            if cnt == 0:
                result = False
if result:
    print "Yes"
else:
    print "No"