class Dice:
    def __init__(self, p):
        self.y = [p[0], p[1], p[5], p[4]]
        self.x = [p[0], p[2], p[5], p[3]]
        self.z = [p[1], p[2], p[4], p[3]]
    def roll(self, c):
        if c == 'y':
            self.y.append(self.y.pop(0))
            self.x[0] = self.y[0]
            self.x[2] = self.y[2]
            self.z[0] = self.y[1]
            self.z[2] = self.y[3]
        elif c == 'x':
            self.x.append(self.x.pop(0))
            self.y[0] = self.x[0]
            self.y[2] = self.x[2]
            self.z[1] = self.x[1]
            self.z[3] = self.x[3]
        elif c == 'z':
            self.z.append(self.z.pop(0))
            self.x[1] = self.z[1]
            self.x[3] = self.z[3]
            self.y[1] = self.z[0]
            self.y[3] = self.z[2]
    def num(self, n):
        n = n - 1;
        pos_y = [0, 1, 5, 4]
        pos_x = [0, 2, 5, 3]
        if n in pos_y:
            return self.y[pos_y.index(n)]
        else:
            return self.x[pos_x.index(n)]
    def same(self, other):
        for _ in range(4):
            if self == other:
                return True
            other.roll('x')
            for _ in range(4):
                if self == other:
                    return True
                other.roll('y')
                for _ in range(4):
                    if self == other:
                        return True
                    other.roll('z')
        return False
    def __eq__(self, other):
        for i in range(1,7):
            if (self.num(i) != other.num(i)):
                return False
        return True

n = int(input())
dices = []
for _ in range(n):
    dices.append(Dice([int(i) for i in input().split()]))

yes = all([not dices[0].same(other) for other in dices[1:]])
print('Yes' if yes else 'No')