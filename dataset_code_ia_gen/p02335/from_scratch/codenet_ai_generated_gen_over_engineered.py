MODULO = 10**9 + 7

class ModuloArithmetic:
    def __init__(self, mod):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod

    def sub(self, a, b):
        return (a - b) % self.mod

    def mul(self, a, b):
        return (a * b) % self.mod

    def pow(self, base, exponent):
        result = 1
        current = base % self.mod
        exp = exponent
        while exp > 0:
            if exp & 1:
                result = (result * current) % self.mod
            current = (current * current) % self.mod
            exp >>= 1
        return result

    def inv(self, a):
        # Fermat's little theorem for mod prime
        return self.pow(a, self.mod - 2)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

class Combinatorics:
    def __init__(self, max_n, mod_arithmetic):
        self.mod = mod_arithmetic
        self.max_n = max_n
        self.fact = [1] * (max_n + 1)
        self.inv_fact = [1] * (max_n + 1)
        self._precompute_factorials()

    def _precompute_factorials(self):
        for i in range(1, self.max_n + 1):
            self.fact[i] = self.mod.mul(self.fact[i-1], i)
        self.inv_fact[self.max_n] = self.mod.inv(self.fact[self.max_n])
        for i in reversed(range(self.max_n)):
            self.inv_fact[i] = self.mod.mul(self.inv_fact[i+1], i+1)

    def nCr(self, n, r):
        if r > n or r < 0:
            return 0
        return self.mod.mul(self.fact[n], self.mod.mul(self.inv_fact[r], self.inv_fact[n-r]))

class BallsAndBoxesSolver:
    """
    Problem abstraction for the 'Balls and Boxes 5' variant:
    - Balls indistinguishable
    - Boxes distinguishable
    - Each box at most one ball
    """
    def __init__(self, n_balls, k_boxes, modulo):
        self.n = n_balls
        self.k = k_boxes
        self.mod = modulo
        self.mod_arith = ModuloArithmetic(modulo)
        self.comb = Combinatorics(max_n=max(n_balls,k_boxes), mod_arithmetic=self.mod_arith)

    def solve(self):
        # Since balls are indistinguishable and boxes distinguishable,
        # and each box can contain at most one ball,
        # the number of ways to place n indistinguishable balls into k distinguishable boxes
        # such that no box has more than one ball = number of ways to select n boxes out of k
        # because balls are identical the arrangement depends only on which boxes are occupied.
        # This is simply C(k, n) if n <= k else 0.
        if self.n > self.k:
            return 0
        return self.comb.nCr(self.k, self.n)

def main():
    import sys
    input_string = sys.stdin.read().strip()
    n_str, k_str = input_string.split()
    n, k = int(n_str), int(k_str)

    solver = BallsAndBoxesSolver(n_balls=n, k_boxes=k, modulo=MODULO)
    answer = solver.solve()
    print(answer)

if __name__ == '__main__':
    main()