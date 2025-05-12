def get_num(top):  # 転がす番号の候補を決める
    if top == 1:
        return [5, 4]
    elif top == 2:
        return [6, 4]
    elif top == 3:
        return [6, 5]
    elif top == 4:
        return [6, 5]
    elif top == 5:
        return [6, 4]
    elif top == 6:
        return [5, 4]

def get_dir(num, front, top):  # 転がる向きを決める
    if num == front:
        return ["F", num]
    elif num == 7 - front:
        return ["B", num]
    # print(num, front)
    if num == 4:
        if (front == 1 and top == 5) or (front == 5 and top == 6) or (front == 6 and top == 2) or (front == 2 and top == 1):
            return ["L", num]
        elif (front == 5 and top == 1) or (front == 6 and top == 5) or (front == 2 and top == 6) or (front == 1 and top == 2):
            return ["R", num]

    if num == 5:
        if (front == 1 and top == 3) or (front == 3 and top == 6) or (front == 6 and top == 4) or (front == 4 and top == 1):
            return ["L", num]
        elif (front == 3 and top == 1) or (front == 6 and top == 3) or (front == 4 and top == 6) or (front == 1 and top == 4):
            return ["R", num]

    if num == 6:
        if (front == 2 and top == 4) or (front == 4 and top == 5) or (front == 5 and top == 3) or (front == 3 and top == 2):
            return ["L", num]
        elif (front == 4 and top == 2) or (front == 5 and top == 4) or (front == 3 and top == 5) or (front == 2 and top == 3):
            return ["R", num]

def can_roll(dir, nowi, nowj, maps):
    I = 0
    J = 0
    if dir == "F":
        I += 1
    if dir == "B":
        I -= 1
    if dir == "R":
        J += 1
    if dir == "L":
        J -= 1
    if maps[nowi][nowj][0] >= maps[nowi + I][nowj + J][0] + 1:
        return True
    return False

def roll(maps, nowi, nowj, top, front):
    roll_num = get_num(top)
    # print(roll_num, front, top)
    dir1_list = get_dir(roll_num[0], front, top)
    dir2_list = get_dir(roll_num[1], front, top)
    # print(dir1_list, dir2_list)
    dir1 = dir1_list[0]
    dir2 = dir2_list[0]
    # print(dir1, dir2)
    if can_roll(dir1, nowi, nowj, maps):
        # print(nowi, nowj, dir1, 7 - dir1_list[1])
        I = 0
        J = 0
        if dir1 == "F":
            I += 1
            front = top
        if dir1 == "B":
            I -= 1
            front = 7 - top
        if dir1 == "R":
            J += 1
        if dir1 == "L":
            J -= 1
        maps = roll(maps, nowi + I, nowj + J, 7 - dir1_list[1], front)
    elif can_roll(dir2, nowi, nowj, maps):
        # print(nowi, nowj, dir2, 7 - dir2_list[1])
        I = 0
        J = 0
        if dir2 == "F":
            I += 1
            front = top
        if dir2 == "B":
            I -= 1
            front = 7 - top
        if dir2 == "R":
            J += 1
        if dir2 == "L":
            J -= 1
        maps = roll(maps, nowi + I, nowj + J, 7 - dir2_list[1], front)
    else:
        maps[nowi][nowj][0] += 1
        maps[nowi][nowj][1] = top
    return maps

while True:
    n = int(input())
    if not n:
        break

    maps = [[[0, 0] for _ in range(201)] for _ in range(201)]
    nowi = 100
    nowj = 100
    for i in range(n):
        t, f = map(int, input().split())
        maps = roll(maps, nowi, nowj, t, f)
    cnt = [0 for _ in range(6)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j][1]:
                cnt[maps[i][j][1] - 1] += 1
    for i in range(len(cnt)):
        cnt[i] = str(cnt[i])
    # print(maps[100])
    print(" ".join(cnt))