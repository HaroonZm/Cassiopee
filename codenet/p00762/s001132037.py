class RollDir:
    def __init__(self, d, w):
        self.d = d
        self.w = w

    def __str__(self):
        return "Roll dir: {}, weight: {}".format(self.d, self.w)

    @classmethod
    def create(cls, d, w):
        if w == 6 or w == 5 or w == 4:
            return cls(d, w)
        else:
            return None

class Dice:
    def __init__(self, t, f):
        self.top = t
        self.bot = 7 - t

        if t == 1:
            arr = [2, 3, 5, 4]
        elif t == 6:
            arr = [5, 3, 2, 4]
        elif t == 2:
            arr = [3, 1, 4, 6]
        elif t == 5:
            arr = [3, 6, 4, 1]
        elif t == 3:
            arr = [6, 5, 1, 2]
        elif t == 4:
            arr = [1, 5, 6, 2]

        idx = arr.index(f)
        self.front = arr[idx]
        self.right = arr[(idx + 1) % 4]
        self.back = arr[(idx + 2) % 4]
        self.left = arr[(idx + 3) % 4]

    def roll(self, direction):
        if direction == 'N':
            temp = self.top
            self.top = self.front
            self.front = self.bot
            self.bot = self.back
            self.back = temp
        elif direction == 'E':
            temp = self.top
            self.top = self.left
            self.left = self.bot
            self.bot = self.right
            self.right = temp
        elif direction == 'W':
            temp = self.top
            self.top = self.right
            self.right = self.bot
            self.bot = self.left
            self.left = temp
        elif direction == 'S':
            temp = self.top
            self.top = self.back
            self.back = self.bot
            self.bot = self.front
            self.front = temp

    def getRollDir(self):
        arr = []
        roll = RollDir.create('S', self.front)
        if roll != None:
            arr.append(roll)
        roll = RollDir.create('E', self.right)
        if roll != None:
            arr.append(roll)
        roll = RollDir.create('N', self.back)
        if roll != None:
            arr.append(roll)
        roll = RollDir.create('W', self.left)
        if roll != None:
            arr.append(roll)

        return sorted(arr, key=lambda x: x.w ,reverse=True)
        
    def __str__(self):
        return "Top: {}   Front: {}   Left: {}   Right: {}" \
            .format(self.top, self.front, self.left, self.right)

class Cell:
    def __init__(self):
        self.height = 0
        self.val = None

class Grid:
    def __init__(self):
        self.cells = {}

    def drop(self, dice, x, y):
        if (x, y) not in self.cells:
            self.cells[ (x, y) ] = Cell()
        cell = self.cells[ (x, y) ]

        diceRollDirs = dice.getRollDir()
        gridRollDirs = self.getRollableDir(x, y)

        didRoll = False
        for roll in diceRollDirs:
            if roll.d in gridRollDirs:
                direction = roll.d
                dice.roll(direction)
                rollCoord = self.getRollCoord(x, y, direction)
                self.drop(dice, rollCoord[0], rollCoord[1])
                didRoll = True
                break
        
        if not didRoll:
            cell.height += 1
            cell.val = dice.top

    def getRollableDir(self, x, y):
        if (x, y) not in self.cells:
            self.cells[(x, y)] = Cell()
        cell = self.cells[(x, y)]

        arr = []
        if cell.height == 0:
            return []
        if (x-1, y) not in self.cells or self.cells[(x-1, y)].height < cell.height:
            arr.append('N')
        if (x, y+1) not in self.cells or self.cells[(x, y+1)].height < cell.height:
            arr.append('E')
        if (x, y-1) not in self.cells or self.cells[(x, y-1)].height < cell.height:
            arr.append('W')
        if (x+1, y) not in self.cells or self.cells[(x+1, y)].height < cell.height:
            arr.append('S')
        return arr

    def getRollCoord(self, x, y, d):
        if d == 'N':
            return (x-1, y)
        elif d == 'E':
            return (x, y+1)
        elif d == 'W':
            return (x, y-1)
        elif d == 'S':
            return (x+1, y)

    def countVals(self):
        count = [0, 0, 0, 0, 0, 0]
        for coord in self.cells:
            cell = self.cells[coord]
            count[ cell.val - 1 ] += 1
        return count

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break

        grid = Grid()
        for _ in range(N):
            t, f = [ int(x) for x in list(filter(lambda x: x != '', \
                input().strip().split(' '))) ]
            dice = Dice(t, f)
            grid.drop(dice, 0, 0)

        print(" ".join(list(map(str, grid.countVals()))))