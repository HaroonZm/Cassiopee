def is_wall(x1,y1,x2,y2):
    if x1<0 or 4<x1 or y1<0 or 4<y1 or x2<0 or 4<x2 or y2<0 or 4<y2:
        return False
    elif x1 == x2:
        if y1>y2: y1,y2 = y2,y1
        if y2-y1 != 1: return False
        return (walls[y1*2+1][x1] == "1")
    elif y1 == y2:
        if x1>x2: x1,x2 = x2,x1
        if x2-x1 != 1: return False
        return (walls[y1*2][x1] == "1")
    else: return False

def nextmove(x,y):
    lastmove = moves[-1]
    if lastmove == 3: lastmove = -1
    if lastmove < -1: lastmove += 4
    if is_wall(x,y,x+direction[lastmove+1][1],y+direction[lastmove+1][2]):
        return lastmove+1,x+direction[lastmove+1][1],y+direction[lastmove+1][2]

    if is_wall(x,y,x+direction[lastmove][1],y+direction[lastmove][2]):
        return lastmove,x+direction[lastmove][1],y+direction[lastmove][2]

    if is_wall(x,y,x+direction[lastmove-1][1],y+direction[lastmove-1][2]):
        return lastmove-1,x+direction[lastmove-1][1],y+direction[lastmove-1][2]

    if is_wall(x,y,x+direction[lastmove-2][1],y+direction[lastmove-2][2]):
        return lastmove-2,x+direction[lastmove-2][1],y+direction[lastmove-2][2]

direction = [["R",1,0],["U",0,-1],["L",-1,0],["D",0,1]]
walls = []
moves = [0]
for _ in range(9):
    walls.append(input())
lastx = 1
lasty = 0
print("R", end = "")
while True:
    move,lastx,lasty = nextmove(lastx, lasty)
    moves.append(move)
    print(direction[move][0], end = "")
    if lastx == 0 and lasty == 0: break
print()