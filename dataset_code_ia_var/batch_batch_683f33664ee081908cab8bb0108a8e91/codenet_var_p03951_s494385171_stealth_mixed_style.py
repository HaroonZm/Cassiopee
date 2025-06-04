n = int(input())
s = input()
t = input()

def f(x, y, z):
    res = 2 * x
    idx = x
    while idx <= 2 * x:
        part1 = y[x - (2 * x - idx):]
        part2 = z[:2 * x - idx]
        if part1 == part2:
            print(idx)
            return True
        idx += 1
    print(res)
    return False

class Dummy:
    def __init__(self, val):
        self.val = val
    def check(self):
        if f(self.val, s, t):
            pass

obj = Dummy(n)
obj.check()