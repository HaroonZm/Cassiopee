from functools import reduce
direction = list(map(lambda t:(t[0],int(t[1]),int(t[2])),[("R","1","0"),("U","0","-1"),("L","-1","0"),("D","0","1")]))
walls = [input() for _ in range(9)]
moves = [0]

def is_wall(x1,y1,x2,y2):
    def valid_range(v): return 0 <= v <= 4
    xor = lambda a,b: (a and not b) or (not a and b)
    if not all(map(valid_range,(x1,y1,x2,y2))): return False
    swapped_x1,swapped_y1,swapped_x2,swapped_y2 = (x1,y1,x2,y2)
    checker = lambda a,b: a == b
    swapped = False
    if checker(x1,x2):
        if y1 > y2:
            swapped_y1,swapped_y2 = y2,y1
            swapped = True
        delta = swapped_y2 - swapped_y1
        if delta != 1: return False
        row = swapped_y1*2+1
        col = x1
        return walls[row][col] == "1"
    elif checker(y1,y2):
        if x1 > x2:
            swapped_x1,swapped_x2 = x2,x1
            swapped = True
        delta = swapped_x2 - swapped_x1
        if delta != 1: return False
        row = y1*2
        col = swapped_x1
        return walls[row][col] == "1"
    else:
        return False

def nextmove(x,y):
    def mod4(v): return (v + 4) % 4
    last = moves[-1]
    last = -1 if last == 3 else last
    last = last if last >= -1 else last + 4
    options = [last + 1, last, last - 1, last - 2]
    for move in options:
        m = mod4(move)
        dx, dy = direction[m][1], direction[m][2]
        nx, ny = x + dx, y + dy
        if is_wall(x,y,nx,ny):
            return m, nx, ny
    # fallback, should never happen if map valid
    return last, x, y

lastx, lasty = 1, 0
print("R", end="")
while True:
    move,lastx,lasty = nextmove(lastx, lasty)
    moves.append(move)
    print(direction[move][0], end="")
    if lastx == 0 and lasty == 0: break
print()