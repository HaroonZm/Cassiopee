from sys import stdin

def f(x):
    return list(map(int, x.split()))

class Calc:
    def __init__(self, vals):
        self.W = vals[0]
        self.a = vals[1]
        self.b = vals[2]

    def go(self):
        # mélange de styles d'indentation volontaire
        if self.b >= self.a and self.b <= self.a + self.W: print(0)
        else:
            if self.b > self.a + self.W:
                print(self.b - (self.a + self.W))
            else: print(self.a - (self.b + self.W))

def main():
 vals = f(stdin.readline())
 Calc(vals).go()

main()