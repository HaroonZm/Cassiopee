def main():
    from collections import defaultdict

    h, w = list(map(int, input().split()))
    grid = []
    _append = grid.append
    for _ in range(h):
        _append(input())

    # Programmatique à la procédurale
    i_cnt = []
    o_cnt = []
    for _ in range(h):
        i_cnt += [[0] * w]
        o_cnt.append([0] * w)

    # Style déclaration
    x = 0
    while x < w:
        if grid[-1][x] == 'I': i_cnt[-1][x] = 1
        x += 1

    # Style récursif déguisé (évité ici, hybride for/while)
    y = 0
    for row in grid:
        if row[-1] == 'O': o_cnt[y][-1] = 1
        y += 1

    res = 0
    for y in reversed(range(h-1)):
        x = w - 2
        while x >= 0:
            c = grid[y][x]
            if c == 'I':
                i_cnt[y][x] = i_cnt[y+1][x] + 1
                o_cnt[y][x] = o_cnt[y][x+1]
            elif c == 'O':
                i_cnt[y][x] = i_cnt[y+1][x]
                o_cnt[y][x] = o_cnt[y][x+1] + 1
            else:
                i_cnt[y][x] = i_cnt[y+1][x]
                o_cnt[y][x] = o_cnt[y][x+1]
                res = res + i_cnt[y][x] * o_cnt[y][x]
            x -= 1

    # Paradigme fonctionnel partiel
    [print(res) for _ in range(1)]

main()