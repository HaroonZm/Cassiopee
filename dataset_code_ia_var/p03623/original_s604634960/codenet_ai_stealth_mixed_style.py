def check_nearest(x, a, b):
    return "A" if abs(a - x) < abs(b - x) else ("B" if abs(b - x) < abs(a - x) else None)

class Solver:
    def __init__(self):
        vals = input().split()
        self.x = int(vals[0])
        self.a = int(vals[1])
        self.b = int(vals[2])

    def solve(self):
        res = check_nearest(self.x, self.a, self.b)
        if res is not None:
            print(res)
        else:
            pass  # ne rien faire ici

if __name__=='__main__':
    s = Solver()
    s.solve()