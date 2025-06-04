from typing import List, Tuple, Union, Optional
import sys


class SalesTable:
    """
    Abstraction of the sales table data with products and stores,
    including totals and unknown variables represented as question marks.
    """

    def __init__(self, p: int, s: int, raw_rows: List[List[str]]):
        self.p = p  # number of products (rows, excluding total line)
        self.s = s  # number of stores (columns, excluding total column)
        self.known_data = [[None for _ in range(s)] for _ in range(p)]  # type: List[List[Optional[int]]]
        self.product_totals = [0 for _ in range(p)]  # length p
        self.store_totals = [0 for _ in range(s)]  # length s
        self.overall_total = 0

        # Variables keep track of '?' positions in reading order
        self.variable_positions = []  # List[Tuple[int, int]] (row, col)
        self._parse_raw_input(raw_rows)

    def _parse_raw_input(self, raw_rows: List[List[str]]):
        # Parse product rows and their totals
        for i in range(self.p):
            for j in range(self.s):
                val = raw_rows[i][j]
                if val == '?':
                    # Mark unknown
                    self.known_data[i][j] = None
                    self.variable_positions.append((i, j))
                else:
                    self.known_data[i][j] = int(val)
            self.product_totals[i] = int(raw_rows[i][self.s])

        # Last line is store totals and overall total
        for j in range(self.s):
            self.store_totals[j] = int(raw_rows[self.p][j])
        self.overall_total = int(raw_rows[self.p][self.s])

    def total_variables(self) -> int:
        return len(self.variable_positions)

    def build_equations(self) -> Tuple[List[List[int]], List[int]]:
        """
        Constructs a system of linear equations according to the constraints:
        - sum over stores for each product = product total
        - sum over products for each store = store total
        Represent each unknown as a variable in order of variable_positions.
        Output:
            A: coefficient matrix (List of List of ints)
            b: constants vector
        """
        var_index_map = {}  # (i,j) -> index of variable
        for idx, pos in enumerate(self.variable_positions):
            var_index_map[pos] = idx

        num_vars = len(self.variable_positions)
        equations = []
        constants = []

        # Equations for products: sum of variables + known = product total
        for i in range(self.p):
            coeffs = [0] * num_vars
            constant_part = 0
            for j in range(self.s):
                val = self.known_data[i][j]
                if val is None:
                    coeffs[var_index_map[(i, j)]] = 1
                else:
                    constant_part += val
            equations.append(coeffs)
            constants.append(self.product_totals[i] - constant_part)

        # Equations for stores: sum of variables + known = store total
        for j in range(self.s):
            coeffs = [0] * num_vars
            constant_part = 0
            for i in range(self.p):
                val = self.known_data[i][j]
                if val is None:
                    coeffs[var_index_map[(i, j)]] += 1
                else:
                    constant_part += val
            equations.append(coeffs)
            constants.append(self.store_totals[j] - constant_part)

        return equations, constants


