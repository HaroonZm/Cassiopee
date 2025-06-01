direction = [["R",1,0], ["U",0,-1], ["L",-1,0], ["D",0,1]]
walls = []
moves = [0]

for i in range(9):
    line = input()
    walls.append(line)

def is_wall(x1, y1, x2, y2):
    if x1 < 0 or x1 > 4 or y1 < 0 or y1 > 4:
        return False
    if x2 < 0 or x2 > 4 or y2 < 0 or y2 > 4:
        return False
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        if y2 - y1 != 1:
            return False
        return walls[y1*2 + 1][x1] == "1"
    if y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        if x2 - x1 != 1:
            return False
        return walls[y1*2][x1] == "1"
    return False

def nextmove(x, y):
    lastmove = moves[-1]
    if lastmove == 3:
        lastmove = -1
    if lastmove < -1:
        lastmove += 4

    # Try turn right
    right = lastmove + 1
    dx = direction[right][1]
    dy = direction[right][2]
    if is_wall(x, y, x + dx, y + dy):
        return right, x + dx, y + dy

    # Go straight
    dx = direction[lastmove][1]
    dy = direction[lastmove][2]
    if is_wall(x, y, x + dx, y + dy):
        return lastmove, x + dx, y + dy

    # Turn left
    left = lastmove - 1
    dx = direction[left][1]
    dy = direction[left][2]
    if is_wall(x, y, x + dx, y + dy):
        return left, x + dx, y + dy

    # Turn back
    back = lastmove - 2
    dx = direction[back][1]
    dy = direction[back][2]
    if is_wall(x, y, x + dx, y + dy):
        return back, x + dx, y + dy

lastx = 1
lasty = 0
print("R", end="")

while True:
    move, lastx, lasty = nextmove(lastx, lasty)
    moves.append(move)
    print(direction[move][0], end="")
    if lastx == 0 and lasty == 0:
        break
print()