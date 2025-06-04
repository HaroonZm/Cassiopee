MOD = 10**9 + 7

class ModularArithmetic:
    def __init__(self, modulus):
        self.mod = modulus
    
    def add(self, a, b):
        return (a + b) % self.mod
    
    def sub(self, a, b):
        return (a - b) % self.mod
    
    def mul(self, a, b):
        return (a * b) % self.mod
    
    def pow(self, base, exponent):
        result = 1
        cur = base % self.mod
        e = exponent
        while e > 0:
            if e & 1:
                result = (result * cur) % self.mod
            cur = (cur * cur) % self.mod
            e >>= 1
        return result
    
    def inv(self, a):
        # Fermat's little theorem
        return self.pow(a, self.mod - 2)
    
class StirlingSecondKindCalculator:
    """
    Calculates Stirling numbers of the second kind S(n, k),
    the number of ways to partition a set of n distinguishable objects
    into k indistinguishable non-empty subsets.
    """
    def __init__(self, max_n, modulus_arithmetic):
        self.max_n = max_n
        self.mod_arith = modulus_arithmetic
        self.s_table = [[0]*(max_n+1) for _ in range(max_n+1)]
        self._precompute()
    
    def _precompute(self):
        # Base cases
        self.s_table[0][0] = 1
        for n in range(1, self.max_n+1):
            for k in range(1, n+1):
                addend1 = self.s_table[n-1][k-1]
                addend2 = self.mod_arith.mul(k, self.s_table[n-1][k])
                self.s_table[n][k] = self.mod_arith.add(addend1, addend2)
    
    def get(self, n, k):
        if k > n or k < 0:
            return 0
        return self.s_table[n][k]

class BallsAndBoxesSolver:
    """
    Solves the problem of distributing n distinguishable balls into k indistinguishable boxes,
    with each box non-empty.
    Uses Stirling numbers of the second kind directly.
    """
    def __init__(self, modulus=10**9+7):
        self.mod_arith = ModularArithmetic(modulus)
        self.max_n = 1000  # constraint given
        self.stirling_calculator = StirlingSecondKindCalculator(self.max_n, self.mod_arith)
    
    def solve(self, n, k):
        """
        Returns the count of ways to put n distinguishable balls into k indistinguishable boxes
        with no empty boxes, modulo MOD.
        This is simply S(n,k).
        """
        return self.stirling_calculator.get(n, k)

class InputOutputHandler:
    """
    Abstraction for input reading and output printing.
    Can be extended for other IO specifics or testing harnesses.
    """
    def __init__(self):
        pass
    
    def read_parameters(self):
        raw_input = input()
        n_str, k_str = raw_input.strip().split()
        return int(n_str), int(k_str)
    
    def print_result(self, result):
        print(result)

def main():
    io_handler = InputOutputHandler()
    solver = BallsAndBoxesSolver()
    n, k = io_handler.read_parameters()
    result = solver.solve(n, k)
    io_handler.print_result(result)

if __name__ == "__main__":
    main()