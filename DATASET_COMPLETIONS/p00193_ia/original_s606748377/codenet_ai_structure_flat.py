D = (((-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)),
     ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)))
while True:
    try:
        data = raw_input()
        if data == "0":
            break
        m, n = map(int, data.split())
        s = input()
        spos = []
        for _ in xrange(s):
            pos = map(int, raw_input().split())
            spos.append(pos)
        t = input()
        tpos = []
        for _ in xrange(t):
            pos = map(int, raw_input().split())
            tpos.append(pos)
        scover = []
        for pos in spos:
            y, x = pos[1] - 1, pos[0] - 1
            q = [(y, x, 0)]
            cover = [[-1] * m for _ in xrange(n)]
            while len(q) != 0:
                cy, cx, step = q.pop(0)
                if cover[cy][cx] >= 0:
                    continue
                cover[cy][cx] = step
                for dx, dy in D[cy % 2]:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        q.append((ny, nx, step + 1))
            scover.append(cover)
        min_cover = []
        for y in xrange(n):
            row = []
            for x in xrange(m):
                min_val = scover[0][y][x]
                for sc in scover[1:]:
                    if sc[y][x] < min_val:
                        min_val = sc[y][x]
                row.append(min_val)
            min_cover.append(row)
        max_count = 0
        for pos in tpos:
            y, x = pos[1] - 1, pos[0] - 1
            q = [(y, x, 0)]
            cover = [[-1] * m for _ in xrange(n)]
            while len(q) != 0:
                cy, cx, step = q.pop(0)
                if cover[cy][cx] >= 0:
                    continue
                cover[cy][cx] = step
                for dx, dy in D[cy % 2]:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        q.append((ny, nx, step + 1))
            count = 0
            for y2 in xrange(n):
                for x2 in xrange(m):
                    if cover[y2][x2] < min_cover[y2][x2]:
                        count += 1
            if count > max_count:
                max_count = count
        print max_count
    except:
        break