class LinearEquationSolver:
    """
    A generic solver for systems of linear equations with integer coefficients,
    using Gaussian elimination with rational arithmetic for correctness.
    """

    class Rational:
        """
        Rational number class to avoid floating point inaccuracies.
        """
        def __init__(self, numerator: int, denominator: int = 1):
            if denominator == 0:
                raise ZeroDivisionError("Denominator cannot be zero")
            sign = 1
            if numerator < 0:
                sign *= -1
                numerator = -numerator
            if denominator < 0:
                sign *= -1
                denominator = -denominator
            g = self._gcd(numerator, denominator)
            self.n = sign * (numerator // g)
            self.d = denominator // g

        @staticmethod
        def _gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        def __add__(self, other: "LinearEquationSolver.Rational") -> "LinearEquationSolver.Rational":
            n = self.n * other.d + other.n * self.d
            d = self.d * other.d
            return LinearEquationSolver.Rational(n, d)

        def __sub__(self, other: "LinearEquationSolver.Rational") -> "LinearEquationSolver.Rational":
            n = self.n * other.d - other.n * self.d
            d = self.d * other.d
            return LinearEquationSolver.Rational(n, d)

        def __mul__(self, other: "LinearEquationSolver.Rational") -> "LinearEquationSolver.Rational":
            n = self.n * other.n
            d = self.d * other.d
            return LinearEquationSolver.Rational(n, d)

        def __truediv__(self, other: "LinearEquationSolver.Rational") -> "LinearEquationSolver.Rational":
            if other.n == 0:
                raise ZeroDivisionError("division by zero")
            n = self.n * other.d
            d = self.d * other.n
            return LinearEquationSolver.Rational(n, d)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, LinearEquationSolver.Rational):
                return False
            return self.n == other.n and self.d == other.d

        def is_zero(self) -> bool:
            return self.n == 0

        def __str__(self) -> str:
            if self.d == 1:
                return str(self.n)
            return f"{self.n}/{self.d}"

        def to_int_or_none(self) -> Optional[int]:
            if self.d == 1:
                return self.n
            # Rational number must be integer for this problem
            return None

    def __init__(self, A: List[List[int]], b: List[int]):
        self.n_eq = len(A)  # number of equations
        self.n_var = len(A[0]) if A else 0  # number of variables
        # Store augmented matrix as rationals
        self.matrix = [[LinearEquationSolver.Rational(A[i][j]) for j in range(self.n_var)] + 
                       [LinearEquationSolver.Rational(b[i])] for i in range(self.n_eq)]

    def solve(self) -> Union[str, List[int]]:
        """
        Solve the linear system using Gaussian elimination with rational arithmetic.
        Return:
          - "NO" if no unique solution exists,
          - list of integers representing unique solution otherwise.
        """
        A = self.matrix

        row = 0
        col = 0
        where = [-1] * self.n_var  # where[i] = index of row where variable i is pivot

        while row < self.n_eq and col < self.n_var:
            # Find pivot
            pivot = row
            while pivot < self.n_eq and A[pivot][col].is_zero():
                pivot += 1
            if pivot == self.n_eq:
                col += 1
                continue
            if pivot != row:
                A[row], A[pivot] = A[pivot], A[row]

            where[col] = row

            # Normalize pivot row
            pivot_val = A[row][col]
            for c in range(col, self.n_var +1):
                A[row][c] = A[row][c] / pivot_val

            # Eliminate from other rows
            for r in range(self.n_eq):
                if r != row and not A[r][col].is_zero():
                    factor = A[r][col]
                    for c in range(col, self.n_var +1):
                        A[r][c] = A[r][c] - factor * A[row][c]

            row += 1
            col += 1

        # Check for inconsistency:
        for r in range(row, self.n_eq):
            if not A[r][self.n_var].is_zero():
                # 0 = nonzero implies no solution
                return "NO"

        # Check if system has unique solution
        # If some variables have no pivot (where[i] == -1), infinite solutions
        if any(w == -1 for w in where):
            return "NO"

        # Retrieve solution
        solution = [LinearEquationSolver.Rational(0) for _ in range(self.n_var)]
        for i in range(self.n_var):
            r = where[i]
            if r == -1:
                # No pivot for variable i, infinite solutions
                return "NO"
            solution[i] = A[r][self.n_var]

        # Check that solution is integral for this problem
        int_solution = []
        for val in solution:
            intval = val.to_int_or_none()
            if intval is None:
                # Non-integer solution means problem requirement not matched
                return "NO"
            int_solution.append(intval)

        return int_solution


class ToshizoReconstructor:
    """
    High-level orchestrator class that uses SalesTable abstraction and linear solver
    to solve the Missing Numbers problem.
    """

    def __init__(self):
        self.results = []  # type: List[Union[str, List[int]]]

    def process_dataset(self, p: int, s: int, raw_rows: List[List[str]]):
        table = SalesTable(p, s, raw_rows)
        equations, constants = table.build_equations()
        solver = LinearEquationSolver(equations, constants)
        solution = solver.solve()
        self.results.append(solution)

    def print_results(self):
        first = True
        for res in self.results:
            if not first:
                print()
            first = False
            if res == "NO":
                print("NO")
            else:
                for val in res:
                    print(val)


def read_input() -> List[Tuple[int, int, List[List[str]]]]:
    """
    Reads data sets until '0' line.
    Returns list of tuples (p, s, raw_rows).
    """
    data_sets = []
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return data_sets
        if line.strip() == '0':
            break
        p_s = line.strip().split()
        if len(p_s) != 2:
            continue
        p, s = int(p_s[0]), int(p_s[1])
        raw_rows = []
        lines_read = 0
        total_lines = p + 1
        while lines_read < total_lines:
            row_line = sys.stdin.readline()
            if row_line == '':
                break
            if row_line.strip() == '':
                continue
            parts = row_line.strip().split()
            if len(parts) != (s + 1):
                continue
            raw_rows.append(parts)
            lines_read +=1
        if len(raw_rows) == total_lines:
            data_sets.append((p, s, raw_rows))
    return data_sets


def main():
    reconstructor = ToshizoReconstructor()
    datasets = read_input()
    for p, s, raw_rows in datasets:
        reconstructor.process_dataset(p, s, raw_rows)
    reconstructor.print_results()


if __name__ == '__main__':
    main()