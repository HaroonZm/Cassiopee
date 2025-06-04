import sys
from typing import List, Tuple

MOD = 10**9 + 7

class ModularArithmetic:
    """A class to handle modular arithmetic operations."""
    def __init__(self, modulus: int):
        self.mod = modulus

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.mod

    def sub(self, a: int, b: int) -> int:
        return (a - b) % self.mod

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.mod

    def pow(self, base: int, exponent: int) -> int:
        result = 1
        cur = base % self.mod
        e = exponent
        while e > 0:
            if e & 1:
                result = self.mul(result, cur)
            cur = self.mul(cur, cur)
            e >>= 1
        return result

    def inv(self, a: int) -> int:
        # Fermat's little theorem assuming mod prime
        return self.pow(a, self.mod - 2)

    def div(self, a: int, b: int) -> int:
        return self.mul(a, self.inv(b))


class WaysCounterInterface:
    """Interface for counting ways to eat cookies."""
    def count_ways(self, N: int, D: int, X: int) -> int:
        raise NotImplementedError


class WaysCounterDP(WaysCounterInterface):
    """
    Count ways to represent N as a sum of D positive integers each < X.
    Uses combinatorial methods and matrix exponentiation for large D.
    """
    def __init__(self, mod_arith: ModularArithmetic):
        self.mod_arith = mod_arith

    def prefix_sums(self, arr: List[int]) -> List[int]:
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i + 1] = self.mod_arith.add(prefix[i], arr[i])
        return prefix

    def build_transition_matrix(self, max_sum: int, X: int) -> List[List[int]]:
        """
        Build the (max_sum + 1) x (max_sum + 1) transition matrix T,
        where:
         dp_day[i] = sum_{j=1 to X-1} dp_day-1[i-j]
        We'll build T such that:
         new_dp = T * old_dp
        where old_dp and new_dp are vectors of size max_sum + 1.
        The matrix is mostly banded:
            T[i][j] = 1 if i-j in [1, X-1], else 0
         plus T[0][0] = 1 (to keep sum=0 stable)
        """
        size = max_sum + 1
        T = [[0]*size for _ in range(size)]
        # For sum=0, dp for 0 cookies eaten: remains 1 only with no eaten cookies (0)
        T[0][0] = 1  
        for i in range(1, size):
            # dp_day[i] = sum of dp_day-1[i-k] for k=1..X-1 if i-k >= 0
            # So for each j, T[i][j] = 1 iff i-j in [1,X-1]
            start = max(i - (X - 1), 0)
            end = i - 1
            for j in range(start, end + 1):
                T[i][j] = 1
        return T

    def matmul(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size = len(A)
        C = [[0]*size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                a = A[i][k]
                if a == 0:
                    continue
                for j in range(size):
                    C[i][j] = (C[i][j] + a * B[k][j]) % self.mod_arith.mod
        return C

    def matvecmul(self, M: List[List[int]], v: List[int]) -> List[int]:
        size = len(v)
        res = [0]*size
        for i in range(size):
            s = 0
            row = M[i]
            for j in range(size):
                if row[j] != 0 and v[j] != 0:
                    s += row[j] * v[j]
            res[i] = s % self.mod_arith.mod
        return res

    def matpow(self, base: List[List[int]], exponent: int) -> List[List[int]]:
        size = len(base)
        result = [[0]*size for _ in range(size)]
        for i in range(size):
            result[i][i] = 1
        cur = base
        e = exponent
        while e > 0:
            if e & 1:
                result = self.matmul(result, cur)
            cur = self.matmul(cur, cur)
            e >>= 1
        return result

    def count_ways(self, N: int, D: int, X: int) -> int:
        # If impossible to sum N by D positive ints < X, return 0 quickly:
        # minimal sum: D*1 = D, maximal sum: D*(X-1)
        if N < D or N > D*(X-1):
            return 0

        # We're to count sequences (a_1,...,a_D) with each 1 <= a_i < X, sum a_i = N
        # Let b_i = a_i - 1 => b_i >= 0 and b_i < X-1 (X-1 possibilities)
        # Sum b_i = N - D
        # Count number of sequences of length D summing to (N-D) with each element in [0,X-2]

        target = N - D
        max_sum = target

        # dp for day 1:
        # dp_1[i] = 1 if 0 <= i < X-1 else 0
        dp_init = [0]*(max_sum+1)
        for i in range(min(X-1, max_sum+1)):
            dp_init[i] = 1

        # build transition matrix T of size (max_sum+1) x (max_sum+1)
        T = self.build_transition_matrix(max_sum, X)

        # matrix exponentiation: dp_D = T^(D-1)*dp_1
        if D == 1:
            dp_final = dp_init
        else:
            T_pow = self.matpow(T, D-1)
            dp_final = self.matvecmul(T_pow, dp_init)

        return dp_final[target] % self.mod_arith.mod


class CookieEatingSolver:
    """
    High-level solver managing input datasets and dispatching to the counting algorithm.
    Designed with extensibility for alternative solutions or constraints.
    """
    def __init__(self):
        self.mod_arith = ModularArithmetic(MOD)
        self.counter = WaysCounterDP(self.mod_arith)

    def parse_input(self, lines: List[str]) -> List[Tuple[int, int, int]]:
        datasets = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 3:
                continue
            N, D, X = map(int, parts)
            if N == 0 and D == 0 and X == 0:
                break
            datasets.append((N, D, X))
        return datasets

    def solve_dataset(self, N: int, D: int, X: int) -> int:
        return self.counter.count_ways(N, D, X)

    def solve_all(self, lines: List[str]) -> List[int]:
        datasets = self.parse_input(lines)
        results = []
        for (N, D, X) in datasets:
            res = self.solve_dataset(N, D, X)
            results.append(res)
        return results


def main():
    solver = CookieEatingSolver()
    input_lines = sys.stdin.read().strip().split('\n')
    results = solver.solve_all(input_lines)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()