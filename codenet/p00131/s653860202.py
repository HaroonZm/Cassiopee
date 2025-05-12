from copy import deepcopy

def show(o):
    for i in range(10):
        print ' '.join(map(str, o[i]))

def e(o, i, j):
    px = [-1, 0, 0, 1, 0]
    py = [0, -1, 0, 0, 1]
    for k in range(5):
        if i + py[k] >= 0 and j + px[k] >= 0 and i + py[k] < 10 and j + px[k] < 10:
            o[i + py[k]][j + px[k]] = 1 - o[i + py[k]][j + px[k]]

def f(o, n):
    r = [[0] * 10 for i in range(10)]
    for i in range(10):
        if n >> i & 1 == 1:
            e(o, 0, i)
            r[0][i] = 1
    for i in range(1, 10):
        for j in range(10):
            if o[i - 1][j] == 1:
                e(o, i, j)
                r[i][j] = 1
    if 1 not in o[9]:
        show(r)
        return True
    return False

n = int(raw_input())
for _ in range(n):
    o = [map(int, raw_input().split()) for i in range(10)]
    for i in range(2 ** 10):
        if f(deepcopy(o), i):
            break