def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

def nuri(table, m, x, y):
    if table[x-1][y] and m[x-1][y] == 0:
        m[x-1][y] = m[x][y]
        nuri(table, m, x-1, y)
    if table[x+1][y] and m[x+1][y] == 0:
        m[x+1][y] = m[x][y]
        nuri(table, m, x+1, y)
    if table[x][y-1] and m[x][y-1] == 0:
        m[x][y-1] = m[x][y]
        nuri(table, m, x, y-1)
    if table[x][y+1] and m[x][y+1] == 0:
        m[x][y+1] = m[x][y]
        nuri(table, m, x, y+1)
    return

N = list(get_input())
for l in range(0,len(N),13):
    table = [[False for i in range(14)] for j in range(14)]
    for i in range(12):
        for j in range(12):
            if int(N[l+i][j]) == 1:
                table[i+1][j+1] = True

    m = [[0 for i in range(14)] for j in range(14)]

    cnt = 0
    for i in range(1,13):
        for j in range(1,13):
            if table[i][j] and m[i][j] == 0:
                cnt += 1
                m[i][j] = cnt
                nuri(table, m, i, j)

    print(cnt)