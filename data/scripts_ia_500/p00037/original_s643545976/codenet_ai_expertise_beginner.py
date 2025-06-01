wall = []
while True:
    try:
        for i in range(9):
            line = raw_input()
            wall.append(line)
    except:
        break

def go(human):
    x = human[0]
    y = human[1]
    d = human[2]
    if d == 0:  # east
        if y*2 - 1 >= 0 and wall[y*2 - 1][x] == '1':
            return 3
        elif x <= 3 and wall[y*2][x] == '1':
            return 0
        elif y*2 + 1 <= 8 and wall[y*2 + 1][x] == '1':
            return 1
        else:
            return 2
    if d == 1:  # south
        if x <= 3 and wall[y*2][x] == '1':
            return 3
        elif y*2 + 1 <= 8 and wall[y*2 + 1][x] == '1':
            return 0
        elif x - 1 >= 0 and wall[y*2][x - 1] == '1':
            return 1
        else:
            return 2
    if d == 2:  # west
        if y*2 + 1 <= 8 and wall[y*2 + 1][x] == '1':
            return 3
        elif x - 1 >= 0 and wall[y*2][x - 1] == '1':
            return 0
        elif y*2 - 1 >= 0 and wall[y*2 - 1][x] == '1':
            return 1
        else:
            return 2
    if d == 3:  # north
        if x - 1 >= 0 and wall[y*2][x - 1] == '1':
            return 3
        elif y*2 - 1 >= 0 and wall[y*2 - 1][x] == '1':
            return 0
        elif x <= 3 and wall[y*2][x] == '1':
            return 1
        else:
            return 2

solve = "R"
human = (1, 0, 0)  # x, y, direction

while human[0] != 0 or human[1] != 0:
    turn = go(human)
    direction = (human[2] + turn) % 4

    if direction == 0:
        human = (human[0] + 1, human[1], direction)
        solve += "R"
    elif direction == 1:
        human = (human[0], human[1] + 1, direction)
        solve += "D"
    elif direction == 2:
        human = (human[0] - 1, human[1], direction)
        solve += "L"
    else:
        human = (human[0], human[1] - 1, direction)
        solve += "U"

print solve