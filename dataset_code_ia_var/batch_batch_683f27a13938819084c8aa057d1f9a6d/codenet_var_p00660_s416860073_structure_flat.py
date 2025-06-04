mp = None

hash_dic = {}
ret = 0
for i, lst in enumerate([
    [8, 18, 22],
    [2, 8, 12, 16, 22],
    [2, 8, 12, 18, 22],
    [6, 8, 12, 18],
    [2, 6, 12, 18, 22],
    [2, 6, 12, 16, 18, 22],
    [2, 8, 18],
    [2, 6, 8, 12, 16, 18, 22],
    [2, 6, 8, 12, 18, 22]
]):
    v = 0
    for j in lst:
        v += 2 ** j
    hash_dic[v] = i + 1

while True:
    s = input()
    if s == "0":
        break
    drawing1, drawing2 = [s[:28]], [s[29:]]
    for _ in range(20):
        s = input()
        drawing1.append(s[:28])
        drawing2.append(s[29:])
    dice1 = []
    # s1
    mp = [list(line[8:13]) for line in drawing1[1:6]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])
    # s2
    mp = [list(line[1:6]) for line in drawing1[8:13]]
    new_mp = [[None] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            new_mp[x][4 - y] = mp[y][x]
    mp = new_mp
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])
    # s3
    mp = [list(line[8:13]) for line in drawing1[8:13]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])
    # s4
    mp = [list(line[15:20]) for line in drawing1[8:13]]
    new_mp = [[None] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            new_mp[4 - x][y] = mp[y][x]
    mp = new_mp
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])
    # s5
    mp = [list(line[22:27]) for line in drawing1[8:13]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])
    # s6
    mp = [list(line[8:13]) for line in drawing1[15:20]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    for y in range(2):
        mp[y], mp[4 - y] = mp[4 - y], mp[y]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice1.append(hash_dic[ret])

    dice2 = []
    # s1
    mp = [list(line[8:13]) for line in drawing2[1:6]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])
    # s2
    mp = [list(line[1:6]) for line in drawing2[8:13]]
    new_mp = [[None] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            new_mp[x][4 - y] = mp[y][x]
    mp = new_mp
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])
    # s3
    mp = [list(line[8:13]) for line in drawing2[8:13]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])
    # s4
    mp = [list(line[15:20]) for line in drawing2[8:13]]
    new_mp = [[None] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            new_mp[4 - x][y] = mp[y][x]
    mp = new_mp
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])
    # s5
    mp = [list(line[22:27]) for line in drawing2[8:13]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])
    # s6
    mp = [list(line[8:13]) for line in drawing2[15:20]]
    for y in range(5):
        mp[y] = mp[y][::-1]
    for y in range(2):
        mp[y], mp[4 - y] = mp[4 - y], mp[y]
    ret = 0
    for y in range(5):
        for x in range(5):
            if mp[y][x] != ".":
                ret += 2 ** (y * 5 + x)
    dice2.append(hash_dic[ret])

    cnt1 = cnt2 = 0
    for num1 in dice1:
        for num2 in dice2:
            if num1 > num2:
                cnt1 += 1
            if num1 < num2:
                cnt2 += 1
    if cnt1 >= cnt2:
        print("HIGH")
    else:
        print("LOW")