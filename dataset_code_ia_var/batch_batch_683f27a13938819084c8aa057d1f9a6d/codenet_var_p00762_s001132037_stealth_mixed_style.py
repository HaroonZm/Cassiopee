class RollDir(object):
    def __init__(self, d, w):
        self.d = d; self.w = w

    def __repr__(self): return f'Roll dir: {self.d}, weight: {self.w}'

    @staticmethod
    def create(d, w):
        # style: mixing static/classic
        return (RollDir(d, w) if w in (6,5,4) else None)

class Dice:
    # prototypal + attribute dict style
    def __init__(self, t, f):
        setattr(self, 'top', t)
        self.bot = 7-t
        # imperative, multi-style traversal
        seq = {1:[2,3,5,4], 6:[5,3,2,4], 2:[3,1,4,6], 5:[3,6,4,1],
               3:[6,5,1,2], 4:[1,5,6,2]}
        arr = seq[t]
        # functional + classic
        idx = (lambda a, v: a.index(v))(arr, f)
        for prop,val in zip(('front','right','back','left'), [arr[i%4] for i in range(idx, idx+4)]):
            setattr(self, prop, val)

    def roll(self, dir):
        # procedural + duck
        t = self.top
        if dir=='N':
            self.top, self.front, self.bot, self.back = self.front, self.bot, self.back, t
        elif dir=='E':
            self.top, self.left, self.bot, self.right = self.left, self.bot, self.right, t
        elif dir=='W':
            (self.top, self.right, self.bot, self.left) = (self.right, self.bot, self.left, t)
        elif dir=='S':
            tmp = self.top; self.top = self.back; self.back = self.bot; self.bot = self.front; self.front = tmp

    def getRollDir(self):
        lst = []
        for d,v in zip(('S','E','N','W'), (self.front,self.right,self.back,self.left)):
            res = RollDir.create(d,v)
            if res is not None: lst.append(res)
        return sorted(lst, key=lambda x: -x.w)

    def __str__(self):
        return "Top:{}|Front:{}|Left:{}|Right:{}".format(self.top, self.front, self.left, self.right)

class Cell:
    # minimalism + OOP
    height = 0
    def __init__(self): self.val=None

class Grid(object):
    def __init__(self): self.cells={}

    def drop(self, dice, x, y):
        key = (x,y)
        if key not in self.cells:
            self.cells[key]=Cell()
        cell=self.cells[key]
        didRoll=False
        for roll in dice.getRollDir():
            if roll.d in self.getRollableDir(x,y):
                dice.roll(roll.d)
                nx,ny = self.getRollCoord(x,y,roll.d)
                self.drop(dice, nx, ny)
                didRoll=True
                break
        if not didRoll:
            cell.height+=1; cell.val=dice.top

    def getRollableDir(self, x, y):
        def getcell(z,t):
            if (z,t) not in self.cells:
                self.cells[(z,t)]=Cell(); self.cells[(z,t)].height=0
            return self.cells[(z,t)]
        cell = getcell(x,y)
        if cell.height==0:
            return []
        arr = []
        dirs=[('N',(x-1,y)),('E',(x,y+1)),('W',(x,y-1)),('S',(x+1,y))]
        for k, (a,b) in dirs:
            ncell = self.cells.get((a,b))
            if ncell is None or ncell.height < cell.height:
                arr.append(k)
        return arr

    def getRollCoord(self, x, y, d):
        o = {'N': (-1,0), 'E': (0,1), 'W': (0,-1), 'S': (1,0)}
        dx,dy = o[d]
        return x+dx,y+dy

    def countVals(self):
        c=[0]*6
        for k in self.cells:
            v = self.cells[k].val
            c[v-1] += 1
        return c

def main():
    import sys
    while 1:
        N = int(sys.stdin.readline())
        if not N: break
        grid = Grid()
        for __ in range(N):
            t,f = (int(x) for x in filter(None, sys.stdin.readline().split(' ')))
            dice = Dice(t,f)
            grid.drop(dice, 0, 0)
        print(*grid.countVals())

if __name__=='__main__': main()