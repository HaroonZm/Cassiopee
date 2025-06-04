N = int(input())
plane = [0] * N
houkou = ["U", "D", "R", "L"]
for i in range(N):
    x, y, p = list(map(str, input().split()))
    x = int(x)
    y = int(y)
    p2 = houkou.index(p)
    plane[i] = [x, y, x + y, x - y, p2]

time = 10 ** 10

# x座標が同じでぶつかる
plane.sort(key=lambda x: x[1])
plane.sort(key=lambda x: x[0])
for k in range(1, N):
    if plane[k][0] == plane[k - 1][0]:
        if plane[k][1] > plane[k - 1][1]:
            if (plane[k][4] == 1) and (plane[k - 1][4] == 0):
                time2 = (plane[k][1] - plane[k - 1][1]) / 0.2
                time = min(time, time2)
        else:
            if (plane[k][4] == 0) and (plane[k - 1][4] == 1):
                time2 = (plane[k - 1][1] - plane[k][1]) / 0.2
                time = min(time, time2)

# y座標が同じでぶつかる
plane.sort(key=lambda x: x[0])
plane.sort(key=lambda x: x[1])
for k in range(1, N):
    if plane[k][1] == plane[k - 1][1]:
        if plane[k][0] > plane[k - 1][0]:
            if (plane[k][4] == 3) and (plane[k - 1][4] == 2):
                time2 = (plane[k][0] - plane[k - 1][0]) / 0.2
                time = min(time, time2)
        else:
            if (plane[k][4] == 2) and (plane[k - 1][4] == 3):
                time2 = (plane[k - 1][0] - plane[k][0]) / 0.2
                time = min(time, time2)

# 和が同じでぶつかる
plane.sort(key=lambda x: x[2])
for k in range(1, N):
    one = plane[k]
    two = plane[k - 1]
    if one[2] == two[2]:
        time2 = abs(one[0] - two[0]) / 0.1
        max_x = max(one[0], two[0])
        min_x = min(one[0], two[0])
        max_y = max(one[1], two[1])
        min_y = min(one[1], two[1])
        L = [[max_x, max_y], [min_x, min_y]]
        # go() inline
        if one[4] == 0:
            k_x, k_y = one[0], int(one[1] + time2 * 0.1)
        elif one[4] == 1:
            k_x, k_y = one[0], int(one[1] - time2 * 0.1)
        elif one[4] == 2:
            k_x, k_y = int(one[0] + time2 * 0.1), one[1]
        else:
            k_x, k_y = int(one[0] - time2 * 0.1), one[1]
        if two[4] == 0:
            k2_x, k2_y = two[0], int(two[1] + time2 * 0.1)
        elif two[4] == 1:
            k2_x, k2_y = two[0], int(two[1] - time2 * 0.1)
        elif two[4] == 2:
            k2_x, k2_y = int(two[0] + time2 * 0.1), two[1]
        else:
            k2_x, k2_y = int(two[0] - time2 * 0.1), two[1]
        if [k_x, k_y] in L and [k2_x, k2_y] in L and [k_x, k_y] == [k2_x, k2_y]:
            time = min(time, time2)

# 差が同じでぶつかる
plane.sort(key=lambda x: x[3])
for k in range(1, N):
    one = plane[k]
    two = plane[k - 1]
    if one[3] == two[3]:
        time2 = abs(one[0] - two[0]) / 0.1
        max_x = max(one[0], two[0])
        min_x = min(one[0], two[0])
        max_y = max(one[1], two[1])
        min_y = min(one[1], two[1])
        L = [[max_x, min_y], [min_x, max_y]]
        if one[4] == 0:
            k_x, k_y = one[0], int(one[1] + time2 * 0.1)
        elif one[4] == 1:
            k_x, k_y = one[0], int(one[1] - time2 * 0.1)
        elif one[4] == 2:
            k_x, k_y = int(one[0] + time2 * 0.1), one[1]
        else:
            k_x, k_y = int(one[0] - time2 * 0.1), one[1]
        if two[4] == 0:
            k2_x, k2_y = two[0], int(two[1] + time2 * 0.1)
        elif two[4] == 1:
            k2_x, k2_y = two[0], int(two[1] - time2 * 0.1)
        elif two[4] == 2:
            k2_x, k2_y = int(two[0] + time2 * 0.1), two[1]
        else:
            k2_x, k2_y = int(two[0] - time2 * 0.1), two[1]
        if [k_x, k_y] in L and [k2_x, k2_y] in L and [k_x, k_y] == [k2_x, k2_y]:
            time = min(time, time2)

if time == 10 ** 10:
    print("SAFE")
else:
    print(int(time))