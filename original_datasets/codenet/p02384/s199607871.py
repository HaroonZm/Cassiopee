class Dice:
    NS = [1, 5, 6, 2]
    EW = [1, 3, 6, 4]

    def question(self, top, front):
        self.setTop(top)
        sides = [self.NS[1], self.EW[1], self.NS[3], self.EW[3]]
        return sides[(sides.index(front) + 3) % 4]

    def setTop(self, n):
        if n in self.NS:
            while self.NS[0] != n:
                self.N()
        else:
            while self.NS[0] != n:
                self.E()

    def N(self):
        tail = self.NS.pop()
        self.NS.insert(0, tail)
        self.EW[0] = self.NS[0]
        self.EW[2] = self.NS[2]

    def E(self):
        tail = self.EW.pop()
        self.EW.insert(0, tail)
        self.NS[0] = self.EW[0]
        self.NS[2] = self.EW[2]

if __name__ == '__main__':
    dnum = input().split()
    for _ in range(int(input())):
        t, f = input().split()
        r = Dice().question(dnum.index(t) + 1, dnum.index(f) + 1)
        print(dnum[r - 1])