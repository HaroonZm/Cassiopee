D = [
    [(-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)],
    [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]
]

def func(y, x):
    q = [(y, x, 0)]
    cover = []
    for _ in range(n):
        cover.append([-1] * m)
    while q:
        yx_step = q.pop(0)
        y, x, step = yx_step
        if cover[y][x] != -1:
            continue
        cover[y][x] = step
        for dx, dy in D[y % 2]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                q.append((ny, nx, step + 1))
    return cover

def solve():
    scover = list(map(lambda pos: func(pos[1]-1, pos[0]-1), spos))
    min_cover = []
    for y in range(n):
        row = []
        for x in range(m):
            row.append(min(sc[y][x] for sc in scover))
        min_cover.append(row)

    def count(cover):
        ret = 0
        for y, row in enumerate(cover):
            for x in range(len(row)):
                if cover[y][x] < min_cover[y][x]:
                    ret += 1
        return ret

    return max(map(lambda pos: count(func(pos[1]-1, pos[0]-1)), tpos))

while True:
    try:
        data = input()
        if data == "0":
            break
        m, n = map(int, data.split())
        s = int(input())
        spos = []
        for _ in range(s):
            spos.append(list(map(int, input().split())))
        t = int(input())
        tpos = []
        for i in range(t):
            tpos.append(list(map(int, input().split())))
        print(solve())
    except Exception:
        break