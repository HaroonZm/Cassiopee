class ModuloArithmetic:
    def __init__(self, modulus: int):
        self.modulus = modulus

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.modulus

    def sub(self, a: int, b: int) -> int:
        return (a - b) % self.modulus

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.modulus

    def pow(self, base: int, exponent: int) -> int:
        return pow(base, exponent, self.modulus)
    
    def inv(self, a: int) -> int:
        # Fermat's little theorem assuming modulus prime
        return pow(a, self.modulus - 2, self.modulus)

class BeautifulSequenceSolver:
    def __init__(self, n: int, m: int, mod: int = 10**9 + 7):
        self.n = n
        self.m = m
        self.mod = mod
        self.modarith = ModuloArithmetic(mod)

    def count_sequences(self) -> int:
        """
        Counts the number of sequences of length N consisting of 0 and 1
        that contain at least one subsequence of M consecutive 1s.
        The count is done modulo `mod`.
        """
        # Total sequences = 2^N
        total_sequences = self.modarith.pow(2, self.n)

        # Use DP for sequences that do NOT contain M consecutive ones
        # dp[i][j]: number of sequences of length i where the last j bits are consecutive ones (j < M)
        dp = [0] * self.m
        # at i=0, empty sequence with 0 consecutive ones
        dp[0] = 1  

        for i in range(self.n):
            new_dp = [0] * self.m
            # Add '0': resets consecutive ones count
            zero_count = sum(dp) % self.mod
            new_dp[0] = zero_count
            # Add '1': consecutive ones count increases by 1 but cannot reach M
            for j in range(self.m - 1):
                new_dp[j + 1] = dp[j]
            dp = [x % self.mod for x in new_dp]
        
        no_m_conseq_ones = sum(dp) % self.mod

        # beautiful sequences = total_sequences - no_m_conseq_ones
        result = self.modarith.sub(total_sequences, no_m_conseq_ones)
        return result


class InputParser:
    @staticmethod
    def parse() -> tuple[int, int]:
        line = input()
        n_str, m_str = line.strip().split()
        return int(n_str), int(m_str)


class BeautifulSequenceApp:
    def __init__(self, parser_cls=InputParser, solver_cls=BeautifulSequenceSolver):
        self.parser_cls = parser_cls
        self.solver_cls = solver_cls

    def run(self):
        n, m = self.parser_cls.parse()
        solver = self.solver_cls(n, m)
        result = solver.count_sequences()
        print(result)


if __name__ == "__main__":
    app = BeautifulSequenceApp()
    app.run()