while True:
    nums = input().split()
    d = int(nums[0])
    w = int(nums[1])
    if d == 0:
        break

    ans = 0
    e = []
    for i in range(d):
        row = input().split()
        row = [int(x) for x in row]
        e.append(row)

    for si in range(1, d - 1):
        for sj in range(1, w - 1):
            for ti in range(si + 1, d):
                for tj in range(sj + 1, w):
                    mx = 0
                    for i in range(si, ti):
                        for j in range(sj, tj):
                            if e[i][j] > mx:
                                mx = e[i][j]
                    mn = 100
                    # haut et bas du contour
                    for i in [si - 1, ti]:
                        for j in range(sj - 1, tj + 1):
                            if e[i][j] < mn:
                                mn = e[i][j]
                    # gauche et droite du contour
                    for i in range(si - 1, ti + 1):
                        for j in [sj - 1, tj]:
                            if e[i][j] < mn:
                                mn = e[i][j]
                    if mx >= mn:
                        continue
                    tmp = 0
                    for i in range(si, ti):
                        for j in range(sj, tj):
                            tmp += mn - e[i][j]
                    if tmp > ans:
                        ans = tmp
    print(ans)