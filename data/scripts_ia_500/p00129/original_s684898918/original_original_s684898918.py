class Wall():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def sign(self, x, y):
        if (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y) - self.r*self.r > 0:
            return 1
        else:
            return -1

def isVisible(x1, y1, x2, y2, wall):

    if wall.sign(x1, y1) == 1 and wall.sign(x2, y2) == 1:

        x0 = wall.x
        y0 = wall.y
        r0 = wall.r

        la = y2-y1
        lb = -(x2-x1)
        lc = -x1*(y2-y1) + y1*(x2-x1)

        ma = x2-x1
        mb = y2-y1
        mc = -(x2-x1)*x0 - (y2-y1)*y0

        if (la*x0+lb*y0+lc)*(la*x0+lb*y0+lc) <= r0*r0*(la*la+lb*lb):
            if (ma*x1+mb*y1+mc)*(ma*x2+mb*y2+mc) < 0:
                return False
            else:
                return True
        else:
            return True
    elif wall.sign(x1, y1) == -1 and wall.sign(x2, y2) == -1:
        return True
    else:
        return False

while True:
    n = int(input())
    if n == 0:
        break

    walls = []
    for l in range(n):
        x,y,r = [int(i) for i in input().split()]
        walls.append(Wall(x,y,r))

    m = int(input())
    for l in range(m):
        tx, ty, sx, sy = [int(i) for i in input().split()]
        ans = "Danger"
        for k in range(len(walls)):
            if isVisible(tx, ty, sx, sy, walls[k]) == False:
                #print("Wall", k+1, ": Safe")
                ans = "Safe"
                break
        print(ans)