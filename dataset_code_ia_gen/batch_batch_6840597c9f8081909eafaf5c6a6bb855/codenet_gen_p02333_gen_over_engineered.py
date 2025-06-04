MOD = 10**9 + 7

class ModularArithmetic:
    def __init__(self, mod):
        self.mod = mod
        self.factorials = [1]
        self.inv_factorials = [1]

    def extend_factorials(self, n):
        while len(self.factorials) <= n:
            self.factorials.append((self.factorials[-1] * len(self.factorials)) % self.mod)

        if len(self.inv_factorials) <= n:
            self.inv_factorials += [0] * (n + 1 - len(self.inv_factorials))
            self.inv_factorials[n] = pow(self.factorials[n], self.mod - 2, self.mod)
            for i in range(n - 1, len(self.inv_factorials) - (n + 1), -1):
                self.inv_factorials[i] = (self.inv_factorials[i + 1] * (i + 1)) % self.mod

    def comb(self, n, r):
        if r > n or r < 0:
            return 0
        self.extend_factorials(n)
        return (self.factorials[n] * self.inv_factorials[r] % self.mod) * self.inv_factorials[n - r] % self.mod

class StirlingSecondKind:
    def __init__(self, mod):
        self.mod = mod
        self.memo = {}

    def compute(self, n, k):
        # S(n,k) number of ways to partition n distinguishable elements into k nonempty indistinguishable subsets
        # Use DP with memoization
        if (n, k) in self.memo:
            return self.memo[(n, k)]
        if k == 0 or k > n:
            return 0
        if k == 1 or k == n:
            self.memo[(n, k)] = 1
            return 1
        val = (k * self.compute(n - 1, k) + self.compute(n - 1, k - 1)) % self.mod
        self.memo[(n, k)] = val
        return val

class BallsAndBoxesSolver:
    def __init__(self, n, k, mod=10**9 + 7):
        self.n = n
        self.k = k
        self.mod = mod
        self.modarith = ModularArithmetic(mod)
        self.stirling = StirlingSecondKind(mod)

    def count_ways(self):
        # Problem: place n distinguishable balls into k distinguishable boxes with each box at least one ball
        # Formula: Number of onto functions = k! * S(n,k)
        S_nk = self.stirling.compute(self.n, self.k)
        self.modarith.extend_factorials(self.k)
        fact_k = self.modarith.factorials[self.k]
        return (fact_k * S_nk) % self.mod

class InputParser:
    def __init__(self):
        pass

    def parse(self):
        line = input().strip()
        n, k = map(int, line.split())
        return n, k

class OutputWriter:
    def __init__(self):
        pass

    def write(self, ans):
        print(ans)

class Controller:
    def __init__(self):
        self.parser = InputParser()
        self.writer = OutputWriter()

    def execute(self):
        n, k = self.parser.parse()
        solver = BallsAndBoxesSolver(n, k)
        ans = solver.count_ways()
        self.writer.write(ans)

if __name__ == "__main__":
    controller = Controller()
    controller.execute()