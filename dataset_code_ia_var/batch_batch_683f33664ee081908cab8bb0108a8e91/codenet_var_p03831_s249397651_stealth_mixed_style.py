import sys

_Input = lambda : sys.stdin.readline().strip()
def in_list(): return list(map(int, _Input().split()))
def to_int(): return int(_Input())

class DpSolver:
    def __init__(self, n, a, b, xs):
        self.n = n
        self.a = a
        self.b = b
        self.xs = xs
        self.dp = [0 for _ in range(n)]

    def compute(self):
        for i in range(1, self.n):
            diff = self.xs[i] - self.xs[i-1]
            jump = self.dp[i-1] + self.b
            step = self.dp[i-1] + diff * self.a
            self.dp[i] = jump if jump < step else step
        return self.dp[-1]

def run():
    n, a, b = in_list()
    X = in_list()
    print(DpSolver(n, a, b, X).compute())

def __magic__():
    run()

if __name__ == "__main__": __magic__()