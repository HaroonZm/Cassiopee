import sys
from typing import List, Tuple, Iterator

class ModuloArithmetic:
    def __init__(self, modulus: int):
        self.modulus = modulus

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.modulus

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.modulus

class Vector:
    def __init__(self, data: List[int], mod: ModuloArithmetic):
        self.data = data
        self.mod = mod
        self.size = len(data)

    def __getitem__(self, idx: int) -> int:
        if 0 <= idx < self.size:
            return self.data[idx]
        else:
            return 0

    def __setitem__(self, idx: int, value: int):
        if 0 <= idx < self.size:
            self.data[idx] = value % self.mod.modulus

    def copy(self) -> 'Vector':
        return Vector(self.data.copy(), self.mod)

    def __str__(self):
        return " ".join(str(x) for x in self.data)

class Matrix:
    def __init__(self, n: int, mod: ModuloArithmetic):
        self.n = n
        self.mod = mod
        # initialize with zero matrix
        self.data = [[0]*n for _ in range(n)]

    @classmethod
    def construct_transition_matrix(cls, n: int, A: int, B: int, C: int, mod: ModuloArithmetic) -> 'Matrix':
        mat = cls(n, mod)
        for i in range(n):
            # left neighbor
            if i-1 >= 0:
                mat.data[i][i-1] = A % mod.modulus
            # self
            mat.data[i][i] = B % mod.modulus
            # right neighbor
            if i+1 < n:
                mat.data[i][i+1] = C % mod.modulus
        return mat

    def mul_vector(self, vec: Vector) -> Vector:
        result_data = [0]*self.n
        for i in range(self.n):
            s = 0
            for j in range(self.n):
                s += self.mod.mul(self.data[i][j], vec[j])
            result_data[i] = s % self.mod.modulus
        return Vector(result_data, self.mod)

    def mul_matrix(self, other: 'Matrix') -> 'Matrix':
        assert self.n == other.n and self.mod.modulus == other.mod.modulus
        n = self.n
        mod = self.mod
        res = Matrix(n, mod)
        for i in range(n):
            for j in range(n):
                s = 0
                for k in range(n):
                    s += mod.mul(self.data[i][k], other.data[k][j])
                res.data[i][j] = s % mod.modulus
        return res

    def pow(self, exponent: int) -> 'Matrix':
        result = Matrix.identity(self.n, self.mod)
        base = self
        e = exponent
        while e > 0:
            if e & 1:
                result = result.mul_matrix(base)
            base = base.mul_matrix(base)
            e >>= 1
        return result

    @classmethod
    def identity(cls, n: int, mod: ModuloArithmetic) -> 'Matrix':
        I = cls(n, mod)
        for i in range(n):
            I.data[i][i] = 1 % mod.modulus
        return I

class AutomatonDefinition:
    def __init__(self, N: int, M: int, A: int, B: int, C: int, T: int):
        self.N = N
        self.M = M
        self.A = A
        self.B = B
        self.C = C
        self.T = T

class Automaton:
    def __init__(self, definition: AutomatonDefinition, initial_state: Vector):
        self.defn = definition
        self.mod = ModuloArithmetic(self.defn.M)
        self.state = initial_state
        self.transition_matrix = Matrix.construct_transition_matrix(
            self.defn.N, self.defn.A, self.defn.B, self.defn.C, self.mod)

    def evolve(self, steps: int) -> Vector:
        # We use matrix exponentiation to efficiently compute the state at time T.
        # state(T) = transition_matrix^T * state(0)
        if steps == 0:
            return self.state.copy()
        powered = self.transition_matrix.pow(steps)
        return powered.mul_vector(self.state)

def parse_input() -> Iterator[Tuple[AutomatonDefinition, Vector]]:
    for line in sys.stdin:
        if not line.strip():
            continue
        parts = list(map(int, line.split()))
        if len(parts) != 6:
            continue
        N, M, A, B, C, T = parts
        if N == 0 and M == 0 and A == 0 and B == 0 and C == 0 and T == 0:
            break
        # read next line for initial state
        initial_line = next(sys.stdin)
        initial_states = list(map(int, initial_line.split()))
        if len(initial_states) != N:
            # malformed input, ignore
            continue
        defn = AutomatonDefinition(N, M, A, B, C, T)
        mod = ModuloArithmetic(M)
        state = Vector(initial_states, mod)
        yield defn, state

def main():
    for defn, initial_state in parse_input():
        automaton = Automaton(defn, initial_state)
        result = automaton.evolve(defn.T)
        print(result)

if __name__ == "__main__":
    main()