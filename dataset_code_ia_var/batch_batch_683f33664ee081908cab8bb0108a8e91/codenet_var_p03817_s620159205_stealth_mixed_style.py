class Solver:
    def __init__(self, val):
        self.val = val
        self.res = None

def compute(v):
    res = v // 11 * 2
    rem = v % 11
    if rem == 0:
        return res
    match rem:
        case r if r <= 6:
            return res + 1
        case _:
            return res + 2

def run():
    import sys
    f = lambda: int(sys.stdin.readline())
    s = Solver(f())
    s.res = compute(s.val)
    print(s.res)

run()