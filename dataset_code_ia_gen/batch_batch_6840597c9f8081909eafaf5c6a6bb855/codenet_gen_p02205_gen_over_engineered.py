class OperationSequence:
    def __init__(self, initial_a: int, initial_b: int):
        self.a = initial_a
        self.b = initial_b

    def apply_odd(self):
        """Applies the odd iteration operation: A = A - B"""
        self.a = self.a - self.b

    def apply_even(self):
        """Applies the even iteration operation: B = A + B"""
        self.b = self.a + self.b

    def apply_operations_naive(self, n: int) -> tuple[int, int]:
        for i in range(1, n + 1):
            if i % 2 == 1:
                self.apply_odd()
            else:
                self.apply_even()
        return self.a, self.b


class LinearTransformation:
    """
    Represents a linear transformation on the vector (A, B):
    After one iteration (odd + even operations pair), (A, B) transforms to M * (A, B),
    where M is a 2x2 matrix.
    """

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix  # 2x2 matrix

    def __matmul__(self, other: "LinearTransformation") -> "LinearTransformation":
        """Matrix multiplication for composing transformations"""
        a, b, c, d = self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1]
        e, f, g, h = other.matrix[0][0], other.matrix[0][1], other.matrix[1][0], other.matrix[1][1]
        result = [
            [a * e + b * g, a * f + b * h],
            [c * e + d * g, c * f + d * h]
        ]
        return LinearTransformation(result)

    def apply(self, vector: tuple[int, int]) -> tuple[int, int]:
        """Apply transformation matrix to a 2D vector"""
        a, b = vector
        m = self.matrix
        return m[0][0] * a + m[0][1] * b, m[1][0] * a + m[1][1] * b

    @staticmethod
    def identity() -> "LinearTransformation":
        return LinearTransformation([[1, 0], [0, 1]])

    def pow(self, exponent: int) -> "LinearTransformation":
        """Computes matrix to the power exponent via fast exponentiation"""
        result = LinearTransformation.identity()
        base = self
        power = exponent
        while power > 0:
            if power & 1:
                result = result @ base
            base = base @ base
            power >>= 1
        return result


class CalculationTraining:
    def __init__(self, n: int, a: int, b: int):
        self.n = n
        self.a = a
        self.b = b

    def compute(self) -> tuple[int, int]:
        """
        Computes the final (A, B) after N operations.

        Observing the pattern:
        N mod 6 cycles the states:
        
        0: (A, B)
        1: (A - B, B)
        2: (A - B, A)
        3: (-B, A)
        4: (-B, A + B)
        5: (A, A + B)
        
        We can represent two steps (odd + even) as a matrix transformation M:
        For i >= 1, after 2 steps:
        (A', B') = M (A, B) with M = [[0, -1], [1, 1]]
        
        If N is even, final = M^(N/2) * (A, B)
        If N is odd, final = (apply odd operation) + M^((N-1)/2) * (A, B)
        """

        M = LinearTransformation([[0, -1], [1, 1]])
        n = self.n
        a, b = self.a, self.b

        if n == 0:
            return a, b

        if n % 2 == 1:
            # After first odd operation: A = A - B, B unchanged
            a_odd = a - b
            b_odd = b
            # Apply M^( (n-1)//2 )
            steps = (n - 1) // 2
            M_pow = M.pow(steps)
            return M_pow.apply((a_odd, b_odd))
        else:
            # n even: apply M^(n/2)
            steps = n // 2
            M_pow = M.pow(steps)
            return M_pow.apply((a, b))


def main():
    import sys

    class InputHandler:
        def __init__(self):
            self._input = sys.stdin.readline

        def readline(self) -> str:
            return self._input().strip()

        def read_int(self) -> int:
            return int(self.readline())

        def read_two_ints(self) -> tuple[int, int]:
            line = self.readline()
            parts = line.split()
            return int(parts[0]), int(parts[1])

    input_handler = InputHandler()
    n = input_handler.read_int()
    a, b = input_handler.read_two_ints()

    trainer = CalculationTraining(n, a, b)
    final_a, final_b = trainer.compute()

    print(final_a, final_b)


if __name__ == "__main__":
    main()