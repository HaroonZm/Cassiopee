#Deven-Eleven:
D = (((-1, -1), (0, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)),
     ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 0)))
def func(y, x):
    q = [(y, x, 0)]
    cover = [[-1] * m for _ in xrange(n)]
    while len(q) != 0:
        y, x, step = q.pop(0)
        if cover[y][x] >= 0:
            continue
        cover[y][x] = step
        for dx, dy in D[y % 2]:           
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                q.append((ny, nx, step + 1))
    return cover
 
def solve():
    scover = [func(pos[1] - 1, pos[0] - 1) for pos in spos]
    min_cover = [[min(sc[y][x] for sc in scover) for x in xrange(m)] for y in xrange(n)]
    def count(cover):
        ret = 0
        for y in xrange(n):
            for x in xrange(m):
                if cover[y][x] < min_cover[y][x]:
                    ret += 1
        return ret
    return max(count(func(pos[1] - 1, pos[0] - 1)) for pos in tpos)
 
while True:
    try:
        data = raw_input()
        if data == "0":
            break
        m, n = map(int, data.split())
        s = input()
        spos = [map(int, raw_input().split()) for _ in xrange(s)]
        t = input()
        tpos = [map(int, raw_input().split()) for _ in xrange(t)]
        print solve()
    except:
        break