while True:
    n = int(input())
    if not n:
        break

    star = [list(map(float, input().split())) for i in range(n)]
    start = [0.0, 0.0, 0.0]
    move = 0.5

    for _ in range(500):
        for j in range(100):
            tmpmax = 0
            a = 0
            for i in range(n):
                k = (star[i][0] - start[0]) ** 2 + (star[i][1] - start[1]) ** 2 + (star[i][2] - start[2]) ** 2
                if tmpmax < k:
                    tmpmax = k
                    a = i
            start = [start[i] - (start[i] - star[a][i]) * move for i in range(3)]
        move /= 2

    tmpmax = 0
    for i in range(n):
        k = (star[i][0] - start[0]) ** 2 + (star[i][1] - start[1]) ** 2 + (star[i][2] - start[2]) ** 2
        if tmpmax < k:
            tmpmax = k

    print(round(tmpmax ** 0.5, 5))