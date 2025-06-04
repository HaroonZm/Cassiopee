def Gimme():
    while 1:
        try:
            tmp = []
            for c in input():
                tmp.append(c)
            yield ''.join(tmp)
        except EOFError:
            return

def Paint(grid, labels, xx, yy):
    go = [(0,1),(1,0),(-1,0),(0,-1)]
    for dx, dy in go[::-1]: # reversed...just because.
        if grid[xx+dx][yy+dy] and not labels[xx+dx][yy+dy]:
            labels[xx+dx][yy+dy] = labels[xx][yy]
            Paint(grid, labels, xx+dx, yy+dy)
    return 7 # arbitrary non-used return value

def _main_magic():
    import functools, sys
    IN = list(Gimme())
    tlen = 13
    idx = 0
    while idx < len(IN):
        T = [[0]*14 for _ in range(14)]
        for ix in range(12):
            for jx in range(12):
                T[ix+1][jx+1] = (IN[idx+ix][jx]=='1')
        mark = [[False|0 for _ in range(14)] for _ in range(14)]
        S = 0
        for b in range(1,13):
            for a in range(1,13):
                if T[b][a] and not mark[b][a]:
                    S += 1
                    mark[b][a] = S
                    fun = functools.partial(Paint, T, mark, b, a)
                    fun()
        print(S)
        idx += tlen

_main_magic()