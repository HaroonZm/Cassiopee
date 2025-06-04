MOD = 10**9 + 7

class DigitConstraint:
    def __init__(self, char: str, is_first: bool):
        self.char = char
        self.is_first = is_first

    def possible_digits(self):
        if self.char == '?':
            # First digit cannot be zero
            start = 1 if self.is_first else 0
            return range(start, 10)
        else:
            # fixed digit
            d = int(self.char)
            if self.is_first and d == 0:
                # invalid leading zero, but problem states input never starts with zero
                return []
            return [d]

class ArithmeticalRestorationProblem:
    def __init__(self, A: str, B: str, C: str):
        self.A = A
        self.B = B
        self.C = C
        self.length = len(A)
        self.constraints_from_right = []  # will store tuples of DigitConstraint for each digit place (from right)

        # Preprocessing constraints from right to left for easier carry processing
        for i in range(self.length-1, -1, -1):
            is_first = (i == 0)
            dcA = DigitConstraint(A[i], is_first)
            dcB = DigitConstraint(B[i], is_first)
            dcC = DigitConstraint(C[i], is_first)
            self.constraints_from_right.append((dcA, dcB, dcC))

    def count_solutions(self) -> int:
        # DP with memoization
        # State: position (0-based from right), carry (0 or 1)
        # Returns number of ways satisfying constraints
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(pos: int, carry: int) -> int:
            if pos == self.length:
                # All digits processed
                # carry must be zero to be valid
                return 1 if carry == 0 else 0

            dcA, dcB, dcC = self.constraints_from_right[pos]

            total = 0
            for da in dcA.possible_digits():
                for db in dcB.possible_digits():
                    s = da + db + carry
                    dc = s % 10
                    next_carry = s // 10
                    possible_c_digits = dcC.possible_digits()
                    # check if dcC allows this digit
                    if dc in possible_c_digits:
                        total += dfs(pos + 1, next_carry)
            return total % MOD

        return dfs(0, 0)

class InputProcessor:
    def __init__(self):
        self.problems = []

    def read_inputs(self):
        while True:
            A = input().strip()
            if A == '0':
                break
            B = input().strip()
            C = input().strip()
            self.problems.append(ArithmeticalRestorationProblem(A, B, C))

    def solve_and_print_all(self):
        for problem in self.problems:
            print(problem.count_solutions())

def main():
    processor = InputProcessor()
    processor.read_inputs()
    processor.solve_and_print_all()

if __name__ == "__main__":
    main()