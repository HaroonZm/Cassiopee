def solve(sentence):
    now = [0, 0, 0]  # x,y,z
    num_p = {}
    positions = []
    for s in sentence:
        if s.isdecimal():
            if s in num_p:
                now = num_p[s]
            else:
                num_p[s] = now
        else:
            sign = 1 if s[0] == "+" else -1
            if s[1] == "x":
                positions.append([now.copy(), [now[0] + sign, now[1], now[2]]])
                now = [now[0] + sign, now[1], now[2]]
            if s[1] == "y":
                positions.append([now.copy(), [now[0], now[1] + sign, now[2]]])
                now = [now[0], now[1] + sign, now[2]]
            if s[1] == "z":
                positions.append([now.copy(), [now[0], now[1], now[2] + sign]])
                now = [now[0], now[1], now[2] + sign]
    return positions

def rotateX(positions):
    miny = float("inf")
    minz = float("inf")
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][1], positions[i][j][2] = -positions[i][j][2], positions[i][j][1]
            if positions[i][j][1] < miny:
                miny = positions[i][j][1]
            if positions[i][j][2] < minz:
                minz = positions[i][j][2]
    # シフト
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][1] -= miny
            positions[i][j][2] -= minz
        positions[i].sort()
    return positions

def rotateY(positions):
    minx = float("inf")
    minz = float("inf")
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][0], positions[i][j][2] = -positions[i][j][2], positions[i][j][0]
            if positions[i][j][0] < minx:
                minx = positions[i][j][0]
            if positions[i][j][2] < minz:
                minz = positions[i][j][2]
    # シフト
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][0] -= minx
            positions[i][j][2] -= minz
        positions[i].sort()
    return positions

def rotateZ(positions):
    minx = float("inf")
    miny = float("inf")
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][0], positions[i][j][1] = -positions[i][j][1], positions[i][j][0]
            if positions[i][j][0] < minx:
                minx = positions[i][j][0]
            if positions[i][j][1] < miny:
                miny = positions[i][j][1]
    # シフト
    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][0] -= minx
            positions[i][j][1] -= miny
        positions[i].sort()
    return positions

def normal(positions):
    minx = float("inf")
    miny = float("inf")
    minz = float("inf")
    for i in range(len(positions)):
        if positions[i][0][0] < minx:
            minx = positions[i][0][0]
        if positions[i][1][0] < minx:
            minx = positions[i][1][0]

        if positions[i][0][1] < miny:
            miny = positions[i][0][1]
        if positions[i][1][1] < miny:
            miny = positions[i][1][1]

        if positions[i][0][2] < minz:
            minz = positions[i][0][2]
        if positions[i][1][2] < minz:
            minz = positions[i][1][2]

    for i in range(len(positions)):
        for j in range(2):
            positions[i][j][0] -= minx
            positions[i][j][1] -= miny
            positions[i][j][2] -= minz
        positions[i].sort()
    return positions

def check(position1, position2):
    if len(position1) != len(position2):
        return False

    position1.sort()
    position2.sort()
    for i in range(len(position1)):
        if position1[i][0] not in position2[i] or position1[i][1] not in position2[i]:
            return False
    return True

while True:
    string = input()
    if string != "":
        n, *S = string.split()
    else:
        continue
    n = int(n)
    if n == 0:
        break
    while len(S) < n:
        S += input().split()
    position1 = normal(solve(S))

    n, *S = input().split()
    n = int(n)
    while len(S) < n:
        S += input().split()
    position2 = normal(solve(S))

    # 入力ここまで

    end = False
    for z in range(4):
        for y in range(4):
            for x in range(4):
                if check(position1, position2):
                    end = True
                    break
                position2 = rotateX(position2)
            if end:
                break
            position2 = rotateY(position2)
        if end:
            break
        position2 = rotateZ(position2)

    if end:
        print("SAME")
    else:
        print("DIFFERENT")