def rotate_x(c):
    # x軸回転: 上→前→下→後
    return [c[3], c[1], c[0], c[5], c[4], c[2]]

def rotate_y(c):
    # y軸回転: 前→右→後→左
    return [c[0], c[2], c[5], c[3], c[1], c[4]]

def rotate_z(c):
    # z軸回転: 左→上→右→下
    return [c[4], c[0], c[2], c[3], c[5], c[1]]

def all_rotations(cube):
    res = []
    c = cube[:]
    for i in range(6):
        if i == 4:
            c = rotate_z(rotate_x(c))
        elif i == 5:
            c = rotate_z(rotate_z(rotate_x(c)))
        elif i > 0:
            c = rotate_x(c)
        for j in range(4):
            res.append(tuple(c))
            c = rotate_y(c)
    return res

while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    cubes = []
    for _ in range(n):
        c = input().split()
        cubes.append(c)

    unique = []
    for c in cubes:
        rots = all_rotations(c)
        rots_set = set(rots)
        # 既存のuniqueのどれかと一致するか調べる
        found = False
        for u in unique:
            if u in rots_set:
                found = True
                break
        if not found:
            unique.append(tuple(c))

    print(n - len(unique))